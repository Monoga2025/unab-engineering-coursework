"""Editable, deterministic Geneva conveyor generator for Blender 4.2.
Run: blender -b --python geneva_conveyor_generator.py -- --mode build
All geometry and animation are generated locally, with no external dependencies.
"""
import argparse
import math
import os
import sys
from pathlib import Path

import bpy
from mathutils import Vector

MOTOR_RPM = 60
GENEVA_SLOTS = 4
SIMULATION_SECONDS = 5
FPS = 30
CENTER_DISTANCE = 1.10
PIN_RADIUS = CENTER_DISTANCE * math.sin(math.pi / GENEVA_SLOTS)
STEP = 2 * math.pi / GENEVA_SLOTS
ROOT = Path(__file__).resolve().parent
COLLECTIONS = {}
MATERIALS = {}
D = Vector((-2.8, -1.35, 1.22))
G = D + Vector((CENTER_DISTANCE, 0, 0))
SCENE = bpy.context.scene


def angle_at(t):
    cycles = t * MOTOR_RPM / 60
    k = math.floor(cycles)
    theta = 2 * math.pi * (cycles - k - .5)
    alpha = math.pi / 2 - math.pi / GENEVA_SLOTS
    if theta < -alpha:
        return -k * STEP
    if theta > alpha:
        return -(k + 1) * STEP
    return -k * STEP - math.pi / GENEVA_SLOTS - math.atan2(
        PIN_RADIUS * math.sin(theta), CENTER_DISTANCE - PIN_RADIUS * math.cos(theta))


def verify():
    if GENEVA_SLOTS != 4:
        raise ValueError('This production geometry supports exactly four Geneva slots.')
    period = 60 / MOTOR_RPM
    for k in range(16):
        assert abs(angle_at(k * period) + k * STEP) < 1e-10
        assert abs(angle_at((k + .2) * period) - angle_at(k * period)) < 1e-10
        assert abs(angle_at((k + .8) * period) - angle_at((k + 1) * period)) < 1e-10
    worst = 0
    for i in range(251):
        t = .375 + .25 * i / 250
        theta = 2 * math.pi * (t - .5)
        v = Vector((PIN_RADIUS * math.cos(theta) - CENTER_DISTANCE,
                    PIN_RADIUS * math.sin(theta)))
        ray = math.pi + math.pi / 4 + angle_at(t * period)
        residual = abs(v.x * math.sin(ray) - v.y * math.cos(ray))
        worst = max(worst, residual)
    assert worst < 1e-6, worst
    report = ('Analytic verification PASSED\n60 RPM = 1 revolution/second\n'
              '4 slots; 90 degrees per cycle; 75% dwell; 25% engagement\n'
              f'Maximum pin/slot collinearity residual: {worst:.3e} m\n'
              'Verified 16 cycles and 251 engagement samples.\n')
    (ROOT / 'kinematic_verification.txt').write_text(report, encoding='utf-8')
    print(report)


def collection(name):
    c = bpy.data.collections.new(name)
    SCENE.collection.children.link(c)
    COLLECTIONS[name] = c
    return c


def move(obj, group):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    COLLECTIONS[group].objects.link(obj)
    return obj


def material(name, color, metallic=0, rough=.4):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (*color, 1)
    bsdf.inputs['Metallic'].default_value = metallic
    bsdf.inputs['Roughness'].default_value = rough
    MATERIALS[name] = m
    return m


def finish(obj, name, mat, group, bevel=0):
    obj.name = name
    move(obj, group)
    if mat:
        obj.data.materials.append(MATERIALS[mat])
    if bevel:
        mod = obj.modifiers.new('Manufactured edge radius', 'BEVEL')
        mod.width = bevel
        mod.segments = 3
        mod = obj.modifiers.new('Weighted normals', 'WEIGHTED_NORMAL')
    return obj


def box(name, loc, scale, mat='Aluminum', group='03_STRUCTURE', bevel=.025):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finish(obj, name, mat, group, bevel)


def cylinder(name, loc, radius, depth, mat='Steel', group='01_GENEVA', axis='Z', bevel=.01):
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=radius, depth=depth, location=loc)
    obj = bpy.context.object
    if axis == 'X':
        obj.rotation_euler.y = math.pi / 2
    elif axis == 'Y':
        obj.rotation_euler.x = math.pi / 2
    return finish(obj, name, mat, group, bevel)


def empty(name, loc, group):
    obj = bpy.data.objects.new(name, None)
    COLLECTIONS[group].objects.link(obj)
    obj.location = loc
    return obj


def parent(obj, root):
    matrix = obj.matrix_world.copy()
    obj.parent = root
    obj.matrix_world = matrix
    return obj


def cut(obj, cutter):
    bpy.context.view_layer.objects.active = obj
    mod = obj.modifiers.new('Machined subtraction', 'BOOLEAN')
    mod.operation = 'DIFFERENCE'
    mod.object = cutter
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(cutter, do_unlink=True)


def text(name, body, loc, size=.12, mat='White', group='05_FACTORY', rotation=(math.pi / 2, 0, 0)):
    curve = bpy.data.curves.new(name, 'FONT')
    curve.body = body
    curve.size = size
    curve.extrude = .0005
    obj = bpy.data.objects.new(name, curve)
    COLLECTIONS[group].objects.link(obj)
    obj.location = loc
    obj.rotation_euler = rotation
    obj.data.materials.append(MATERIALS[mat])
    return obj


