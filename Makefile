# This file is part of Bombsquad.
#
# Bombsquad is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Bombsquad is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Bombsquad. If not, see <https://www.gnu.org/licenses/>.

SHELL := /bin/bash

all: upscale
	./build.py

.PHONY: upscale remap clean

upscale: build/upscaled/ \
	build/doubleheight/ \
	$(patsubst src/%.bmp,build/upscaled/%.bmp,$(wildcard src/*.bmp)) \
	$(patsubst src/%.bmp,build/doubleheight/%.bmp,$(wildcard src/*.bmp))

build/upscaled/:
	mkdir -p build/upscaled/

build/upscaled/%.bmp: src/%.bmp
	magick convert "$<" -monitor -sample "800x800" "$@"

build/doubleheight/:
	mkdir -p build/doubleheight/

build/doubleheight/%.bmp: src/%.bmp
	magick convert "$<" -monitor -sample "800x1600!" "$@"

remap:
	cd src; \
	for i in *.bmp; do \
		magick mogrify -monitor -define bmp:ignore-filesize=true -dither none -remap colortable.gif -colors 2 "$$i"; \
	done

clean:
	rm -rf build/*
