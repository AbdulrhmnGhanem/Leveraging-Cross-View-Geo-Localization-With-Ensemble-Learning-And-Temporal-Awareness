#!/bin/bash

# Compress all tiff files in a directory
# Usage: compress_tiff.bash <tiff_dir>
# Example: compress_tiff.bash figures
find $1 -maxdepth 1 -name "*.tiff" -execdir  convert {} -compress lzw {} \;