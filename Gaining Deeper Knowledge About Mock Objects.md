Mocks are a type of object which emulates or "mocks" the behavior of real objects.

Here are three reasons why mock objects are useful: 

- Can abstract away complex external dependencies such as database setup, api calls, and server requests
- Useful for testing non-deterministic algorithms, or those that produce different output for the same set of input like a pseudo random number generator
- Helps keep unit tests running fast

Since this course is using unittest as the primary framework for writing unit tests we’re going to use the `unittest.mock` library to tap into the power of mock objects as it was designed to be used with it. You can read up about this module by reading the 
python documentation. 

There's also a couple more terms that I would like to demystify because when you research more about mock objects online you will most likely come across them. These terms are mock, stub, and fake. 

- **mock**: **A dummy piece of code that verifies that everything was called correctly**. In other words, they have pre-programmed expectations. For example, let’s say that you’re creating a web app that requires user registration before they can use it. After calling save the mock should verify that send_email was also called afterwards. 
  - Purpose: Mocks are used to verify the interactions between objects, especially the method calls, arguments passed, and the order in which methods are called.
  - Behavior: A mock is an object that not only simulates a real object but also keeps track of how it is used during the test (i.e., which methods were called, how many times, with what parameters).
  - Example: You might use a mock to ensure that a method was called with the correct arguments or that a method was called a specific number of times.
  - Example in Python (using unittest.mock):
    ```python
    from unittest.mock import MagicMock

    # Creating a mock
    mock_service = MagicMock()

    # Simulating behavior
    mock_service.get_data.return_value = "expected data"
    
    # Verifying interaction
    mock_service.get_data()
    mock_service.get_data.assert_called_once_with()
    ```
  - Use case: Verifying that specific interactions between objects happen correctly (e.g., method calls, exceptions thrown, etc.)
- **stub**: **A dummy piece of code that provides canned answers during the test**. For example, let’s assume that you’re creating some type of physics generator app that has a function called compute which takes on average 3 minutes to run. To save time during testing you replace the real implementation with some dummy values for the sake of speed. 
  - Purpose: Stubs are used to provide predefined responses to method calls during the test, ensuring the test can proceed with controlled behavior. They don’t concern themselves with tracking interactions or verifying things like mocks do.
  - Behavior: A stub is an object that provides canned responses (usually by returning values or throwing exceptions) for specific methods. It’s used to isolate the unit under test from external dependencies.
  - Example: If you're testing a service that calls a database, you might use a stub to simulate the database's behavior by returning predefined data.
  - Example in Python:
    ```python
    # Stub function to return a predefined response
    def get_data_from_database():
        return "stubbed data"
    
    result = get_data_from_database()
    print(result)  # Output: stubbed data
    ```
  - Use case: Replacing external services (e.g., database, APIs) in tests with controlled, predefined responses.
- **fake**: **Create a simplified implementation of an external dependency**. For example, instead of setting up an actual database for testing which can be very time consuming, you use a simpler in-memory database. 
  - Purpose: Fakes are implementations that behave like the real objects but are typically simpler or less performant. They are used when the actual implementation of the object is not necessary for the test.
  - Behavior: A fake is a working implementation of a method or service but simplified or optimized for testing. It often behaves like the real object but might not provide all the functionality or might be optimized for testing scenarios.
  - Example: A fake database might be a simplified in-memory database that mimics the behavior of a real database but doesn't persist data between tests.
  - Example in Python:
    ```python
      class FakeDatabase:
        def __init__(self):
            self.data = {}
    
        def save(self, key, value):
            self.data[key] = value
    
        def get(self, key):
            return self.data.get(key)
    
    fake_db = FakeDatabase()
    fake_db.save("user1", "data1")
    print(fake_db.get("user1"))  # Output: data1
    ```
  - Use case: When you need a fully functional object with simplified or less expensive behavior for testing (e.g., in-memory data stores).


The differences between stub and mock may still not be clear so I'll like to do some further explanation. Another way to differentiate them is to be aware that:
- A stub is built solely for testing purposes while a mock is like a stub but it also records if expected calls were made. 
- Also, a stub doesn't fail while a mock can fail. 
- A stub also makes sure that a method returns the correct value while a mock acts similar to a debugger, stepping into the code and making sure that everything is correct before returning the correct value. 