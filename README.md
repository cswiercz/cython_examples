# Cython Examples

A collection of Cython examples, tests, and what not. Too many times
have I written a neat Cython code or technique only to find out
weeks-months later that I forgot how it's done.

## Running the Examples

To compile each example, navigate to the example directory and run:

```
$ cd example_subdirectory
$ python setup.py build_ext --inplace
```

Then, execute the corresponding `run.py` script:

```
$ python run.py
```

Evenually, I'll include a top-level setup script that will automatically
compile every example.)

## List of Examples

* `memoryview_pointers` - How to turn Cython memoryviews into C-pointers
  so they can be sent to C functions.

## Authors

* Chris Swierczewski (cswiercz)
