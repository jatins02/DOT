import os
import shutil

import imageio_ffmpeg


def main():
    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ffmpeg_directory = os.path.join(project_directory, "ffmpeg")
    os.makedirs(ffmpeg_directory, exist_ok=True)

    source = imageio_ffmpeg.get_ffmpeg_exe()
    extension = ".exe" if os.name == "nt" else ""
    destination = os.path.join(ffmpeg_directory, f"ffmpeg{extension}")
    shutil.copy2(source, destination)

    if os.name != "nt":
        os.chmod(destination, 0o755)

    print(f"Prepared bundled FFmpeg at {destination}")


if __name__ == "__main__":
    main()