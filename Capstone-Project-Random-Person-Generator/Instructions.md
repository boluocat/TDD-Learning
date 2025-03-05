# Background
The goal of the project will be to build a random person generator using Python.

When the main script is run, the output should look something like the following:
```Python
{'first_name': 'Elenore', 'last_name': 'Mccreary', 'email': 'elenore.mccreary@icloud.com', 'sex': 'female', 'age': 76, 'job': 'programmer', 'phone': '598-94-399'}
```

The project will incorporate the concepts related to test driven development (TDD) taught in courses 1-3 by using the Red-Greed-Refactor approach to coding. Here's an example of the file structure I created for project.

```txt
- data
    - dist.all.last
    - dist.female.first
    - dist.male.first

- tests
    - test_random_person_generator.py
- random_person_generator.py
```

The data folder holds the datasets that you'll be using, the tests folder holds the unit tests for your program, and random_person_generator.py contains the core logic.

The first step is to get a list of first names and last names. That way you can read the file into python and then extract the details you'll need for the program. An open data set of names that you can use is from census.gov: https://www.census.gov/topics/population/genealogy/data/1990_census/1990_census_namefiles.html

These datasets contain 80,000+ names which will give the random banes we generate lots of variance. Download the .dat file to the location of the data folder on your machine. A .dat file is just a generic data file, and in this case it contains text.

# Functions in This program

Now that you have the project structure and files that you'll be using let's take a look at the individual functions that you'll be creating along with their purpose.
- male_first_name(): Iterates through dist.male.first and randomly selects a name.
- female_first_name(): Iterates through dist.female.first and randomly selects a name.
- surname(): Iterates through dist.all.last and randomly selects a name.
- generate_random_name(): Generates a random first and last name.
- random_age(min=1, max=100): Generates a random integer which represents age. The default keyword arguments are min and max which represents the minimum and maximum age limits respectively. The function should use a try/except statement to verify that the input is **not outside of the range 1-100**. If the exception is triggered the function should return the following message:
  ```txt
  "Enter in min greater than 0 and a max less than one hundred"
  ```
- random_email_service(): Generates a random email service provider such as aol, gmail, outlook, yahoo, icloud, or yandex.
- random_phone_number(): Generates a random phone number using the following syntax:**###-###-####**. The very **first digit should not be 0**.
- create_occupation(): Returns a random occupation such as cook, actor, programmer, doctor, dentist, uber driver, photographer, or astronaut. **If the person's age is less than 4, the job will default 'NA', and if the person's age is less than 8 then the job will default to 'student'**.
- create_person(): Builds a dictionary of a random person and returns it. Here's an example of such a dictionary:
  ```python
  {'first_name': 'Pasquale', 'last_name': 'Stommes', 'email': 'pasquale.stommes@outlook.com', 'sex': 'male', 'age': 3, 'job': 'NA', 'phone': '343-58-515'}
  ```
  **The dictionary built should contain the first name, last name, email, sex, age, job and phone number. The email address should contain the first name, dot, last name, ampersand, email service, and then dot com.**

# Unit test
All of the nine functions is random_person_generator.py should have associated unit tests. The unit tests should be placed under the tests folder and in a file called test_random_person_generator.py.

When run, all of the unit tests should pass:
```txt
.........

----------------------------------------------------------------------

Ran 9 tests in 0.004s
```

# Modules That Will Help 
There are several modules from the python standard library which can assist with building this program. They are:

- re: https://docs.python.org/3/library/re.html
- random: https://docs.python.org/3/library/random.html
- unittest.mock: https://docs.python.org/3/library/unittest.mock.html
- pathlib: https://docs.python.org/3/library/pathlib.html
- Also, to read in files in python research the with statement:  https://docs.python.org/3/reference/compound_stmts.html#the-with-statement

Make sure that your code is formatted according to PEP 8 and that your functions contain documentation. 
https://www.python.org/dev/peps/pep-0008

Since the goal of the course is to learn TDD, the code for this project must be built using this approach. Create the test for male_first_name that fails, do the minimum to get it to pass, and then refactor. Need help getting started? Read the getting started guide.