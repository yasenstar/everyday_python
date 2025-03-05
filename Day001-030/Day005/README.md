# Everyday Python - Day 005 - Handling Exceptions and Invalid Input

## Know `try...except` block

Today let's learn and familiar one useful Python statement `try...except...`, the basic idea is this: if you execute one or more statements in a `try...except` block and there's an error while executing, your program will not crash and print a `Traceback`. Instead, the execution is transferred to the `except` block, where you can perform an appropriate operation, e.g. printing a helpful error message or trying something else.

Picking some of similar conversion you practiced in previous day in a `try...except` block and print a helpful error message on invalid input:

```python
>>> try:
        a = float(input('Enter a number: '))
    except ValueError:
        print('Hey, my friend, you entered an invalid number')
```

Note 1: when you press `enter` key after `:`, you may notice the curcor is automatically indented to 4 characters to the right, keep that as the "indent" is crucial in Python syntax/grammer.

Note 2: after line `a = ...`, and press `Enter`, you then need to press `Backspace` key to make sure `except` is left-aligned with `try`, their two need to be at the same level, same reason as above Note 1.

Note 3: we need to specify the type of the exception we want to handle. Here we want to handle the `ValueError` exception, so we specify it as `except ValueError`, do not miss the `:` in the end.

Note 4: after the last line and you press `Enter`, you may see there're still three dots in the front of the line, you need to press `Enter` one more time to exit the `try...except` block mode.

Now, when you give an invalid input, such as `3/4` which is a fraction number, it prints a helpful error message, as shown at below:

```python
Enter a number: 3/4
Hey, my friend, you entered an invalid number
```

## Give User an Input Hint

To help user input correct information, you can also specify a prompt with the `input()` function to tell the user what kind of input is expected by your program. For instance as below:

```python
>>> a = input('Please input an integer: ')
```

The user will now see the message hinting to enter an integer (whole number) as input:

```python
Please input an integer: 1
```

Note: we normally add one space after the `:`, so that the prompt sentence have one space before user's input, this is not the syntax but just for pretty layout and more readibility.

## Take Care of Data Conversion

In many programs, we'll ask the user to enter a number as input, so we'll have to make sure we take care of conversion before we attempt to perform any (mathematical) opeations on these numbers.

You can combine the input and conversion in a single statement, as follows:

```python
>>> a = int(input())
1
>>> type(a)
<class 'int'>
>>> a + 1
2
```

## Handle User's Input Exception

Above data conversion together with input works perfectly if the user inputs an integer. But as we saw earlier, if the input is a floating point number (even one that's equivalent to an integer, like 1.0), this will produce an error, try below sample:

```python
a = int(input('Please input an integer: ))
1.0
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: '1.0'
```

In order to avoid this error, we could set up a `ValueError` catch like the one we saw earlier for fractions. That way the program would catch floating point numbers, which won't work in a program meant for integers. However, it would also flag numbers like `1.0` and `2.0`, which Python _sees_ as floating point numbers but that are equivalent to integers and would work just fine if they were entered as the right Python type.

To get around all these, we will use the `is_integer()` method to filter out any numbers with a significant digit after the decimal point. (Note: this method is only defined for `float` type numbers in Python; it won't work with numbers that are already entered in integer form, which you will see one `SyntaxError`, no worry on that.).

Try below example:

```python
>>> 1.1.is_integer()
False
>>> 105.is_integer()
<python-input-7>:1: SyntaxWarning: invalid decimal literal
  105.is_integer()
  File "<python-input-7>", line 1
    105.is_integer()
        ^^^^^^^^^^
SyntaxError: invalid syntax
```

Here, we call the method `is_integer()` to check if `1.1` is an integer, and the result is `False` because `1.1` really is a floating point number. On the other hand, when the method is called with `1.0`, `105.0` as the floating point number, the result is `True`, see below:

```python
>>> 1.0.is_integer()
True
>>> 105.0.is_integer()
True
```

Compare above two examples between `105` and `105.0`.

We can use `is_integer()` to filter out non-integer input while keeping input like `1.0` still, which is expressed as a floating point number but is equivalent to an integer.

---

WELL DONE! I know today's content may looks boring, but it's very important and useful for your later programming, enjoy and see you next day!

---

Source: Doing Math with Python, Chapter 1 "Getting User Input"