def key(obj, path, frame):
    obj.keyframe_insert(data_path=path, frame=frame)


def linear(obj):
    if obj.animation_data and obj.animation_data.action:
        for fc in obj.animation_data.action.fcurves:
            for point in fc.keyframe_points:
                point.interpolation = 'LINEAR'


def setup():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for c in list(bpy.data.collections):
        if not c.objects:
            bpy.data.collections.remove(c)
    for n in ('01_GENEVA', '02_CONVEYOR', '03_STRUCTURE', '04_PRODUCTS', '05_FACTORY', '06_LIGHTS', '07_CAMERAS'):
        collection(n)
    material('Steel', (.35, .42, .49), .88, .25)
    material('Machined silver', (.62, .72, .8), .85, .21)
    material('Dark drive steel', (.055, .085, .115), .8, .28)
    material('Aluminum', (.31, .39, .43), .8, .32)
    material('Rubber', (.014, .022, .027), .05, .72)
    material('Safety yellow', (.92, .52, .035), .3, .34)
    material('White', (.82, .89, .9), .1, .45)
    material('Carton', (.42, .24, .10), .0, .7)
    material('Label', (.74, .78, .72), .0, .65)
    material('Floor', (.085, .115, .14), .25, .5)
    material('Panel', (.035, .065, .09), .5, .38)
    material('Cyan', (.015, .62, .74), .25, .3)
    material('Green', (.05, .75, .3), .1, .3)
    SCENE.unit_settings.system = 'METRIC'
    SCENE.unit_settings.scale_length = .25
    SCENE.render.engine = 'BLENDER_EEVEE_NEXT'
    SCENE.eevee.shadow_ray_count = 4
    SCENE.render.resolution_x = 1920
    SCENE.render.resolution_y = 1080
    SCENE.render.resolution_percentage = 100
    SCENE.render.fps = FPS
    SCENE.render.image_settings.file_format = 'PNG'
    SCENE.render.film_transparent = False
    SCENE.world.color = (.14, .14, .14)
    SCENE.world.use_nodes = True
    SCENE.world.node_tree.nodes['Background'].inputs[0].default_value = (.06, .085, .12, 1)
    SCENE.world.node_tree.nodes['Background'].inputs[1].default_value = .35
    SCENE.view_settings.view_transform = 'AgX'
    SCENE.view_settings.exposure = -.7
    SCENE.render.image_settings.color_mode = 'RGB'
    SCENE['MOTOR_RPM'] = MOTOR_RPM
    SCENE['GENEVA_SLOTS'] = GENEVA_SLOTS
    SCENE['SIMULATION_SECONDS'] = SIMULATION_SECONDS
    SCENE['Kinematics'] = 'Analytic external Geneva; active .375-.625 seconds; baked at 120 Hz.'


def mechanism():
    driver = empty('DRIVER_60_RPM', D, '01_GENEVA')
    driven = empty('GENEVA_4_SLOT_INDEX', G, '01_GENEVA')
    cylinder('Driver bearing block', D + Vector((0, 0, -.22)), .22, .16, 'Aluminum')
    cylinder('Driven bearing block', G + Vector((0, 0, -.22)), .25, .16, 'Aluminum')
    for loc in (D, G):
        box('Bearing plinth', loc + Vector((0, 0, -.34)), (.58, .58, .12), 'Dark drive steel', '01_GENEVA')
        for sx in (-1, 1):
            for sy in (-1, 1):
                cylinder('Socket head fastener', loc + Vector((sx * .21, sy * .21, -.27)), .036, .036, 'Steel')
    disk = cylinder('Continuous input flywheel', D, .85, .12, 'Dark drive steel')
    parent(disk, driver)
    pin = cylinder('Eccentric hardened pin', D + Vector((PIN_RADIUS, 0, .19)), .065, .31, 'Machined silver')
    parent(pin, driver)
    wheel = cylinder('Geneva star - four open radial slots', G + Vector((0, 0, .19)), .80, .16, 'Machined silver', bevel=0)
    for n in range(GENEVA_SLOTS):
        a = math.pi + math.pi / 4 + n * STEP
        loc = G + Vector((.67 * math.cos(a), .67 * math.sin(a), .19))
        cutter = box('Slot cutter', loc, (.98, .151, .5), None, '01_GENEVA', 0)
        cutter.rotation_euler.z = a
        cut(wheel, cutter)
        # Mating concave dwell surfaces between the radial slots.
        a2 = a + STEP / 2
        cutter = cylinder('Locking arc cutter', G + Vector((CENTER_DISTANCE * math.cos(a2), CENTER_DISTANCE * math.sin(a2), .19)), .545, .5, None, bevel=0)
        cut(wheel, cutter)
    bevel = wheel.modifiers.new('Slot edge chamfer', 'BEVEL')
    bevel.width = .009
    bevel.segments = 2
    parent(wheel, driven)
    # Locking disk: remove the sector around the pin for the indexing phase.
    lock = cylinder('Circular dwell locking cam', D + Vector((0, 0, .19)), .53, .13, 'Dark drive steel', bevel=0)
    cutter = box('Cam clearance cutter', D + Vector((.65, 0, .19)), (.98, 1.4, .5), None, '01_GENEVA', 0)
    cut(lock, cutter)
    parent(lock, driver)
    for name, p, root in [('Input shaft', D, driver), ('Output vertical shaft', G, driven)]:
        parent(cylinder(name, p + Vector((0, 0, -.03)), .12, .68, 'Steel'), root)
        parent(cylinder(name + ' retaining cap', p + Vector((0, 0, .35)), .19, .065, 'Dark drive steel'), root)
        parent(cylinder(name + ' center bolt', p + Vector((0, 0, .39)), .06, .035, 'Steel'), root)
    # Radial index marks read clearly from the top camera.
    for n in range(4):
        a = n * STEP
        marker = box('Output quadrant mark', G + Vector((.46 * math.cos(a), .46 * math.sin(a), .278)), (.12, .025, .004), 'Safety yellow' if n == 0 else 'Dark drive steel', '01_GENEVA', .002)
        marker.rotation_euler.z = a
        parent(marker, driven)
    for root in (driver, driven):
        for i in range(15 * FPS * 4 + 1):
            t = i / (FPS * 4)
            root.rotation_euler.z = 2 * math.pi * (t * MOTOR_RPM / 60 - .5) if root == driver else angle_at(t)
            key(root, 'rotation_euler', 1 + i / 4)
        linear(root)
    return driver, driven


