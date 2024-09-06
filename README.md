# Bombsquad(2y)
My terminal font based on the Intellvision (I use the 2y version). Most glyphs were extracted from GROM using jzintv's `show_grom` utility.

This project can be used as a base for other 8x8 bitmap fonts that may be upscaled to 8x16 by modifying the bitmap files inside `src/`. Make sure the filenames each match an Unicode codepoint.

## To build
You need:
- ImageMagick
- FontForge
- Python 3

In a Linux (or WSL):
```sh
cd build
./remap.sh
./upscale.sh
./build.py
```
Check for .otf/.ttf/.zip files after running.

