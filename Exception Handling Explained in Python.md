In computer programming there are many enemies. They are the bugs, the errors, and the theater of the unexpected that can show its unpleasant self in our programs. This enemy is so formidable that it caused software engineers to develop practices to combat them. One strategy is called exception handling which detects anomalies that can occur when a program is run and then handles them gracefully. 

Exceptions respond to a wide array of occurrences such as a file not existing, the required memory not being available, or a user providing invalid input. The programmer can use exception handling to cause the program to terminate once the exception is triggered or they can use it so that the program continues.  

Exception handling works nicely with TDD to help make your software more fault tolerant. 

Let's take a look at some examples in python.

An Example of a Try Except Statement:
```python
try:
    pass
except Exception:
    pass
```

The only use for this above code snippet is to illustrate the syntax for try/except statements.

The try block contains the code that we want to try and execute. The except block contains the name of the Exception class. 

Note, try and except are reserved keywords in python so don’t use them as variable names. 

The except block will never be triggered if no errors occur within the try block like in the code snippet above. However, let’s say that hypothetically the exception block was triggered, then in that case the code within the except block will be executed which is where the exception is handled. In python lots of details of the trace back is revealed, and it’s typically a good idea not to expose too much sensitive info  in your program as this is more data that malicious users can utilize. 

There’s a lot of things that can cause an exception and the good news is that python has several built-in exception classes that you can check out here: 
https://docs.python.org/3/library/exceptions.html

In the code snippet, Exception is not a good class to use because it’s too general. The more specific you can make your Exception classes the better, it will also give more context to what our code is doing. Therefore it’s typically not a good idea to use a BaseClass like Exception, but instead use a Concrete Class. 

Let’s look at a less trivial example:
```python
try:
    with open('top_secret.csv', 'r+') as secret:
        for x in secret:
            print(x)
except FileNotFoundError:
    print('File is not here!')
```
The above code opens the file top_secret.csv for reading and writing with the intention of iterating over it and printing the contents. However, this file does not exist so the exception block will be triggered and the code will be processed here.

There’s also the finally/else statements that can be applied to exception handling in python. The finally block will always be executed regardless if the exception is triggered or not. Also, the else block can be used if you want code to be executed that’s not part of the exception. This is one way to keep exception logic isolated from business logic as mixing the two together could make the code difficult to maintain. 