def hand_crank(driver):
    """Radial hand crank on the continuous input wheel, opposite the Geneva cross.

    The arm and vertical grip are parented to the driver empty, so they rotate with
    the wheel exactly like a hand would turn it. Sized for 3D printing.
    """
    hub = cylinder('Crank hub', D + Vector((0, 0, .34)), .16, .10, 'Machined silver',
                   '01_GENEVA', 'Z', bevel=.012)
    parent(hub, driver)
    arm = box('Crank arm', D + Vector((-.44, 0, .34)), (.92, .11, .07),
              'Machined silver', '01_GENEVA', .02)
    arm.rotation_euler.z = 0
    parent(arm, driver)
    grip = cylinder('Crank hand grip', D + Vector((-.86, 0, .50)), .052, .30,
                    'Safety yellow', '01_GENEVA', 'Z', bevel=.02)
    parent(grip, driver)
    parent(cylinder('Crank grip retaining cap', D + Vector((-.86, 0, .66)), .075, .04,
                    'Dark drive steel', '01_GENEVA', 'Z', bevel=.01), driver)
    return driver


def apply_solidworks_style():
    """Flat, CAD-style viewport look: Workbench studio shading, plain background,
    black object outlines and light cavity. No cinematic lights or environment."""
    SCENE.render.engine = 'BLENDER_WORKBENCH'
    shading = SCENE.display.shading
    shading.light = 'STUDIO'
    shading.studio_light = 'Default'
    shading.color_type = 'MATERIAL'
    shading.show_shadows = False
    shading.show_cavity = True
    shading.cavity_type = 'BOTH'
    shading.curvature_ridge_factor = 1.0
    shading.curvature_valley_factor = 1.0
    shading.show_object_outline = True
    shading.object_outline_color = (0, 0, 0)
    shading.show_specular_highlight = True
    shading.background_type = 'WORLD'
    shading.background_color = (1.0, 1.0, 1.0)
    SCENE.world.use_nodes = True
    SCENE.world.node_tree.nodes['Background'].inputs[0].default_value = (1.0, 1.0, 1.0, 1)
    SCENE.world.node_tree.nodes['Background'].inputs[1].default_value = 1.0
    SCENE.display.render_aa = '8'
    print('STYLE-DEBUG', SCENE.render.engine, shading.background_type,
          tuple(shading.background_color), SCENE.render.film_transparent)
    SCENE.view_settings.view_transform = 'Standard'
    SCENE.view_settings.look = 'None'
    SCENE.render.film_transparent = False
    for name in ('05_FACTORY',):
        COLLECTIONS[name].hide_render = True
        COLLECTIONS[name].hide_viewport = True


def export_stl(parts=None):
    """Export printable parts as individual binary STL files."""
    folder = ROOT / 'stl'
    folder.mkdir(exist_ok=True)
    targets = parts or [
        'Continuous input flywheel', 'Eccentric hardened pin',
        'Geneva star - four open radial slots', 'Circular dwell locking cam',
        'Crank hub', 'Crank arm', 'Crank hand grip',
        'Input shaft', 'Output vertical shaft',
    ]
    written = []
    for name in targets:
        obj = bpy.data.objects.get(name)
        if not obj:
            continue
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        path = folder / (name.replace(' ', '_').replace('/', '-') + '.stl')
        bpy.ops.wm.stl_export(filepath=str(path), export_selected_objects=True,
                              global_scale=1.0, apply_modifiers=True)
        written.append(str(path))
        print('EXPORTED', path)
    return written


def light(name, loc, power, color, size, target):
    data = bpy.data.lights.new(name, 'AREA')
    data.energy = power
    data.color = color
    data.shape = 'DISK'
    data.size = size
    obj = bpy.data.objects.new(name, data)
    COLLECTIONS['06_LIGHTS'].objects.link(obj)
    obj.location = loc
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat('-Z', 'Y').to_euler()


