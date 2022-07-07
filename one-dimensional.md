# A One-Dimensional Warmup

Instead of tackling two-dimensional images, let's look at one-dimensional data: sound.
The simplest way to represent audio is as a sequence of intensity values.
Here's 40 samples from a signal with values in the range 0 to 15:

```python
signal = [
    13, 14, 11, 2,  6,  8,  0, 15,  8, 14,
     0,  4, 15, 7, 13,  0, 13, 12,  1,  6,
     7,  9,  1, 8,  3, 13,  8,  7,  9,  6,
    10,  9, 12, 1,  1, 12,  0,  5, 15,  4
]
```

It's straightforward to count how many values are zero:

```python
num_zero = 0
for value in signal:
    if value == 0:
        num_zero = num_zero + 1
print(num_zero)
```

What if we want to count how many are zero (lowest possible)
and at the same time count how many are 15 (highest possible)?

```python
num_zero = 0
num_max = 0
for value in signal:
    if value == 0:
        num_zero = num_zero + 1
    elif value == 15:
        num_max = num_max + 1
print("Number of 0:", num_zero)
print("Number of maximum value:", num_max)
```

But what if we want to count how many there are of each distinct value?
We could define sixteen variables `num_0`, `num_1`, ..., `num_15`
and have sixteen branches in our `if`-`elif` check,
but that's a lot of typing.
And if our next signal has values from 0 to 255 or even higher,
we pretty clearly need a different approach.

So let's do this:

1.  Create an array with sixteen elements,
    i.e., one element that corresponds to each of the 16 possible values
    in our signal.

2.  Fill that array with zeroes.

3.  Loop over the values in the signal.
    If the value is `v`,
    add 1 to the count in location `v` in the array.

We're going to use a trick to combine steps 1 and 2:

```python
example = ["hello"] * 3
print(example)
```

produces:

```
['hello', 'hello', 'hello']
```

Similarly, `[0] * 3` is `[0, 0, 0]`.
Our code is therefore:

```python
signal = [
    13, 14, 11, 2,  6,  8,  0, 15,  8, 14,
     0,  4, 15, 7, 13,  0, 13, 12,  1,  6,
     7,  9,  1, 8,  3, 13,  8,  7,  9,  6,
    10,  9, 12, 1,  1, 12,  0,  5, 15,  4
]
counts = [0] * 16 # 16 zeroes in an array
for value in signal:
    counts[value] = counts[value] + 1
print(counts)
```

which produces:

```
[4, 4, 1, 1, 2, 1, 3, 3, 4, 3, 1, 1, 3, 4, 2, 3]
```

## Exercises

1.  Suppose we want to find the first occurrence of each value in the signal.
    For example, the first occurrence of the value 13 is location 0,
    while the first occurrence of 0 is location 6.
    Modify the program shown above to find this instead of counting values.
    (Hint: you might want to start the array as `[None] * 16`
    so that you can tell when you're seeing a value for the first time.)

2.  Suppose we have two short samples like this:

    ```
    left = [13, 11, 6, 7, 13, 3, 15, 11, 4, 9]
    right = [8, 8, 10, 6, 5, 11, 1, 6, 13, 12]
    ```

    Write a program that blends these signals by taking alternate values from each.
    The output should be:

    ```
    [13, 8, 11, 8, ..., 4, 13, 9, 12]
    ```
