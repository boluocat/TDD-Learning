# What is `pylint`
`pylint` is a package to check code conforms to PEP 8. 
Pylint checkers can provide three set of features:
- options that control their execution,
- messages that they can raise,
- reports that they can generate.

It has a range of useful features for test driven development and programming in general such as:
- Refactoring help
- UML diagram
- Checks line code length
- Checks if variable names are well formed
- Checks if imported modules are used
View all of the features of `Pylint` here: https://pylint.readthedocs.io/en/latest/technical_reference/features.html
View all of the configuration pf `pylint` here: https://pylint.readthedocs.io/en/latest/user_guide/configuration/all-options.html# 

# What is PEP 8
PEP 8 is a set of recommendations for styling code in Python.

# Install pylint
`pylint` is a third party package of Python. To use it, you need to install it beforehand.
```shell
pip install pylint
```

# Using pylint to check `.py` formate
```shell
python -m pylint /path/file.py
```

There are also a few kinds of format can be used to output.
 - test
 - parseable
 - colorized (error will colorized light)
 - json2 (improved json format)
 - json
 - msvs (visual studio)

Example for colorizing result
```shell
python311 -m  pylint .\test_create_table_in_db.py --output-format colorized
************* Module test_create_table_in_db
test_create_table_in_db.py:45:8: W0107: Unnecessary pass statement (unnecessary-pass)
```

Example for json2 file output
```shell
python311 -m  pylint .\test_create_table_in_db.py --output-format=json2 >pylint_report_for_test_db.json
```

```json2
{
    "messages": [
        {
            "type": "warning",
            "symbol": "unnecessary-pass",
            "message": "Unnecessary pass statement",
            "messageId": "W0107",
            "confidence": "UNDEFINED",
            "module": "test_create_table_in_db",
            "obj": "TestDatabase.tearDown",
            "line": 45,
            "column": 8,
            "endLine": 45,
            "endColumn": 12,
            "path": "test_create_table_in_db.py",
            "absolutePath": "E:\\git\\TDD-Learning\\test_create_table_in_db.py"
        }
    ],
    "statistics": {
        "messageTypeCount": {
            "fatal": 0,
            "error": 0,
            "warning": 1,
            "refactor": 0,
            "convention": 0,
            "info": 0
        },
        "modulesLinted": 3,
        "score": 9.47
    }
}
```



# Example for using `pylint`

## The original code is here:

```python
'''
Using Mocking to test the create_table_in_db function
'''

import unittest
from unittest.mock import MagicMock

CONTENT = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )'''
        
# Function to be tested
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(CONTENT)
    conn.commit()

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Set up the mock database connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

    def test_table_creation(self):
        """Test if a table creation query is executed"""
        create_table(self.mock_conn)
        
        # Verify that the correct SQL query was executed
        self.mock_cursor.execute.assert_called_with(CONTENT)

    def tearDown(self):
        """Clean up"""
        pass

if __name__ == '__main__':
    unittest.main()
```


## Using `pylint` to check if code conforms to PEP 8:
```shell
python311 -m pylint .\test_create_table_in_db.py
```
The report is here:
```text
test_create_table_in_db.py:14:0: C0303: Trailing whitespace (trailing-whitespace)
test_create_table_in_db.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
test_create_table_in_db.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
test_create_table_in_db.py:21:0: C0115: Missing class docstring (missing-class-docstring)
test_create_table_in_db.py:38:8: W0107: Unnecessary pass statement (unnecessary-pass)

------------------------------------------------------------------
Your code has been rated at 7.37/10 (previous run: 7.37/10, +0.00)

```
And you can modify your code based on this.

# Using `pydoc` to create a pydoc:
```shell
python311 -m pydoc .\test_create_table_in_db.py
```