def camera(name, loc, target, lens=45, ortho=None):
    data = bpy.data.cameras.new(name)
    obj = bpy.data.objects.new(name, data)
    COLLECTIONS['07_CAMERAS'].objects.link(obj)
    obj.location = loc
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat('-Z', 'Y').to_euler()
    data.lens = lens
    data.clip_end = 150
    if ortho:
        data.type = 'ORTHO'
        data.ortho_scale = ortho
    return obj


def save():
    source = bpy.data.texts.get('geneva_conveyor_generator.py') or bpy.data.texts.new('geneva_conveyor_generator.py')
    source.clear()
    source.write(Path(__file__).read_text(encoding='utf-8'))
    for marker in SCENE.timeline_markers:
        marker.camera = None
    for obj in COLLECTIONS['07_CAMERAS'].objects:
        if obj.type == 'FONT':
            if obj.animation_data and obj.animation_data.action:
                obj.animation_data.action.use_fake_user = True
                obj['HUD_ACTION'] = obj.animation_data.action.name
                obj.animation_data.action = None
            obj.hide_render = True
            obj.hide_viewport = True
    SCENE.frame_set(1)
    bpy.ops.wm.save_as_mainfile(filepath=str(ROOT / 'GENEVA_CONVEYOR_PROJECT.blend'))


