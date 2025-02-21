# Everyday Python - Day 003 - Install Python and Know Numbers

Today we learn how to handle fractions in Python.

## Create Fraction Numbers

Using fractions, we need to use Python's `fractions` module.

You can think of a `module` as a program written by someone else that you cna use in your own program. A module can include classes, functions, and even variable (label) definitions. (no worry, we'll learn `class`, `function` later on) It can be part of Python's standard library or distributed from a 3rd-party location. If in the latter case, you would have to install the module before you could use it. (using `pip install module-name` which we will practice later.)

Now, let's learn the `fractions` module, which is part of the standard Python library, meaning that it's already installed when you installed Python. It defines a class called `Fraction`, which is what we will use to enter fractions into our program.

Note: `fractions` is the module name, start from low case `f`; while `Fraction` is the class name, start from capital `F`, just remmeber that for now, the Class is inside module.

Before we can use the `fractions` module, we need to `import` it, which is a way of telling Python that we want to use the class from this module.

Let's practice below quick example -- we will create a new variable, `f`, which refers to the fraction `3/4`:

```python
>>> from fractions import Fraction
>>> f = Fraction(3, 4)
>>> f
Fraction(3, 4)
```

In above steps, we first import the `Fraction` class from the `fractions` module. Next, we create an object of this class (or called instance of the class) by passing the numerator and denominator as parameters. This creates a `Fraction` object for the fraction `3/4`. When we print (just type `f`) the object, Python displays the fraction in the form `Fraction(_numerator_, _denominator_)`.

Try yourself to create some more fractions as practice.

## Work with Fractions

The basic mathematical operations, including the comparison operations, are all valid for fractions.

You can also combine a fraction, an integer, and a floating point number in a single expression, try typing below sample (if you close and re-open the Terminal, you need `from fractions import Fraction` before you can use `Fraction`):

```python
>>> Fraction(3, 4) + 1 + 1.5
3.25
```

Try more expression with complex combination.

When you have a floating point number in an expression, the result of the expression is returned as a floating point number.

On the other hand, when you have only a fraction and an integer in the expression, the result is a fraction, even if the result has a denominator of `1`, test and think the result of below example:

```python
>>> Fraction(3, 4) + 1 + Fraction(1/4)
Fraction(2, 1)
```

Now you know the basics of working with fractions in Python.

---

Source: "Doing Math with Python" Chapter 1