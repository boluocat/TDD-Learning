"""
Contains the logic for randomly creating

"""

import re
from random import choice
from random import randint
from pathlib import Path

path = Path(__file__).parent.absolute()
male_path = str(path) + r"\data\dist.male.first"
female_path = str(path) + r"\data\dist.female.first"
surname_path = str(path) + r"\data\dist.all.last"


def male_first_name():
    """
    Reads in the dat file containing male
    names, parses it, and returns a random
    male name.
    :return: A random male first name
    """
    male_names = []
    with open(male_path, 'r') as male:
        for x in male:
            res = ''.join(re.findall('[a-zA-Z]+', x))
            male_names.append(res)
        random_male = choice(male_names)
        return random_male.capitalize()


def female_first_name():
    """
    Reads in the dat file containing female
    names, parses it, and returns a random
    female name.
    :return: A random female first name
    """
    female_names = []
    with open(female_path, 'r') as female:
        for x in female:
            res = ''.join(re.findall('[a-zA-Z]+', x))
            female_names.append(res)
        random_female = choice(female_names)
        return random_female.capitalize()


def surname():
    """
    Reads in the dat file containing all last
    names, parses it, and returns a random
    last name.
    :return: A random surname
    """
    surnames = []
    with open(surname_path, 'r') as surname:
        for x in surname:
            res = ''.join(re.findall('[a-zA-Z]+', x))
            surnames.append(res)
        random_surname = choice(surnames)
        return random_surname.capitalize()


def generate_random_name():
    """
    Generates a random name. Includes first name
    and last name.
    :return: first and last name
    """
    first_name = choice([male_first_name(), female_first_name()])
    return first_name + ' ' + surname()


def random_age(min=1, max=100):
    """
    Returns a random age from 1-100. :min: and
    :max: must be between 1-100 or a ValueError
    exception will be raised.
    :min: minimum age
    :max: maximum age
    :return: random int between min and max
    """
    try:
        if min > 0 and max < 101:
            return randint(min, max)
        else:
            raise ValueError
    except ValueError:
        raise ValueError("Enter in min greater than 0 and a max "\
               "less than one")


def random_email_service():
    """
    Generates a random email service from the following
    providers: gmail, outlook, yahoo, aol, icloud, yandex
    :return: random email service
    """
    return choice(['gmail', 'outlook', 'yahoo', 'aol', 'icloud', 'yandex'])


def random_phone_number():
    """
    Creates a random phone number for the person.
    For simplicity sakes, the format wil be area
    code followed by hyphen 3 digits. The first
    digit will not include 0.
    :return: phone number in the following format:
    xxx-xxx-xxxx
    """
    phone = ''
    for x in range(0, 10):
        if x % 3 == 0 and x != 0 and x != 9:
            phone += '-'
        elif x == 0:
            phone += str(randint(1, 9))
        else:
            phone += str(randint(0, 9))
    return phone


def create_occupation():
    """
    Randomly creates the occupation of
    :return: a random occupation
    """
    return choice(['cook', 'actor', 'programmer', 'doctor',
                   'dentist', 'uber driver', 'photographer', 'astronaut'])


def create_person():
    """
    Generate a random person. Their details will be stored in
    a dictionary with the following details of the person:
    first_name, last_name, email, years, job, and number.
    :return: A dictionary that contains the key/value mappings
    of the person.
    """
    person = {}
    names = [male_first_name(), female_first_name()]
    first_name = choice(names)
    gender = 'male' if first_name == names[0] else 'female'
    last_name = surname()
    email_service = first_name.lower() + '.' + last_name.lower() + '@' + random_email_service() + '.com'
    years = random_age()
    job = create_occupation()
    number = random_phone_number()
    if years < 4:
        job = 'NA'
    elif years < 18:
        job = 'student'
    person.update({'first_name': first_name,
                   'last_name': last_name,
                   'email': email_service,
                   'sex': gender,
                   'age': years,
                   'job': job,
                   'phone': number
                   })
    return person


if __name__ == '__main__':
    person = create_person()
    print(person)