def conveyor(marker=True):
    radius = .29
    pitch = radius * STEP
    SCENE['ROLLER_RADIUS'] = radius
    SCENE['PRODUCT_PITCH'] = pitch
    SCENE['TRANSMISSION_RATIO'] = 1.0
    SCENE['INPUT_PHASE_OFFSET'] = -math.pi
    # Open mechanical connection: vertical output shaft into a 1:1 bevel housing.
    cylinder('Output riser to bevel gearbox', (G.x, G.y, 1.17), .115, .48)
    box('Right angle bevel gearbox 1 to 1', (G.x, G.y, .99), (.48, .44, .43), 'Panel')
    cylinder('Horizontal indexed transmission shaft', (G.x, -.85, .99), .10, 1.05, axis='Y')
    cylinder('Flexible shaft coupling', (G.x, -.85, .99), .155, .22, 'Safety yellow', axis='Y')
    text('Ratio badge', '1:1', (G.x - .15, G.y - .227, .94), .105, 'White', '03_STRUCTURE')
    # A visible equal-diameter timing-pulley pair lifts the drive to roller height.
    timing_pulleys = []
    for z in (.99, 1.6):
        timing_pulleys.append(cylinder('1 to 1 timing pulley', (G.x, -.34, z), .17, .11, 'Safety yellow', '02_CONVEYOR', 'Y'))
        cylinder('Timing belt pulley wrap', (G.x, -.34, z), .177, .065, 'Rubber', '02_CONVEYOR', 'Y')
    for x in (G.x - .175, G.x + .175):
        box('Vertical synchronous timing belt', (x, -.34, 1.295), (.028, .068, .61), 'Rubber', '02_CONVEYOR', .004)
    rollers = []
    for x, name in ((-1.7, 'DRIVE_ROLLER'), (3.85, 'RETURN_ROLLER')):
        roller = cylinder(name, (x, .42, 1.6), radius, 1.15, 'Dark drive steel', '02_CONVEYOR', 'Y')
        rollers.append(roller)
        for y in (-.24, 1.08):
            box('Roller bearing housing', (x, y, 1.6), (.3, .18, .35), 'Aluminum')
            cylinder('Roller bearing visible cap', (x, y - .1, 1.6), .12, .04, 'Steel', '03_STRUCTURE', 'Y')
    box('Upper dark rubber belt', (1.075, .42, 1.892), (5.55, 1.1, .035), 'Rubber', '02_CONVEYOR', .012)
    box('Return dark rubber belt', (1.075, .42, 1.307), (5.55, 1.1, .035), 'Rubber', '02_CONVEYOR', .012)
    # Curved rubber surfaces around the ends, physically consistent with the belt path.
    for x in (-1.7, 3.85):
        cylinder('Rubber end wrap', (x, .42, 1.6), .3, 1.1, 'Rubber', '02_CONVEYOR', 'Y')
    for y in (-.23, 1.07):
        box('Longitudinal extrusion', (1.075, y, 1.36), (6.2, .12, .2))
        box('Extrusion dark channel', (1.075, y - .064, 1.36), (5.94, .006, .038), 'Dark drive steel')
        for x in (-1.55, 1.05, 3.6):
            box('Square extrusion upright', (x, y, .72), (.13, .13, 1.22))
            box('Leveling foot', (x, y, .115), (.3, .26, .12), 'Rubber')
            box('Leg mounting bracket', (x, y, 1.27), (.33, .16, .1), 'Steel')
    for x in (-1.55, 1.05, 3.6):
        box('Cross member', (x, .42, .4), (.12, 1.3, .12))
    box('Geneva structural shelf', (-2.3, -1.36, .83), (3.0, 1.65, .12), 'Aluminum')
    for x in (-3.45, -1.2):
        box('Indexer shelf support', (x, -1.4, .45), (.12, .12, .75))
    text('Machine model badge', 'INDEX / 04', (-3.38, -2.2, .82), .11, 'White', '03_STRUCTURE')
    # Discrete seams travel around both the top and the underside of the belt.
    length = 5.55
    perimeter = 2 * length + 2 * math.pi * radius
    seams = [box('Belt seam %02d' % i, (0, 0, 0), (.024, 1.06, .006), 'Aluminum', '02_CONVEYOR', .001) for i in range(32)]
    def belt_path(s):
        if s < length:
            return -1.7 + s, 1.915, 0
        s -= length
        if s < math.pi * radius:
            a = math.pi / 2 - s / radius
            return 3.85 + radius * math.cos(a), 1.6 + radius * math.sin(a), a - math.pi / 2
        s -= math.pi * radius
        if s < length:
            return 3.85 - s, 1.287, math.pi
        s -= length
        a = -math.pi / 2 - s / radius
        return -1.7 + radius * math.cos(a), 1.6 + radius * math.sin(a), a - math.pi / 2
    products = []
    count = 5
    loop_length = length
    spacing = loop_length / count
    for i in range(count):
        root = empty('PRODUCT_%02d_INDEXED' % (i + 1), (0, 0, 0), '04_PRODUCTS')
        parcel = box('Product carton %02d' % i, (0, 0, .16), (.32, .52, .32), 'Carton', '04_PRODUCTS', .02)
        parent(parcel, root)
        label = box('Product paper label %02d' % i, (0, -.264, .18), (.23, .007, .16), 'Label', '04_PRODUCTS', .003)
        parent(label, root)
        tape = box('Packaging tape %02d' % i, (0, 0, .324), (.055, .51, .004), 'Label', '04_PRODUCTS', .002)
        parent(tape, root)
        for n in range(8):
            stripe = box('Barcode stripe', (-.083 + n * .022, -.27, .18), (.005 + (n % 2) * .003, .003, .09), 'Panel', '04_PRODUCTS', 0)
            parent(stripe, root)
        products.append(root)
    # End covers conceal recycling transitions rather than making cartons teleport in view.
    for x in (-1.68, 3.83):
        box('End transfer tunnel roof', (x, .42, 2.31), (.63, 1.18, .08), 'Panel')
        for y in (-.18, 1.02):
            box('End transfer tunnel side', (x, y, 2.1), (.63, .08, .45), 'Panel')
    station_x = -1.42 + 5 * pitch
    cam_e, cam_R, cam_z = .12, .22, 3.30
    head = cam = pushrod = None
    if marker:
        for y in (-.43, 1.26):
            box('Inspection station gantry leg', (station_x, y, 2.03), (.13, .13, 1.8), 'Aluminum')
        box('Inspection station crossbeam', (station_x, .42, 2.94), (.23, 1.82, .15), 'Aluminum')
        head = box('DWELL_ONLY_INSPECTION_HEAD', (station_x, .42, 2.67), (.4, .46, .34), 'Panel')
        lens = cylinder('Inspection sensor lens', (station_x, .42, 2.48), .1, .05, 'Cyan', '03_STRUCTURE')
        parent(lens, head)
        text('Inspection station label', 'VISION  /  QC', (station_x - .18, -.448, 2.49), .08, 'White', '03_STRUCTURE')
        # Cam-driven marking head: an eccentric cam plus its pushrod visibly lower the head,
        # so the descending header is driven by a real piece instead of floating freely.
        SCENE['MARKING_CAM'] = 'Eccentric cam + pushrod lower the marking head once per input revolution (during dwell).'
        cylinder('Marking cam shaft', (station_x, .42, cam_z), .05, 1.75, 'Steel', '03_STRUCTURE', 'Y')
        for y in (-.54, 1.38):
            box('Marking cam post', (station_x, y, cam_z), (.12, .12, .58), 'Aluminum')
        cam = cylinder('Marking eccentric cam', (station_x, .42, cam_z), cam_R, .13, 'Machined silver', '03_STRUCTURE', 'Y')
        pushrod = cylinder('Marking pushrod', (station_x, .42, 2.88), .045, .28, 'Steel', '03_STRUCTURE', 'Z')
        box('Pushrod guide sleeve', (station_x, .42, 2.88), (.15, .15, .2), 'Dark drive steel')
    else:
        SCENE['MARKING_CAM'] = 'Removed: this variant keeps only the Geneva drive and the conveyor.'
    SCENE['PRODUCT_RECYCLE'] = '5 cartons; recycle at belt end inside transfer tunnels; spacing = belt_length/count.'
    for frame in range(1, 452):
        t = (frame - 1) / FPS
        angle = angle_at(t)
        travel = -angle * radius
        for roller in rollers:
            roller.rotation_euler.y = -angle
            key(roller, 'rotation_euler', frame)
        for i, obj in enumerate(seams):
            x, z, rotation = belt_path((i * perimeter / len(seams) + travel) % perimeter)
            obj.location = (x, .42, z)
            obj.rotation_euler.y = -rotation
            key(obj, 'location', frame)
            key(obj, 'rotation_euler', frame)
        for i, obj in enumerate(products):
            obj.location = (-1.7 + ((i * spacing + travel + .28) % loop_length), .42, 1.914)
            key(obj, 'location', frame)
        if marker:
            phase = (t * MOTOR_RPM / 60) % 1
            # The eccentric cam turns once per input revolution; the head is down during dwell.
            theta = 2 * math.pi * phase - math.pi / 2
            cam.location = (station_x + cam_e * math.cos(theta), .42, cam_z + cam_e * math.sin(theta))
            key(cam, 'location', frame)
            head_z = 2.75 - .22 * (.5 - .5 * math.sin(theta))
            head.location.z = head_z
            key(head, 'location', frame)
            contact_z = cam_z - cam_R + cam_e * math.sin(theta)
            head_top = head_z + .17
            pushrod.location.z = (head_top + contact_z) / 2
            pushrod.scale.z = max(.02, (contact_z - head_top) / .28)
            key(pushrod, 'location', frame)
            key(pushrod, 'scale', frame)
    animated = rollers + seams + products + ([head, cam, pushrod] if marker else [])
    for obj in animated:
        linear(obj)
    # Recycling must be discontinuous inside the tunnels, not a backward sweep across the belt.
    for obj in products:
        for fc in obj.animation_data.action.fcurves:
            if fc.data_path == 'location' and fc.array_index == 0:
                points = fc.keyframe_points
                for j in range(len(points) - 1):
                    if points[j + 1].co.y < points[j].co.y - 1:
                        points[j].interpolation = 'CONSTANT'


