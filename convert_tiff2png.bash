#!/bin/bash
# Convert all tiff files in a directory to png files into a new directory
# Usage: convert_tiff2png.bash <tiff_dir> <png_dir>
# Example: convert_tiff2png.bash convert_tiff2png.bash figures png
find $1 -name "*.tiff" -execdir convert {} $2/$(basename {}).png \;
# find $1 -name "*.tiff" -exec basename \{} \;
