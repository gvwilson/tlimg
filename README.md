# A Tiny Little Image Processing Pipeline

Python has several toolkits for manipulating image files.
My favorite is [Pillow](https://python-pillow.org/),
which is a derivative of an earlier library called PIL.
The [Pillow tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
will help you figure out how to load and manipulate images;
this lesson describes the handful you'll need right away.

> Note: you must install the library using `pip install Pillow` or `conda install Pillow`.
> Please see me if this doesn't work on your computer.
> If you are using Python 3, you'll need to use `pip3` instead of `pip`
> and `python3` instead of `python` in what follows. 

This folder contains four monochrome images called `sample_00.png` to `sample_03.png`.
Each one contains a single circular (ish) blot;
our goal is to write a program to find its center and radius.

Let's start by opening a file and looking at its properties:

```
from PIL import Image

picture = Image.open("sample_00.png")
print("format", picture.format)
print("size", picture.size)
print("mode", picture.mode)
```
```
format PNG
size (400, 400)
mode L
```

This tells us that we have a 400×400 PNG image.
The mode "L" means that it's a monochrome image
and that each pixel's gray-scale value is stored in a single byte.
This means that our color values run from 0 (for black) to 255 (for white).

If we want to get the color of a particular pixel we use the `getpixel` method:

```
position = (10, 10)
color = picture.getpixel(position)
print(f"color at {position}: {color}")
```
```
color at (10, 10): 26
```

These three lines introduce a couple of new ideas:

1.  We represent coordinates as *tuples* containing XY values.
    While lists are written with square brackets `[…]`,
    tuples are written with parentheses `(…)`.
    We index tuples the same way we index anything in Python: with square brackets.
    For example, if `location` is a variable with the value `(22, 33)`,
    then `location[0]` is 22 and `location[1]` is 33.

2.  We can format output using *f-strings* (and yes, the "f" means "format").
    If we put a lower-case 'f' immediately before a string,
    as in `f"…"`,
    and then put variables' names or other expressions inside curly braces `{…}` inside the string,
    Python converts the expression to text and puts it in the string for us.

So here's a plan for finding the center of the blob in each image:

1.  Write a program called `histogram.py` that takes the name of a file as input
    and prints a two-column table showing how many times each gray-scale value
    from 0 to 255 appears in the image.
    (We explain below how to give a filename on the command line
    so that you don't have to edit your program each time you want to process a different file.)

2.  Write a second program called `convert.py` that takes three command line values:
    the name of an input file,
    a threshold from 0 to 255,
    and the name of an output file.
    This program creates and saves a new image in which each pixel is either 0 or 255
    (i.e., pure black or pure white)
    depending on whether it is below or above the specified threshold.

3.  Write a third program called `center.py` that takes a pure black-and-white image
    produced by `center.py`
    and finds the center of the blob by calculating the average X and Y coordinates
    of the white pixels.

This is a big assignment,
so don't worry if you don't get through all of it for next week:
we'll look at what you've got and take it from there.

## Handling Command-Line Arguments

Take a look at this little program:

```
import sys

print(f"sys.argv is {sys.argv}")
```

Let's run it on the command line with no extra arguments:

```
$ python sys_argv.py
sys.argv is ['sys_argv.py']
```

Let's run it again with some arguments:

```
$ python sys_argv.py alpha beta gamma
sys.argv is ['sys_argv.py', 'alpha', 'beta', 'gamma']
```

What this shows us is that Python's `sys` module has a list called `sys.argv`
that stores all the values given on the command line
when the program was run.
The zero'th item in this list is the name of the program itself,
so if we want the first argument, it's `sys.argv[1]`.
All of these values are strings,
which means it's up to us to convert them to numbers.

For example,
here's some code you can use in `convert.py`:

```
import sys

assert len(sys.argv) == 4, "Usage: convert.py input_file split_value output_file"

input_file = sys.argv[1]
split_value = int(sys.argv[2])
output_file = sys.argv[3]
```