def factory():
    box('Factory floor', (0, 0, -.05), (25, 22, .1), 'Floor', '05_FACTORY')
    for x in range(-10, 12, 2):
        box('Floor expansion joint', (x, 0, .003), (.015, 22, .002), 'Panel', '05_FACTORY', 0)
    for y in range(-8, 10, 2):
        box('Floor expansion joint', (0, y, .003), (25, .015, .002), 'Panel', '05_FACTORY', 0)
    for y in (-3, 2.2):
        box('Safety perimeter line', (.2, y, .006), (9, .045, .008), 'Safety yellow', '05_FACTORY', 0)
    for x in (-4.3, 4.7):
        box('Safety perimeter end', (x, -.4, .006), (.045, 5.2, .008), 'Safety yellow', '05_FACTORY', 0)
    box('Back factory wall', (0, 6, 3), (25, .2, 6), 'Panel', '05_FACTORY')
    for x in (-7, -2, 3, 8):
        box('Factory wall column', (x, 5.8, 3), (.18, .3, 6), 'Aluminum', '05_FACTORY')
        box('Wall lighting strip', (x + 1.4, 5.65, 4.4), (2.3, .045, .08), 'White', '05_FACTORY')
    for z in (3.7, 3.95):
        cylinder('Utility pipeline', (0, 5.55, z), .055, 20, 'Aluminum', '05_FACTORY', 'X')
    box('Control cabinet', (3, 2.7, 1.15), (1.0, .55, 2.1), 'Aluminum', '05_FACTORY')
    box('Control panel inset', (3, 2.41, 1.56), (.74, .035, .75), 'Panel', '05_FACTORY')
    box('Touch screen', (3, 2.383, 1.65), (.5, .012, .3), 'Cyan', '05_FACTORY')
    text('HMI status', 'AUTO / 60 RPM', (2.79, 2.37, 1.63), .044, 'White')
    for x in (2.8, 3.0, 3.2):
        cylinder('Panel push button', (x, 2.36, 1.3), .035, .035, 'Safety yellow' if x == 3.2 else 'Green', '05_FACTORY', 'Y')
    text('Factory title', 'PRECISION  /  INDEXING CELL', (-3.5, 5.86, 3.0), .3, 'White')
    text('Factory subtitle', 'MECHATRONICS   |   GENEVA DRIVE', (-3.5, 5.85, 2.65), .13, 'Aluminum')
    for x in (-5.3, 5.9):
        box('Adjacent manufacturing pedestal', (x, 3.8, .6), (1.3, .9, 1.2), 'Aluminum', '05_FACTORY')
        box('Adjacent work surface', (x, 3.8, 1.24), (1.5, 1.1, .12), 'Dark drive steel', '05_FACTORY')
    light('Key large cool softbox', (-1, -4, 7), 2300, (.78, .88, 1), 5, (0, 0, 1))
    light('Warm metal rim', (2, 4, 6), 2700, (1, .8, .59), 4, (0, 0, 1))
    light('Geneva dedicated fill', (-5, -2, 4), 1050, (.7, .86, 1), 3, D)
    light('Conveyor overhead strip', (3, 0, 7), 1600, (.85, .94, 1), 4, (2, 0, 1))


CLIPS = [
    ('01_MODELO_GENERAL', 12), ('02_GINEBRA_CLOSEUP', 15),
    ('03_GINEBRA_TOP', 12), ('04_60RPM_TIMELINE', 6),
    ('05_INDEXACION_90_GRADOS', 12), ('06_BANDA_FUNCIONANDO', 15),
    ('07_AMBIENTACION_FABRICA', 15), ('08_MECANISMO_AISLADO', 10),
    ('09_COMPONENTES', 10), ('10_FINAL_CINEMATIC', 15),
]


