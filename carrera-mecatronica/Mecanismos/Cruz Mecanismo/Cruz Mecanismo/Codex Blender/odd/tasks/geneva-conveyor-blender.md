# Geneva Conveyor Blender Production

## Objective
Create an editable Blender scene and generator script for an industrial four-slot Geneva indexer driving a conveyor, then produce the requested ten MP4 clips and seven PNG captures in `Codex Blender/`.

## Problem and Why
The user needs an engineering-pitch-ready visualization demonstrating synchronized 60 RPM continuous input, intermittent 90-degree Geneva indexing, and conveyor motion. They do not yet have Daniel's or Merchan's videos; keep the work organized without depending on those assets.

## Scope and Constraints
- Work only in `Codex Blender/`; copy source assets there and do not modify the originals.
- Blender project: `GENEVA_CONVEYOR_PROJECT.blend`; editable Python generator: `geneva_conveyor_generator.py`.
- 10 named 1920x1080, 30 FPS MP4 deliverables and 7 named 1920x1080 PNG captures.
- Keep outputs in `renders/` and `capturas/`, collections as requested.
- Use Blender 4.2 if available; prioritize stable, synchronized Geneva kinematics and Eevee speed.
- Never invent Daniel/Merchan source clips; leave their eventual integration organized as pending inputs.
- Existing repository has unrelated dirty files; do not touch them. Git root is above the writable workspace and `.git` is read-only here; commits/branch work may be unavailable.
- TDD: no project test runner/config discovered yet; resolve by running Blender background generation/sanity checks as the functional validation.

## Route and Trigger
- Route: delegated direct for exploration and the Blender generator writer; parent handles source copying, independent verification, and rendering orchestration.
- Trigger evidence: mapping required the source assets, Blender availability, and rendering constraints across multiple files. Source asset mapping delegated read-only before implementation.

## Tasks
- [x] T01 — Map source assets and Blender/render environment; copy originals into `Codex Blender/`.
- [x] T02 — Implement and verify the Geneva kinematic core and generator script with a short animation check.
- [x] T03 — Build the full editable conveyor/factory scene, collections, cameras, and save `.blend`.
- [ ] T04 — Render the ten requested clips and seven stills; verify files, dimensions, frame rates, and durations. (in progress: stills done, clips rendering)

## Acceptance Criteria
- Driver rotates at 60 RPM (one revolution per second); Geneva output advances 90 degrees per revolution with physically plausible dwell/engagement/acceleration/deceleration.
- Conveyor and products visibly index and stop in sync; industrial station and clean premium setting are present.
- Blender project opens, with clearly named collections/cameras/materials and editable script/config variables.
- All requested MP4 and PNG files exist with specified dimensions/rate/clip durations; no missing Daniel/Merchan media is fabricated.

## Checks and Progress
- Checks: Blender background script generation; short kinematics render before full build; inspect still render; verify media metadata and required filenames.
- TDD mode source: project guidance indicates no automated test framework; runner: Blender 4.2 background executable.
- Forecast: several hundred lines across generator and this task document; render output excluded from authored-line estimate.
- Delivery strategy: ask-on-risk (default); Git work-unit commit feasibility pending because the repository root and `.git` are outside the writable scope.
- T01 evidence: Blender 4.2.16 LTS background probe passed. Six original files copied into `fuentes_originales/`; SHA256 matches all six originals (`verificacion/source_manifest.json`). Daniel/Merchan folders remain empty under `pendientes/`. DriveInfo confirms 144 GB free; earlier PowerShell PSDrive zero was not an actual capacity reading.
- Commits: unavailable within current writable scope; no unrelated repository changes touched.
- TDD: explicit on/off configuration not established; do not claim TDD. Use deterministic analytic and runtime acceptance checks.
- T02/T03 generator implementation delegated to `build_blender_generator`; parent verifies independently.
- T02 evidence: initial `.blend` and generator saved. Independent `verify_blender_scene.py` reopened the saved file with script auto-execution disabled: 481 temporal samples match analytic input/output motion; four revolutions produce -360.00001 degrees; dwell motion is zero; 121 phases have no pin/locking-cam surface penetration. A 2-second, 60-frame internal proof MP4 rendered and contact sheet visually inspected (`verificacion/kinematic_motion_proof.mp4`, `scene_report.json`). This preview is 960x540; requested final deliverables remain 1920x1080.
- RDD status command failed resolving ancestor repository identity (access denied); no review performed or approval claimed. Source SHA256 checks passed.
- T03 evidence: `GENEVA_CONVEYOR_PROJECT.blend` saved with named collections, cameras, and materials; seven 1920x1080 PNG captures rendered into `capturas/`; scene/core verification logs in `logs/`.
- T04 progress: full render at 32 Eevee samples measured ~10 s/frame (about 10 h for 3660 frames) and was rejected as impractical; re-run at 8 samples (~2.5 s/frame). Clip 01 completed in 977 s and was resume-verified. Render queue relaunched detached via `render_all.py --resume --samples 8`; remaining nine clips estimated ~1.5-2 h.
- Next step: let the detached queue finish, then run `python verify_deliverables.py --decode` to confirm all ten MP4 (1920x1080, 30 FPS, exact durations) and seven PNG, and refresh `verificacion/delivery_report.json`.
