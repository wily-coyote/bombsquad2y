all:
	./upscale.sh
	./build.py

remap:
	./remap.sh

.PHONY: clean
clean:
	rm -rf build/*
