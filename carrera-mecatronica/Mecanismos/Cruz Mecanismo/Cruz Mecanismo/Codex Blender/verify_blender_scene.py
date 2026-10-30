"""Independent checks of the saved scene; run with Blender --disable-autoexec."""
import json
import math
from pathlib import Path
import sys

import bpy
from mathutils.bvhtree import BVHTree

ROOT = Path(__file__).resolve().parent
scene = bpy.context.scene
driver = bpy.data.objects['DRIVER_60_RPM']
driven = bpy.data.objects['GENEVA_4_SLOT_INDEX']
pin = bpy.data.objects['Eccentric hardened pin']
wheel = bpy.data.objects['Geneva star - four open radial slots']
lock = bpy.data.objects['Circular dwell locking cam']
fps = scene.render.fps / scene.render.fps_base
rpm = scene.get('MOTOR_RPM', 60)
slots = scene.get('GENEVA_SLOTS', 4)
step = 2 * math.pi / slots
period = 60 / rpm
distance = (driven.location - driver.location).length
radius = distance * math.sin(math.pi / slots)
report = {'status': 'passed', 'rpm': rpm, 'slots': slots, 'checks': {}, 'errors': []}


def at_time(t):
    frame = 1 + t * fps
    integer = math.floor(frame)
    scene.frame_set(integer, subframe=frame - integer)
    bpy.context.view_layer.update()


def expected_output(t):
    cycles = t / period
    whole = math.floor(cycles)
    theta = 2 * math.pi * (cycles - whole - .5)
    alpha = math.pi / 2 - math.pi / slots
    if theta <= -alpha:
        return -whole * step
    if theta >= alpha:
        return -(whole + 1) * step
    return -whole * step - math.pi / slots - math.atan2(
        radius * math.sin(theta), distance - radius * math.cos(theta))


def check(name, condition, evidence):
    report['checks'][name] = evidence
    if not condition:
        report['errors'].append(name)


def world_bvh(obj):
    evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
    mesh = evaluated.to_mesh()
    verts = [evaluated.matrix_world @ v.co for v in mesh.vertices]
    faces = [tuple(poly.vertices) for poly in mesh.polygons]
    tree = BVHTree.FromPolygons(verts, faces)
    evaluated.to_mesh_clear()
    return tree


errors = []
input_errors = []
pin_errors = []
for i in range(4 * 120 + 1):
    t = i / 120
    at_time(t)
    errors.append(abs(driven.rotation_euler.z - expected_output(t)))
    input_errors.append(abs(driver.rotation_euler.z - 2 * math.pi * (t / period - .5)))
    if .375 <= (t / period) % 1 <= .625:
        delta = pin.matrix_world.translation - driven.matrix_world.translation
        ray = math.pi + math.pi / slots + driven.rotation_euler.z
        # Each revolution engages the next slot. Minimize across all slot rays.
        pin_errors.append(min(abs(delta.x * math.sin(ray + k * step)
                                  - delta.y * math.cos(ray + k * step))
                              for k in range(slots)))
check('output_matches_analytic_curve', max(errors) < 5e-6, {'max_rad_error': max(errors), 'samples': len(errors)})
check('input_is_exact_60rpm', max(input_errors) < 5e-6, {'max_rad_error': max(input_errors)})
check('pin_stays_in_slot_centerline', max(pin_errors) < 5e-6, {'max_distance_error': max(pin_errors)})
at_time(0)
origin = driven.rotation_euler.z
at_time(4 * period)
check('four_turns_equal_full_output_turn', abs(driven.rotation_euler.z - origin + 2 * math.pi) < 5e-6,
      {'output_degrees_after_four_turns': math.degrees(driven.rotation_euler.z - origin)})
for start, end in ((0, .37), (.63, 1)):
    at_time(start * period)
    a = driven.rotation_euler.z
    at_time(end * period)
    check(f'dwell_{start}_{end}', abs(driven.rotation_euler.z - a) < 1e-6,
          {'rotation_change_rad': driven.rotation_euler.z - a})

intersections = []
for i in range(121):
    t = i / 120
    at_time(t)
    star_tree = world_bvh(wheel)
    for other in (pin, lock):
        overlaps = star_tree.overlap(world_bvh(other))
        if overlaps:
            intersections.append({'t': t, 'object': other.name, 'surface_pairs': len(overlaps)})
check('no_pin_or_lock_surface_penetration', not intersections, {'intersections': intersections})
check('requested_collections', all(name in bpy.data.collections for name in (
    '01_GENEVA', '02_CONVEYOR', '03_STRUCTURE', '04_PRODUCTS', '05_FACTORY', '06_LIGHTS', '07_CAMERAS')),
    {'collections': list(bpy.data.collections.keys())})
if 'DRIVE_ROLLER' in bpy.data.objects:
    roller = bpy.data.objects['DRIVE_ROLLER']
    product = bpy.data.objects['PRODUCT_01_INDEXED']
    head = bpy.data.objects['DWELL_ONLY_INSPECTION_HEAD']
    roller_error, displacement_error, stroke_during_motion = [], [], []
    r = scene['ROLLER_RADIUS']
    at_time(0)
    initial_x = product.location.x
    for i in range(31):
        t = i / 30 * period
        at_time(t)
        roller_error.append(abs(roller.rotation_euler.y + driven.rotation_euler.z))
        displacement_error.append(abs((product.location.x - initial_x) + expected_output(t) * r))
        if .375 < t / period < .625:
            stroke_during_motion.append(abs(head.location.z - 2.67))
    check('roller_is_synchronized_1_to_1', max(roller_error) < 5e-6,
          {'max_error_rad': max(roller_error)})
    check('product_displacement_matches_roller_arc', max(displacement_error) < 5e-6,
          {'max_error_scene_units': max(displacement_error), 'pitch_scene_units': r * step})
    check('inspection_head_retracted_during_index', max(stroke_during_motion) < 5e-6,
          {'maximum_stroke_during_motion': max(stroke_during_motion)})
    check('ten_cameras', len(bpy.data.cameras) == 10, {'camera_count': len(bpy.data.cameras)})
    check('at_least_four_products', sum(o.name.startswith('PRODUCT_') for o in bpy.data.objects) >= 4,
          {'product_count': sum(o.name.startswith('PRODUCT_') for o in bpy.data.objects)})
report['resolution'] = [scene.render.resolution_x, scene.render.resolution_y]
report['fps'] = fps
report['note'] = 'Checks evaluated the reopened .blend with script auto-execution disabled.'
if report['errors']:
    report['status'] = 'failed'
out = ROOT / 'verificacion' / 'scene_report.json'
out.write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
if report['errors']:
    raise RuntimeError('Scene verification failed: ' + ', '.join(report['errors']))
if '--proof' in sys.argv:
    scene.frame_start, scene.frame_end = 1, 60
    scene.render.resolution_percentage = 50
    scene.eevee.taa_render_samples = 8
    scene.render.image_settings.file_format = 'FFMPEG'
    scene.render.ffmpeg.format = 'MPEG4'
    scene.render.ffmpeg.codec = 'H264'
    scene.render.ffmpeg.constant_rate_factor = 'MEDIUM'
    scene.render.ffmpeg.audio_codec = 'NONE'
    scene.render.filepath = str(ROOT / 'verificacion' / 'kinematic_motion_proof.mp4')
    bpy.ops.render.render(animation=True)