def cameras():
    cams = []
    specs = [
        ((-7.5, -10, 7.7), (.15, -.1, 1.15), 48, None),
        ((-4.2, -4.35, 5.6), (-2.3, -1.35, 1.32), 54, None),
        ((-2.3, -1.35, 7), (-2.3, -1.35, 1.3), 50, 3.9),
        ((-2.3, -1.35, 7), (-2.3, -1.35, 1.3), 50, 4.2),
        ((-2.3, -1.35, 7), (-2.3, -1.35, 1.3), 50, 4.3),
        ((-4.6, -4.6, 3.6), (-1.5, -.7, 1.35), 50, None),
        ((-9, -12, 8.2), (.4, .8, 1.5), 42, None),
        ((-4, -4.4, 5.8), (-2.3, -1.35, 1.3), 58, None),
        ((-4.5, -5.2, 4.9), (-2.3, -1.35, 1.65), 53, None),
        ((-7.8, -9.5, 6.5), (.0, -.2, 1.15), 49, None),
    ]
    for idx, (loc, target, lens, ortho) in enumerate(specs):
        cam = camera(CLIPS[idx][0], loc, target, lens, ortho)
        cams.append(cam)
        mark = SCENE.timeline_markers.new(CLIPS[idx][0], frame=1 + idx * 45)
        # Unbound shot marker: render camera is selected explicitly per clip.
    # Gentle orbits retain the entire cell in view.
    for idx, end in ((0, (-5.8, -11.1, 7.2)), (5, (-2.3, -5.9, 3.0)), (6, (-7.7, -12.6, 8)), (9, (-5.6, -10.4, 7.5))):
        cam = cams[idx]
        target = Vector(specs[idx][1])
        key(cam, 'location', 1)
        key(cam, 'rotation_euler', 1)
        cam.location = end
        cam.rotation_euler = (target - cam.location).to_track_quat('-Z', 'Y').to_euler()
        key(cam, 'location', CLIPS[idx][1] * FPS)
        key(cam, 'rotation_euler', CLIPS[idx][1] * FPS)
    # Camera-local labels avoid obscuring the mechanism and require no handlers.
    for idx in (2, 3, 4):
        cam = cams[idx]
        half_width = cam.data.ortho_scale / 2
        half_height = half_width * 1080 / 1920
        title = text('Overlay title %02d' % idx,
                     'GINEBRA / 4 POSICIONES' if idx != 3 else 'ENTRADA CONTINUA / 60 RPM',
                     (0, 0, 0), .085, 'White', '07_CAMERAS', (0, 0, 0))
        title.parent = cam
        title.location = (-half_width + .13, half_height - .17, -2)
        for sec in range(CLIPS[idx][1] + 1):
            if idx == 4:
                body = 'VUELTA %02d    CRUZ %d°' % (sec, sec * 90)
            elif idx == 2:
                body = '%02d VUELTAS  /  1 VUELTA POR SEGUNDO' % sec
            else:
                body = '%d s     |     %d°' % (sec, sec * 360)
            label = text('Overlay %02d second %02d' % (idx, sec), body, (0, 0, 0), .1, 'Safety yellow', '07_CAMERAS', (0, 0, 0))
            label.parent = cam
            label.location = (-half_width + .13, -half_height + .13, -2)
            for frame, hidden in ((0, True), (1 + sec * FPS, False), (1 + (sec + 1) * FPS, True)):
                label.hide_render = hidden
                key(label, 'hide_render', frame)
    return cams


def configure_clip(number, cams):
    idx = number - 1
    if not 0 <= idx < len(CLIPS):
        raise ValueError('Clip must be between 1 and 10')
    SCENE.camera = cams[idx]
    # Timeline camera markers document shots but must not override a selected render camera.
    for marker in SCENE.timeline_markers:
        marker.camera = None
    SCENE.frame_start = 1
    SCENE.frame_end = CLIPS[idx][1] * FPS
    for group in ('02_CONVEYOR', '03_STRUCTURE', '04_PRODUCTS', '05_FACTORY'):
        COLLECTIONS[group].hide_render = number in (8, 9)
    for name in ('Output riser to bevel gearbox', 'Horizontal indexed transmission shaft', 'Flexible shaft coupling'):
        bpy.data.objects[name].hide_render = number in (8, 9)
    # Only the selected camera's HUD is rendered.
    for obj in COLLECTIONS['07_CAMERAS'].objects:
        if obj.type == 'FONT' and obj.parent != SCENE.camera:
            obj.animation_data_clear()
            obj.hide_render = True
    if number == 9:
        for name in ('DRIVER_60_RPM', 'GENEVA_4_SLOT_INDEX'):
            root = bpy.data.objects[name]
            root.animation_data_clear()
            root.rotation_euler.z = -math.pi if name.startswith('DRIVER') else 0
        offsets = {'Continuous input flywheel': -.5,
                   'Eccentric hardened pin': 1.2,
                   'Geneva star - four open radial slots': .8,
                   'Input shaft': .35, 'Output vertical shaft': .35,
                   'Circular dwell locking cam': .38,
                   'Input shaft retaining cap': .35, 'Input shaft center bolt': .35,
                   'Output vertical shaft retaining cap': .35, 'Output vertical shaft center bolt': .35}
        for obj in COLLECTIONS['01_GENEVA'].objects:
            if obj.name.startswith(('Bearing plinth', 'Driver bearing block', 'Driven bearing block', 'Socket head fastener')):
                offsets[obj.name] = -.65
            elif obj.name.startswith('Output quadrant mark'):
                offsets[obj.name] = .8
        for name, offset in offsets.items():
            obj = bpy.data.objects[name]
            original = obj.location.copy()
            for frame, factor in ((1, 0), (55, 0), (120, 1), (195, 1), (260, 0), (300, 0)):
                obj.location = original + Vector((0, 0, offset * factor))
                key(obj, 'location', frame)
    SCENE.frame_set(1)


