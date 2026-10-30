"""Verify the requested delivery, without importing Blender or changing media."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import struct
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CLIPS = {
    "01_MODELO_GENERAL.mp4": 12,
    "02_GINEBRA_CLOSEUP.mp4": 15,
    "03_GINEBRA_TOP.mp4": 12,
    "04_60RPM_TIMELINE.mp4": 6,
    "05_INDEXACION_90_GRADOS.mp4": 12,
    "06_BANDA_FUNCIONANDO.mp4": 15,
    "07_AMBIENTACION_FABRICA.mp4": 15,
    "08_MECANISMO_AISLADO.mp4": 10,
    "09_COMPONENTES.mp4": 10,
    "10_FINAL_CINEMATIC.mp4": 15,
}
STILLS = [
    "01_general.png", "02_geneva_pin_entry.png", "03_geneva_moving.png",
    "04_geneva_rest.png", "05_conveyor.png", "06_60rpm.png", "07_top_view.png",
]


def verify(decode: bool = False) -> dict:
    """Require exact frame counts/rate, dimensions, and a readable Blender header."""
    report = {"status": "passed", "files": [], "errors": []}
    ffprobe = shutil.which("ffprobe")
    ffmpeg = shutil.which("ffmpeg")
    for name, seconds in CLIPS.items():
        path = ROOT / "renders" / name
        record = {"file": str(path.relative_to(ROOT)), "expected_seconds": seconds}
        try:
            if not path.is_file():
                raise ValueError("missing")
            if not ffprobe:
                raise ValueError("ffprobe is unavailable")
            result = subprocess.run([
                ffprobe, "-v", "error", "-select_streams", "v:0",
                "-show_entries", "stream=width,height,r_frame_rate,avg_frame_rate,nb_frames,duration,codec_name,pix_fmt",
                "-of", "json", str(path),
            ], capture_output=True, text=True, check=True)
            stream = json.loads(result.stdout)["streams"][0]
            record.update(stream)
            if (stream["width"], stream["height"]) != (1920, 1080):
                raise ValueError("resolution is not 1920x1080")
            if stream["r_frame_rate"] != "30/1" or stream["avg_frame_rate"] != "30/1":
                raise ValueError("frame rate is not constant 30 FPS")
            if int(stream["nb_frames"]) != seconds * 30:
                raise ValueError("incorrect frame count")
            if abs(float(stream["duration"]) - seconds) > 0.002:
                raise ValueError("incorrect duration")
            if stream["codec_name"] != "h264":
                raise ValueError("MP4 is not encoded with H.264")
            if decode:
                if not ffmpeg:
                    raise ValueError("ffmpeg is unavailable for decode check")
                result = subprocess.run([
                    ffmpeg, "-v", "error", "-xerror", "-i", str(path),
                    "-map", "0:v:0", "-f", "null", "-",
                ], capture_output=True, text=True, check=True)
                if result.stderr.strip():
                    raise ValueError(result.stderr.strip())
                record["full_decode"] = "passed"
            record["status"] = "passed"
        except (ValueError, KeyError, IndexError, OSError, subprocess.SubprocessError) as error:
            record["status"] = "failed"
            report["errors"].append(f"{name}: {error}")
        report["files"].append(record)
    for name in STILLS:
        path = ROOT / "capturas" / name
        record = {"file": str(path.relative_to(ROOT))}
        try:
            with path.open("rb") as handle:
                header = handle.read(24)
            if header[:8] != b"\x89PNG\r\n\x1a\n":
                raise ValueError("not a PNG")
            width, height = struct.unpack(">II", header[16:24])
            record.update(width=width, height=height)
            if (width, height) != (1920, 1080):
                raise ValueError("resolution is not 1920x1080")
            record["status"] = "passed"
        except (ValueError, OSError, struct.error) as error:
            record["status"] = "failed"
            report["errors"].append(f"{name}: {error}")
        report["files"].append(record)
    for name in ("GENEVA_CONVEYOR_PROJECT.blend", "geneva_conveyor_generator.py"):
        path = ROOT / name
        if not path.is_file() or not path.stat().st_size:
            report["errors"].append(f"{name}: missing or empty")
    if report["errors"]:
        report["status"] = "failed"
    report["expected_video_frames"] = sum(CLIPS.values()) * 30
    report["expected_total_seconds"] = sum(CLIPS.values())
    report["note"] = "Media integrity does not replace visual/kinematic inspection."
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decode", action="store_true", help="Decode every video frame.")
    args = parser.parse_args()
    result = verify(args.decode)
    target = ROOT / "verificacion" / "delivery_report.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0 if result["status"] == "passed" else 1)
