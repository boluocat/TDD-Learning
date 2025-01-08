from unittest.mock import Mock
from unittest.mock import create_autospec

m1 = Mock()

# Question 1
# preconfigure m1 so it has a method called 'run'
# preconfigure m1 so it returns 5
attributes = {'run.return_value': 5}
m1 = Mock(**attributes)
print(m1.run())

# Question 2
# call m1.run() with 1, 3, 5, 7
attributes = {'run.return_value':1}
m1 = Mock(**attributes)
print(m1.run())
attributes = {'run.return_value':3}
m1 = Mock(**attributes)
print(m1.run())
attributes = {'run.return_value':5}
m1 = Mock(**attributes)
print(m1.run())
attributes = {'run.return_value':7}
m1 = Mock(**attributes)
print(m1.run())
# call m1.run () with 2, 4, 6
attributes = {'run.return_value':2}
m1 = Mock(**attributes)
print(m1.run())
attributes = {'run.return_value':4}
m1 = Mock(**attributes)
print(m1.run())
attributes = {'run.return_value':6}
m1 = Mock(**attributes)
print(m1.run())

# What's the results?

# Question 3
# pass m1 to the dir() function.
print(dir(m1))
# which attribute verifies how many times m1 is called?
times = m1.call_count
print(times)

# Question 4
# update m1.run() so it now returns [1, 2, 3]
# use return_value attribute for this
attributes = {'run.return_value':[1, 2, 3]}

# Question 5
# Test that you re-configured m1 correctly. Call m1.run()
m1 = Mock(**attributes)
print(m1.run())

# Question 6
# Use dir(m1) to see teh functionality of the mock object again
print(dir(m1))
# call assert_called and assert_called_once
print(m1.run.assert_called())
print(m1.run.assert_called_once())
# What's the output? Keep notes of this

# Question 7

# Create a simple function with the following details:

def function(a, b, c):
    return a + b + c  

m1 = Mock()
m1.adder = function
print(m1.adder(1,2,3))
print(m1.adder(1,2))

# Use unittest.mock to ensure that the mock object is called correctly
# I.e, the following should product an error
# >>> m1(1)
# >>> m1(5, 10)
# The following should NOT
# >>> m1(1, 2, 3)
# If stuck, read: https://docs.python.org/3/library/unittest.mock.html 
