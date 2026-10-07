# DOT

A Python desktop tool for downloading playlist audio, suggesting cleaner filenames with Groq, and previewing tracks. It combines CustomTkinter, yt-dlp, FFmpeg, and Pygame in a music-library organization workflow.

## Use

With Python, Tk support, and an audio device available, run from the repository root in an activated virtual environment:

```sh
python -m pip install -r requirements.txt
python scripts/prepare_ffmpeg.py
```

Set `GROQ_API_KEY` in your environment or a local `.env` file, then launch:

```sh
python src/app.py
```

Paste a playlist URL and select Submit. Audio is saved under `downloads/`; the results view supports playback and manual renaming. Filename metadata is sent to Groq. Packaged builds are available on the [releases page](https://github.com/jatins02/DOT/releases).

## Status

Prototype: the current implementation prints the API key to the console and can process older files in `downloads/`. Rename collisions and partial failures need fixes. Use an empty output folder and disposable files; avoid shared logs until key logging is removed.
