# Everyday Python - Day 004 - Getting User Input

When we talking about "User Input", normally it's saying input by keyboard, but there're many other ways, like motion capture, sensor capture, bar code scanner, etc., we here focus on "keyboard" first.

As we start to write programs, it will help to have a nice, simple way to accept user input via the function `input()`. That way we can write programs that ask a user to input a number, perform specific operations on that number, and then display the results of the operations.

Today, let's learn `input()`, still in command window, try below simple example (still using Terminal in your computer):

```python
>>> a = input()
1
```

At first line, we call the `input()` function, which waits on the screen for user (you) to type something, as shown in line two, try type `1` or any other characters, and press `Enter`. The input provided is stored in variable `a`:

```python
>>> a
'1'
```

Notice the single quotes around `1`. The `input()` function returns the input always as a _string_. In Python, a string is any set of characters between two quotes. When you want to create a string, either single quotes or double quotes can be used, like below example:

```python
>>> s1 = 'a string'
>>> s2 = "a string"
```

The above `s1` and `s2` are both referring to the same string.

__Even if the only characyters in a string are numbers, Python wont' treat that string as a number unless we get rid of those quotation marks.__ So before we can perform any mathematical operations with the input, we'll have to convert it into the correct number type. A string can be converted to an integer or floating point number using the `int()` or `float()` function, respectively, try below sample and see whether you can get the same results (notice the 2nd line gets an error message, try to understand that, the `"<python-input-1>"` may be different to your view, which is fine.):

```python
>>> a = '1'
>>> a + 1
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    a + 1
TypeError: can only concatenate str (not "int") to str
>>> print(a, type(a), int(a), type(int(a)))
1 <class 'str'> 1 <class 'int'>
>>> int(a) + 1
2
>>> float(a) + 1
2.0
```

These are the same `int()` and `float()` functions we saw earlier, but this time instead of converting the input from one kind of number to another, they taks a string as input ('1') and return a number (2 or 2.0). __It's important to note, however, that the `int()` function cannot convert a string containing a floating point decimal into an integer.__ If you take a string that has a floating point number (like '2.5' or even '2.0') and input that string into the `int()` function, you'll get an error message:

```python
>>> int('2.0')
Traceback (most recent call last):
  File "<pythong-input-3>", line 1, in <module>
    int('2.0')
ValueError: invalid literal for int() with base 10: '2.0'
```

Do not be afraid of Error Message, treat them as your friend during programming! Those are examples of the _exception_ -- Python's way of telling you that it cannot continue executing your program because of an error. In this recent caes, the exception is of the type `ValueError`.

Similarly, when you supply a fractional number such as `3/4` as an input, Python cannot convert it into an equivalent floating point number or integer. Once again, a `ValueError` exception is raised:

```python
>>> a = float(input())
3/4
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    a = float(input())
ValueError: cloud not convert string to float: '3/4'
>>>
```

When an exception if found, the program is stopped executing. You may find it useful to perform the conversion in a `try...except` block so that you can _handle_ the exception and alert the user that the program has encountered an invalid input.

Let's take rest and we'll look at `try...except` blocks in the next day.

---

Source: "Doing Math with Python"  Chapter 1 "Getting User Input"