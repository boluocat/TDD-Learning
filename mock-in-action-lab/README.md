This lab us designed for you to get some hands on practice with using `unittest.mock`. This is a straightforward step-by-step lab whose purpose  is to get you to tie together the concepts you’ve learned about mocks by actually getting your hands dirty. 

Make sure to work through all of the questions and to take notes along the way.   

1) Create a mock object using unittest.mock called m1. 

Pre-configure it so that it has a method called run that returns 5. Here's some starter code to get the creative juices flowing:  
```python
>>> from unittest.mock import Mock 
>>> m1 = Mock() 
``` 
The only part left for you to fill in for question 1 is how do you preconfigure the mock to have a method called run which returns 5?  

2) Call m1 using the arguments of 1, 3, 5, 7, and 2, 4, 6. What is the result?  

3) Pass m1 into the dir() function. Look at the results and based off of the names, which one would you guess is used to verify how many  times run was called? Double check your hypothesis using the python documentation: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_count   

4) Update m1.run so that it has a new return value which is the following: [1, 2, 3]. 

Call the return_value attribute on run to do this.   

5) Have you configured m1.run to have a new value? If so, test it by calling m1.run()

6) Again, use dir(m1) to look up the functionality associated with the mock object. Which attribute can you use to track all of the calls you've  previously made? Double check your guess by using the unittest.mock module: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_count   

Call the following methods on m1: assert_called() and assert_called_once. 

What is the outcome, why is this the case?  

7) Go ahead and create a simple code snippet called function with the following details:  

```python
def function(a, b, c):
    return a + b + c  
```
How can we use mock to ensure that our mock objects fail in the same way that your production code does if used incorrectly. For example, if I have  a mock object titled m2, if I make the following calls an error will occur:   

>>> m1(1) 

>>> m1(5, 10)  

However, if you pass in the following then no error will generate:  

>>> m2(1, 2, 3)  <MagicMock name='mock()' id='57441920'>  

Read up about autospeccing from unittest.mock if you get stuck: https://docs.python.org/3/library/unittest.mock.html   