def render_stills(cams):
    folder = ROOT / 'capturas'
    folder.mkdir(exist_ok=True)
    requests = [('01_general', 1, 1), ('02_geneva_pin_entry', 2, 12.25),
                ('03_geneva_moving', 2, 16), ('04_geneva_rest', 2, 26),
                ('05_conveyor', 6, 7), ('06_60rpm', 4, 91), ('07_top_view', 3, 16)]
    # Avoid destructive overlay filtering while switching still cameras.
    overlays = [o for o in COLLECTIONS['07_CAMERAS'].objects if o.type == 'FONT']
    actions = {o: o.animation_data.action for o in overlays if o.animation_data}
    for name, clip, frame in requests:
        for obj, action in actions.items():
            obj.animation_data.action = action
        SCENE.camera = cams[clip - 1]
        for marker in SCENE.timeline_markers:
            marker.camera = None
        SCENE.frame_set(int(frame), subframe=frame % 1)
        for obj in overlays:
            if obj.parent != SCENE.camera:
                if obj.animation_data:
                    obj.animation_data.action = None
                obj.hide_render = True
            elif not obj.animation_data:
                obj.hide_render = False
        SCENE.render.filepath = str(folder / (name + '.png'))
        bpy.ops.render.render(write_still=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['build', 'proof', 'stills', 'clip', 'export-stl'], default='build')
    parser.add_argument('--clip', type=int, default=1)
    parser.add_argument('--preview-frames', type=int, default=0)
    parser.add_argument('--still-frame', type=float)
    parser.add_argument('--samples', type=int, default=32)
    parser.add_argument('--percentage', type=int, default=100)
    parser.add_argument('--style', choices=['solidworks', 'factory'], default='solidworks')
    parser.add_argument('--rgba-frames', type=str, default=None)
    parser.add_argument('--no-marker', action='store_true')
    args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
    ROOT.mkdir(parents=True, exist_ok=True)
    verify()
    setup()
    driver, driven = mechanism()
    hand_crank(driver)
    conveyor(marker=not args.no_marker)
    if args.style == 'factory':
        factory()
    else:
        apply_solidworks_style()
    cams = cameras()
    SCENE.camera = cams[0]
    SCENE.frame_end = 15 * FPS
    SCENE.eevee.taa_render_samples = args.samples
    SCENE.render.resolution_percentage = args.percentage
    SCENE['CLIPS'] = '; '.join('%s:%ds' % item for item in CLIPS)
    SCENE['STYLE'] = args.style
    if args.mode == 'export-stl':
        export_stl()
        return
    if args.mode == 'build':
        save()
    if args.mode == 'proof':
        SCENE.camera = cams[2]
        for marker in SCENE.timeline_markers:
            marker.camera = None
        SCENE.frame_set(16)
        SCENE.render.filepath = str(ROOT / 'kinematic_proof.png')
        bpy.ops.render.render(write_still=True)
    elif args.mode == 'stills':
        render_stills(cams)
    elif args.mode == 'clip':
        configure_clip(args.clip, cams)
        folder = ROOT / ('verificacion' if args.preview_frames or args.still_frame is not None else 'renders')
        folder.mkdir(exist_ok=True)
        if args.still_frame is not None:
            SCENE.frame_set(int(args.still_frame), subframe=args.still_frame % 1)
            SCENE.render.filepath = str(folder / ('preview_still_%02d.png' % args.clip))
            bpy.ops.render.render(write_still=True)
            return
        if args.preview_frames:
            SCENE.frame_end = args.preview_frames
        if args.rgba_frames:
            out = Path(args.rgba_frames)
            out.mkdir(parents=True, exist_ok=True)
            SCENE.render.film_transparent = True
            SCENE.render.image_settings.file_format = 'PNG'
            SCENE.render.image_settings.color_mode = 'RGBA'
            SCENE.render.filepath = str(out / 'f_')
            bpy.ops.render.render(animation=True)
            return
        SCENE.render.image_settings.file_format = 'FFMPEG'
        SCENE.render.ffmpeg.format = 'MPEG4'
        SCENE.render.ffmpeg.codec = 'H264'
        SCENE.render.ffmpeg.constant_rate_factor = 'HIGH'
        SCENE.render.ffmpeg.ffmpeg_preset = 'GOOD'
        SCENE.render.filepath = str(folder / (('preview_clip_%02d' % args.clip if args.preview_frames else CLIPS[args.clip - 1][0]) + '.mp4'))
        bpy.ops.render.render(animation=True)

if __name__ == '__main__':
    main()









