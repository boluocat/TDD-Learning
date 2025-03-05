'''
This module generates random people with random attributes such as first name, last name, age, email, phone number, and occupation.
'''
import random 
import pathlib

def read_file(file_name):
    '''Read a file and return a list of lines'''
    with open(file_name) as f:
        return f.read().splitlines()
    
def male_first_name():
    '''Return a random male first name from dist.male.first file'''
    male_list = read_file(f'{parent_path}/data/dist.male.first')
    chosen_male = random.choice(male_list)
    return chosen_male.split(' ')[0]

def female_first_name():
    '''Return a random female first name from dist.female.first file'''
    female_list = read_file(f'{parent_path}/data/dist.female.first')
    chosen_female = random.choice(female_list)
    return chosen_female.split(' ')[0]

def surname():
    '''Return a random surname from dist.all.last file'''
    surname_list = read_file(f'{parent_path}/data/dist.all.last')
    chosen_surname = random.choice(surname_list)
    return chosen_surname.split(' ')[0]

def generate_random_name():
    '''Generate a random name including first name and last name'''
    if gender == 'male':
        return male_first_name(), surname()
    else:
        return female_first_name(), surname()
    
def random_age(min=1, max=100):
    '''Generate a random age between min and max'''
    if min < 0 or max > 100:
        return 'Enter in min greater than 0 and a max less than one hundred'
    return random.randint(min, max)

def random_email_service():
    '''Generate a random email service provider'''
    email_service_provider = ['gmail.com', 'yahoo.com', 'outlook.com', 'aol.com', 'hotmail.com']
    return random.choice(email_service_provider)
    
def random_phone_number():
    '''Generate a random phone number'''
    first_part = random.randint(100,999)
    second_part = random.randint(000,999)
    third_part = random.randint(000,999)
    return f'{first_part}-{second_part}-{third_part}'

def create_occupation(age):
    '''Create an occupation based on age'''
    occupation_list = ['cook','actor','programmer','doctor','dentist','uber driver','photographer','astronaut']
    if age < 4:
        return 'NA'
    elif age >=4 and age < 18:
        return 'student'
    else:
        return random.choice(occupation_list)
    
def create_person():
    '''Create a person with random attributes'''
    first_name = generate_random_name()[0]
    last_name = generate_random_name()[1]
    email_service = random_email_service()
    email = f'{first_name}.{last_name}@{email_service}'
    sex = gender
    age = random_age()
    job = create_occupation(age)
    phone = random_phone_number()
    return {'first_name': first_name, 'last_name': last_name, 'email': email, 'sex':sex, 'age': age, 'job': job, 'phone': phone}


parent_path = pathlib.Path(__file__).parent.absolute()
gender = random.choice(['male', 'female'])