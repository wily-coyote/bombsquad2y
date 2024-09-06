#!/usr/bin/env python

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

import fontforge
import os
import zipfile

outputs = []

def makeFont(folder, name, output, width=1):
	print("{} -> {}".format(folder, output))
	font = fontforge.font()

	# I have absolutely no idea which one of these parameters removes the
	# 1px gap in WezTerm

	font.descent = 200
	font.ascent = 1400
	font.em = 1600
	assert font.ascent+font.descent==font.em, "em is not the sum of ascent + descent"

	font.fontname = name
	font.familyname = name
	font.fullname = name
	font.weight = "Regular"
	font.copyright = ""
	font.version = "001.000"

	font.os2_version = 4

	font.os2_use_typo_metrics = 1
	font.os2_typoascent = font.ascent
	font.os2_typoascent_add = 0
	font.os2_typodescent = -font.descent
	font.os2_typodescent_add = 0

	font.hhea_ascent = font.ascent
	font.hhea_ascent_add = 0
	font.hhea_descent = -font.descent
	font.hhea_descent_add = 0

	font.os2_winascent = font.ascent
	font.os2_winascent_add = 0
	font.os2_windescent = font.descent
	font.os2_windescent_add = 0

	font.os2_capheight = font.ascent
	font.os2_xheight = 1000

	font.os2_subxoff = 0
	font.os2_subyoff = 800
	font.os2_subxsize = 1600
	font.os2_subysize = 1600

	font.os2_supxoff = 0
	font.os2_supyoff = 800
	font.os2_supxsize = 1600
	font.os2_supysize = 1600

	font.os2_strikeypos = 700
	font.os2_strikeysize = 200

	font.os2_typolinegap = 0
	font.os2_panose = (0,0,0,9,0,0,0,0,0,0)
	font.vhea_linegap = 0
	font.hhea_linegap = 0

	font.upos = -100
	font.uwidth = 200

	font.encoding = "unicode"

	for k in font.layers:
		font.layers[k].is_quadratic = True

	for bmp in os.listdir(folder):
		print(bmp[3:7], end="\r")
		codepoint = int(bmp[3:7], 16)
		glyph = font.createChar(codepoint)
		glyph.manualHints = True
		glyph.importOutlines(folder+"/"+bmp)
		glyph.autoTrace()
		glyph.width = int(1600*width)

	for codepoint in [0x0020, 0x00A0]:
		print("%04x" % codepoint, end="\r")
		glyph = font.createChar(codepoint)
		glyph.manualHints = True
		glyph.width = int(1600*width)

	font.save(output)
	ttf = output.replace(".sfd", ".ttf")
	otf = output.replace(".sfd", ".otf")
	font.generate(ttf)
	font.generate(otf)
	outputs.append(ttf)
	outputs.append(otf)
	font.close()

makeFont("upscaled", "Bombsquad", "Bombsquad.sfd")
makeFont("doubleheight", "Bombsquad-2y", "Bombsquad-2y.sfd", width=0.5)

archive = zipfile.ZipFile("Bombsquad.zip", mode="w", compression=zipfile.ZIP_DEFLATED)
for i in outputs:
	os.chmod(i, 0o777)
	archive.write(i, i)
archive.close()