The Python document is following here:
```TEXT
NAME
    test_create_table_in_db - Using Mocking to test the create_table_in_db function

CLASSES
    unittest.case.TestCase(builtins.object)
        TestDatabase
    
    class TestDatabase(unittest.case.TestCase)
     |  TestDatabase(methodName='runTest')
     |  
     |  This class is used to test the create_table function
     |  
     |  Method resolution order:
     |      TestDatabase
     |      unittest.case.TestCase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  setUp(self)
     |      Set up the mock database connection
     |  
     |  tearDown(self)
     |      Clean up
     |  
     |  test_table_creation(self)
     |      Test if a table creation query is executed
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from unittest.case.TestCase:
     |
     |  __call__(self, *args, **kwds)
     |      Call self as a function.
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __hash__(self)
     |      Return hash(self).
     |
     |  __init__(self, methodName='runTest')
     |      Create an instance of the class that will use the named test
     |      method when executed. Raises a ValueError if the instance does
     |      not have a method with the specified name.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__(self)
     |      Return str(self).
     |
     |  addCleanup(self, function, /, *args, **kwargs)
     |      Add a function, with arguments, to be called when the test is
     |      completed. Functions added are called on a LIFO basis and are
     |      called after tearDown on test failure or success.
     |
     |      Cleanup items are called even if setUp fails (unlike tearDown).
     |
     |  addTypeEqualityFunc(self, typeobj, function)
     |      Add a type specific assertEqual style function to compare a type.
     |
     |      This method is for use by TestCase subclasses that need to register
     |      their own type equality functions to provide nicer error messages.
     |
     |      Args:
     |          typeobj: The data type to call this function on when both values
     |                  are of the same type in assertEqual().
     |          function: The callable taking two arguments and an optional
     |                  msg= argument that raises self.failureException with a
     |                  useful error message when the two arguments are not equal.
     |
     |  assertAlmostEqual(self, first, second, places=None, msg=None, delta=None)
     |      Fail if the two objects are unequal as determined by their
     |      difference rounded to the given number of decimal places
     |      (default 7) and comparing to zero, or by comparing that the
     |      difference between the two objects is more than the given
     |      delta.
     |
     |      Note that decimal places (from zero) are usually not the same
     |      as significant digits (measured from the most significant digit).
     |
     |      If the two objects compare equal then they will automatically
     |      compare almost equal.
     |
     |  assertAlmostEquals = deprecated_func(*args, **kwargs)
     |
     |  assertCountEqual(self, first, second, msg=None)
     |      Asserts that two iterables have the same elements, the same number of
     |      times, without regard to order.
     |
     |          self.assertEqual(Counter(list(first)),
     |                           Counter(list(second)))
     |
     |       Example:
     |          - [0, 1, 1] and [1, 0, 1] compare equal.
     |          - [0, 0, 1] and [0, 1] compare unequal.
     |
     |  assertDictContainsSubset(self, subset, dictionary, msg=None)
     |      Checks whether dictionary is a superset of subset.
     |
     |  assertDictEqual(self, d1, d2, msg=None)
     |
     |  assertEqual(self, first, second, msg=None)
     |      Fail if the two objects are unequal as determined by the '=='
     |      operator.
     |
     |  assertEquals = deprecated_func(*args, **kwargs)
     |
     |  assertFalse(self, expr, msg=None)
     |      Check that the expression is false.
     |
     |  assertGreater(self, a, b, msg=None)
     |      Just like self.assertTrue(a > b), but with a nicer default message.
     |
     |  assertGreaterEqual(self, a, b, msg=None)
     |      Just like self.assertTrue(a >= b), but with a nicer default message.
     |
     |  assertIn(self, member, container, msg=None)
     |      Just like self.assertTrue(a in b), but with a nicer default message.
     |
     |  assertIs(self, expr1, expr2, msg=None)
     |      Just like self.assertTrue(a is b), but with a nicer default message.
     |
     |  assertIsInstance(self, obj, cls, msg=None)
     |      Same as self.assertTrue(isinstance(obj, cls)), with a nicer
     |      default message.
     |
     |  assertIsNone(self, obj, msg=None)
     |      Same as self.assertTrue(obj is None), with a nicer default message.
     |
     |  assertIsNot(self, expr1, expr2, msg=None)
     |      Just like self.assertTrue(a is not b), but with a nicer default message.
     |
     |  assertIsNotNone(self, obj, msg=None)
     |      Included for symmetry with assertIsNone.
     |
     |  assertLess(self, a, b, msg=None)
     |      Just like self.assertTrue(a < b), but with a nicer default message.
     |
     |  assertLessEqual(self, a, b, msg=None)
     |      Just like self.assertTrue(a <= b), but with a nicer default message.
     |
     |  assertListEqual(self, list1, list2, msg=None)
     |      A list-specific equality assertion.
     |
     |      Args:
     |          list1: The first list to compare.
     |          list2: The second list to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |
     |  assertLogs(self, logger=None, level=None)
     |      Fail unless a log message of level *level* or higher is emitted
     |      on *logger_name* or its children.  If omitted, *level* defaults to
     |      INFO and *logger* defaults to the root logger.
     |
     |      This method must be used as a context manager, and will yield
     |      a recording object with two attributes: `output` and `records`.
     |      At the end of the context manager, the `output` attribute will
     |      be a list of the matching formatted log messages and the
     |      `records` attribute will be a list of the corresponding LogRecord
     |      objects.
     |
     |      Example::
     |
     |          with self.assertLogs('foo', level='INFO') as cm:
     |              logging.getLogger('foo').info('first message')
     |              logging.getLogger('foo.bar').error('second message')
     |          self.assertEqual(cm.output, ['INFO:foo:first message',
     |                                       'ERROR:foo.bar:second message'])
     |
     |  assertMultiLineEqual(self, first, second, msg=None)
     |      Assert that two multi-line strings are equal.
     |
     |  assertNoLogs(self, logger=None, level=None)
     |      Fail unless no log messages of level *level* or higher are emitted
     |      on *logger_name* or its children.
     |
     |      This method must be used as a context manager.
     |
     |  assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None)
     |      Fail if the two objects are equal as determined by their
     |      difference rounded to the given number of decimal places
     |      (default 7) and comparing to zero, or by comparing that the
     |      difference between the two objects is less than the given delta.
     |
     |      Note that decimal places (from zero) are usually not the same
     |      as significant digits (measured from the most significant digit).
     |
     |      Objects that are equal automatically fail.
     |
     |  assertNotAlmostEquals = deprecated_func(*args, **kwargs)
     |
     |  assertNotEqual(self, first, second, msg=None)
     |      Fail if the two objects are equal as determined by the '!='
     |      operator.
     |
     |  assertNotEquals = deprecated_func(*args, **kwargs)
     |
     |  assertNotIn(self, member, container, msg=None)
     |      Just like self.assertTrue(a not in b), but with a nicer default message.
     |
     |  assertNotIsInstance(self, obj, cls, msg=None)
     |      Included for symmetry with assertIsInstance.
     |
     |  assertNotRegex(self, text, unexpected_regex, msg=None)
     |      Fail the test if the text matches the regular expression.
     |
     |  assertNotRegexpMatches = deprecated_func(*args, **kwargs)
     |
     |  assertRaises(self, expected_exception, *args, **kwargs)
     |      Fail unless an exception of class expected_exception is raised
     |      by the callable when invoked with specified positional and
     |      keyword arguments. If a different type of exception is
     |      raised, it will not be caught, and the test case will be
     |      deemed to have suffered an error, exactly as for an
     |      unexpected exception.
     |
     |      If called with the callable and arguments omitted, will return a
     |      context object used like this::
     |
     |           with self.assertRaises(SomeException):
     |               do_something()
     |
     |      An optional keyword argument 'msg' can be provided when assertRaises
     |      is used as a context object.
     |
     |      The context manager keeps a reference to the exception as
     |      the 'exception' attribute. This allows you to inspect the
     |      exception after the assertion::
     |
     |          with self.assertRaises(SomeException) as cm:
     |              do_something()
     |          the_exception = cm.exception
     |          self.assertEqual(the_exception.error_code, 3)
     |
     |  assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs)
     |      Asserts that the message in a raised exception matches a regex.
     |
     |      Args:
     |          expected_exception: Exception class expected to be raised.
     |          expected_regex: Regex (re.Pattern object or string) expected
     |                  to be found in error message.
     |          args: Function to be called and extra positional args.
     |          kwargs: Extra kwargs.
     |          msg: Optional message used in case of failure. Can only be used
     |                  when assertRaisesRegex is used as a context manager.
     |
     |  assertRaisesRegexp = deprecated_func(*args, **kwargs)
     |
     |  assertRegex(self, text, expected_regex, msg=None)
     |      Fail the test unless the text matches the regular expression.
     |
     |  assertRegexpMatches = deprecated_func(*args, **kwargs)
     |
     |  assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None)
     |      An equality assertion for ordered sequences (like lists and tuples).
     |
     |      For the purposes of this function, a valid ordered sequence type is one
     |      which can be indexed, has a length, and has an equality operator.
     |
     |      Args:
     |          seq1: The first sequence to compare.
     |          seq2: The second sequence to compare.
     |          seq_type: The expected datatype of the sequences, or None if no
     |                  datatype should be enforced.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |
     |  assertSetEqual(self, set1, set2, msg=None)
     |      A set-specific equality assertion.
     |
     |      Args:
     |          set1: The first set to compare.
     |          set2: The second set to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |
     |      assertSetEqual uses ducktyping to support different types of sets, and
     |      is optimized for sets specifically (parameters must support a
     |      difference method).
     |
     |  assertTrue(self, expr, msg=None)
     |      Check that the expression is true.
     |
     |  assertTupleEqual(self, tuple1, tuple2, msg=None)
     |      A tuple-specific equality assertion.
     |
     |      Args:
     |          tuple1: The first tuple to compare.
     |          tuple2: The second tuple to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |
     |  assertWarns(self, expected_warning, *args, **kwargs)
     |      Fail unless a warning of class warnClass is triggered
     |      by the callable when invoked with specified positional and
     |      keyword arguments.  If a different type of warning is
     |      triggered, it will not be handled: depending on the other
     |      warning filtering rules in effect, it might be silenced, printed
     |      out, or raised as an exception.
     |
     |      If called with the callable and arguments omitted, will return a
     |      context object used like this::
     |
     |           with self.assertWarns(SomeWarning):
     |               do_something()
     |
     |      An optional keyword argument 'msg' can be provided when assertWarns
     |      is used as a context object.
     |
     |      The context manager keeps a reference to the first matching
     |      warning as the 'warning' attribute; similarly, the 'filename'
     |      and 'lineno' attributes give you information about the line
     |      of Python code from which the warning was triggered.
     |      This allows you to inspect the warning after the assertion::
     |
     |          with self.assertWarns(SomeWarning) as cm:
     |              do_something()
     |          the_warning = cm.warning
     |          self.assertEqual(the_warning.some_attribute, 147)
     |
     |  assertWarnsRegex(self, expected_warning, expected_regex, *args, **kwargs)
     |      Asserts that the message in a triggered warning matches a regexp.
     |      Basic functioning is similar to assertWarns() with the addition
     |      that only warnings whose messages also match the regular expression
     |      are considered successful matches.
     |
     |      Args:
     |          expected_warning: Warning class expected to be triggered.
     |          expected_regex: Regex (re.Pattern object or string) expected
     |                  to be found in error message.
     |          args: Function to be called and extra positional args.
     |          kwargs: Extra kwargs.
     |          msg: Optional message used in case of failure. Can only be used
     |                  when assertWarnsRegex is used as a context manager.
     |
     |  assert_ = deprecated_func(*args, **kwargs)
     |
     |  countTestCases(self)
     |
     |  debug(self)
     |      Run the test without collecting errors in a TestResult
     |
     |  defaultTestResult(self)
     |
     |  doCleanups(self)
     |      Execute all cleanup functions. Normally called for you after
     |      tearDown.
     |
     |  enterContext(self, cm)
     |      Enters the supplied context manager.
     |
     |      If successful, also adds its __exit__ method as a cleanup
     |      function and returns the result of the __enter__ method.
     |
     |  fail(self, msg=None)
     |      Fail immediately, with the given message.
     |
     |  failIf = deprecated_func(*args, **kwargs)
     |
     |  failIfAlmostEqual = deprecated_func(*args, **kwargs)
     |
     |  failIfEqual = deprecated_func(*args, **kwargs)
     |
     |  failUnless = deprecated_func(*args, **kwargs)
     |
     |  failUnlessAlmostEqual = deprecated_func(*args, **kwargs)
     |
     |  failUnlessEqual = deprecated_func(*args, **kwargs)
     |
     |  failUnlessRaises = deprecated_func(*args, **kwargs)
     |
     |  id(self)
     |
     |  run(self, result=None)
     |
     |  shortDescription(self)
     |      Returns a one-line description of the test, or None if no
     |      description has been provided.
     |
     |      The default implementation of this method returns the first line of
     |      the specified test method's docstring.
     |
     |  skipTest(self, reason)
     |      Skip this test.
     |
     |  subTest(self, msg=<object object at 0x000001D699E846F0>, **params)
     |      Return a context manager that will return the enclosed block
     |      of code in a subtest identified by the optional message and
     |      keyword parameters.  A failure in the subtest marks the test
     |      case as failed but resumes execution at the end of the enclosed
     |      block, allowing further test code to be executed.
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from unittest.case.TestCase:
     |
     |  __init_subclass__(*args, **kwargs) from builtins.type
     |      This method is called when a class is subclassed.
     |
     |      The default implementation does nothing. It may be
     |      overridden to extend subclasses.
     |
     |  addClassCleanup(function, /, *args, **kwargs) from builtins.type
     |      Same as addCleanup, except the cleanup items are called even if
     |      setUpClass fails (unlike tearDownClass).
     |
     |  doClassCleanups() from builtins.type
     |      Execute all class cleanup functions. Normally called for you after
     |      tearDownClass.
     |
     |  enterClassContext(cm) from builtins.type
     |      Same as enterContext, but class-wide.
     |
     |  setUpClass() from builtins.type
     |      Hook method for setting up class fixture before running tests in the class.
     |
     |  tearDownClass() from builtins.type
     |      Hook method for deconstructing the class fixture after running all tests in the class.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from unittest.case.TestCase:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from unittest.case.TestCase:
     |
     |  failureException = <class 'AssertionError'>
     |      Assertion failed.
     |
     |
     |  longMessage = True
     |
     |  maxDiff = 640

FUNCTIONS
    create_table(conn)
        This function is used to create a table in the database

DATA
    CONTENT = '\n        CREATE TABLE IF NOT EXISTS users (\n    ... TEXT ...

FILE
    e:\git\tdd-learning\test_create_table_in_db.py
```

What's a long report, it seems a lot of places need to be edited.