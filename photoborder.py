#! /usr/bin/env python3

import argparse
import os

from PIL import Image

parser = argparse.ArgumentParser(
    description="Adds a white border to an image.\n"
    "Saves result with a '-wb.jpg' suffix.\n"
    "Default values shown in parentheses.\n"
)

parser.add_argument(
    "-p",
    "--border_percent",
    help="Percentage of largest dimension to use as border width (%(default)s)",
    type=float,
    metavar="PERCENT",
    default=0.5
)

parser.add_argument(
    "-c",
    "--colour",
    help="Colour to be used for border (%(default)s)",
    metavar="PIL_COLOR_NAME",
    default="white"
)

parser.add_argument(
    "-s",
    "--show",
    help="Display output image (%(default)s)",
    action = "store_true",
    default=False
)

parser.add_argument('image', nargs='+', metavar="IMAGE")

args = parser.parse_args()

for f in args.image:

    im = Image.open(f)
    width, height = im.size

    border_size = int(max(width, height) * args.border_percent / 100)
    output = Image.new(im.mode, (width + 2 * border_size, height + 2 * border_size), args.colour)
    output.paste(im, (border_size, border_size))

    base, ext = os.path.splitext(f)
    output_file = base + "-wb" + ext
    print(output_file)
    output.save(output_file, quality=90)
    if args.show:
        output.show()
