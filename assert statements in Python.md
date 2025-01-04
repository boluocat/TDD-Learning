## How to create assert statements in Python

The general syntax for applying assert statements is :

`assert condition_one, condition_two, ..., condition_n`

One way to get the hang of assert statements is to open up the python REPL and then start typing in commands as shown below: 

```python
>>> y = 5
>>> assert y > 3
>>> assert y < 10
>>> assert y != -1
```

Notice how there’s no output in the above code snippets? Now, let’s add the following code snippet to the python REPL:

```
>>> z = 100
>>> assert z < 100
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

Wait one sec! In this case our program terminated and we have an error message that says **AssertionError**. The reason this error propagated is because of the following:

The assert statement serves as a debugging tool because it allows us to easily pinpoint where something went wrong. You can also test multiple conditions as shown in the following pseudocode:

```python
 assert statement_one, statement_two, …, statement_n
```

A concrete example of this in action is indicated below: 

```python
>>> x = 3
>>> assert x == 3 and x > 0 and x <= 3
```

In the above example we’re applying the assert statement to multiple conditional statements. Therefore, if any of the above conditions evaluates to False then it will raise an AssertionError. 

## **Adding a Custom Error Message**

You could also add a default error message if your assert statement evaluates to False as indicated in the following pseudocode: 

```python
assert condition, False
```

Below is a concrete example of how to apply a custom error message to an assert statement: 

```

>>> x = int(input('Enter in integer 1 '))
Enter in integer 1 10
>>> y = int(input('Enter in integer 2 '))
Enter in integer 2 0
>>> assert 0 < x <= 100, "x is less than 0, or x is greater than 100"
>>> assert 0 < y <= 100, "y is less than 0, or y is greater than 100"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: y is less than 0, or y is greater than 100
```

## **Using an Assert Statement to Verify Function Output**

Assert statements can also be used to test if a function returns the expected value. An example of how to use an assert statement in this context is shown below: 

```python
def create_list(n=10):
  
    x = []
  
    for y in range(n):
  
        x.append(y)
  
return x


>>> assert len(create_list()) == 10
>>> y = 1000
>>> assert len(create_list(1000)) == 1000

```

In the above code snippet we have a function called create_list that creates an empty list in x, appends values to x, and then returns x. The function create_list has a keyword parameter of n=10. Therefore, we can assume that if we called the function using the default parameter, then the length should be 10. We verified this with the following statement which is why no error occurred:

```python
>>> assert len(create_list()) == 10
```

We can also overwrite the keyword argument to test if the function still returns no errors as shown in the following code snippet:

```python
>>> y = 1000
>>> assert len(create_list(1000)) == 1000
```

 Again, no errors. Modify this code so that an AssertionError occurs before moving on. 

## **How to Turn Assertions Off** 

 You can also run your python scripts so that the assert statements are ignored. The below one liner is put in python file called test.py:

```python
assert False, "this is an error!"
```

If you run test.py from the command line/terminal, then this will be the output:

```
Traceback (most recent call last):
  
  File "test.py", line 5, in <module>
  
    assert False, "this is an error!"
  
AssertionError: this is an error!
```

However, re-run test.py with the following command line arguments:

```
python -O test.py
```

What you should notice is that nothing happened, because the assert statements are ignored due to the -O flag. 

## **When to Apply Assert Statements?**

Now that we know how to use assert statements what are some scenarios in which we’ll apply them? Below is a bulleted list which contains tips on when and when not to apply assert statements in your programs:

- Use assert statements as debugging tools
- Use assert statements to fail fast so you can quickly pinpoint issues
- Use assertions to verify that function output is expected 
- Don’t use assert statements to catch errors 
- Don’t use assert statements to validate data. 

To read up more about assert statements in python view the python docs: https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assert-stmt