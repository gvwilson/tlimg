#!/usr/bin/env python

"""Generate some random blotch images."""

import math
import random
import sys
from PIL import Image, ImageFilter

WIDTH = 400
HEIGHT = 400
BACKGROUND = 50
PEAK = 255
SIZE = 0.1
BLUR = 3


def main():
    assert len(sys.argv) == 4, "Usage: generate stem num seed"
    stem = sys.argv[1]
    num = int(sys.argv[2])
    seed = int(sys.argv[3])

    random.seed(seed)

    for i in range(num):
        filename = f"{stem}_{i:02d}.png"
        img = make_image()
        img.save(filename)


def make_image():
    """Create a random image."""
    img = Image.new(mode="L", size=(WIDTH, HEIGHT))
    make_background(img)
    make_blot(img)
    img = img.filter(ImageFilter.GaussianBlur(radius = BLUR))
    return img


def make_background(img):
    """Fill background in image."""
    for x in range(img.width):
        for y in range(img.height):
            color = random.randint(0, BACKGROUND - 1)
            img.putpixel((x, y), color)


def make_blot(img):
    """Make a blot on an image."""
    radius = int(img.width * SIZE * (1 + random.uniform(-0.5, 0.5)))
    c_x = random.randint(int(0.4 * img.width), int(0.6 * img.width))
    c_y = random.randint(int(0.4 * img.height), int(0.6 * img.height))
    for x in range(c_x - radius, c_x + radius + 1):
        if (0 <= x < img.width):
            for y in range(c_y - radius, c_y + radius + 1):
                if (0 <= y < img.width) and (dist((x, y), (c_x, c_y)) <= radius):
                    color = random.randint(BACKGROUND, PEAK - 1)
                    img.putpixel((x, y), color)


def dist(p1, p2):
    """Return distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == "__main__":
    main()
