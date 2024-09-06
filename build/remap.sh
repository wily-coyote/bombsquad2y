#!/usr/bin/env bash

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

for i in ../src/*.bmp; do magick mogrify -monitor -dither none -remap ../src/colortable.gif -colors 2 "$i"; done
