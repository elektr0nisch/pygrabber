# PyGrabber

Open-source CLI tools for downloading (grabbing, ripping) online media content.

## Supported services

- HTML5 embedded `<video>` and `<audio>` elements
- YouTube
- MediathekView (German public broadcast)

## Planned services

- Vimeo

## Requirements

- Python >= 3.9

## Example

```bash

# Downloading a single file
python pygrabber.py -i https://www.youtube.com/watch?v=dQw4w9WgXcQ -o target/

# Downloading multiple files
python pygrabber.py -i https://www.youtube.com/watch?v=dQw4w9WgXcQ https://www.ardmediathek.de/video/feuer-und-flamme/folge-6-explosion-bei-brand-s06-e06/wdr/Y3JpZDovL3dkci5kZS9CZWl0cmFnLTkzOTEwMGM4LWNkZTUtNDA3Yi05NmNhLTVkZjBkZDExN2RjNw -o target/

```
