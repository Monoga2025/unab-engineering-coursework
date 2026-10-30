# Geneva Conveyor - Blender Production

Open `GENEVA_CONVEYOR_PROJECT.blend` in Blender 4.2 LTS or later. The supplied
scene uses baked mathematical animation; enabling Python auto-execution is not
required to play it. The authoritative delivery checks are in `verificacion/`.

## Contents

- `geneva_conveyor_generator.py`: editable procedural geometry, animation, cameras,
  shot configuration, and rendering. Also embedded in the Blender Text Editor.
- `renders/`: ten H.264 MP4 clips, 1920 x 1080, 30 FPS; 122 seconds total.
- `capturas/`: seven named PNG captures at 1920 x 1080.
- `fuentes_originales/`: copies of the original CAD files, technical PDF, and AVI.
  `verificacion/source_manifest.json` records their matching SHA256 hashes.
- `pendientes/Daniel/` and `pendientes/Merchan/`: reserved for footage not supplied.
  None of the generated clips depends on these missing videos.
- `logs/`, `verificacion/`, `odd/tasks/`: render logs, checks, internal previews,
  and resumable work tracking. Internal previews are not final deliverables.

## Regenerate

Run these PowerShell commands from this directory:

```powershell
$blender = 'C:\Program Files\Blender Foundation\Blender 4.2\blender.exe'
& $blender -b --python-exit-code 1 --python .\geneva_conveyor_generator.py -- --mode build
& $blender -b --python-exit-code 1 --python .\geneva_conveyor_generator.py -- --mode stills
& $blender -b --python-exit-code 1 --python .\geneva_conveyor_generator.py -- --mode clip --clip 4
python .\render_all.py --resume --stills
python .\verify_deliverables.py --decode
```

`--mode build` replaces the generated master scene; save manual edits under a
different filename before regenerating. Rendering modes reconstruct their shots
from the generator, not from manual changes to the master. Use Blender's normal
Render controls to render manual edits. `render_all.py --resume` skips existing
clips only when their dimensions, frame rate, and frame count match the request.

## Motion model

The generator exposes `MOTOR_RPM = 60`, `GENEVA_SLOTS = 4`, and
`SIMULATION_SECONDS = 5`. The requested shot durations are defined separately in
`CLIPS`; they are not shortened to five seconds.

At the supplied settings, each input revolution takes one second and produces a
90-degree clockwise output index. Engagement occupies 0.375-0.625 seconds within
each cycle; the remaining 75% is dwell. Four input revolutions give one full
output revolution. Input/output curves are sampled at 120 Hz and saved in the
scene. Conveyor roller and carton travel derive from the same output angle.
The idealized 1:1 right-angle transmission is represented by shafts and a gearbox
housing; it is not a contact-dynamics simulation or a manufacturing design.

The inspection head operates during dwell. Cartons repeat behind end covers.
Clip 09 deliberately pauses the drive while components separate and reassemble.
Change source parameters and regenerate to update baked animation; editing scene
custom properties alone does not rebake it.

## Verification and sources

`verify_blender_scene.py` checks the reopened scene with script execution
disabled: analytic angle agreement, 360-degree cumulative output, dwell, pin/slot
alignment, pin/cam penetration, roller/carton synchronization, and cameras.
`verify_deliverables.py --decode` checks exact frame counts, frame rates,
dimensions, durations, and decodes every final video frame.

- Original technical reference: `fuentes_originales/Documento_Tecnico_Mecanismo_Ginebra.pdf`.
- [CMU: Geneva wheel mechanism](https://www.cs.cmu.edu/~rapidproto/mechanisms/chpt8.html).
- [Blender 4.2 command-line arguments](https://docs.blender.org/manual/en/4.2/advanced/command_line/arguments.html).
- [Blender 4.2 Eevee sampling](https://docs.blender.org/manual/en/4.2/render/eevee/render_settings/sampling.html).

The source CAD files are preserved as references; the Blender scene is newly
modeled procedural geometry, not a native SolidWorks assembly import. Original
engineering calculations are not a certification of the visualized machine.
