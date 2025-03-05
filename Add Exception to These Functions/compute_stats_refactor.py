import pathlib

parent_path = pathlib.Path(__file__).parent.absolute()
file = f'{parent_path}/random_nums.txt'

def read_ints():
    '''Reads integers from a file and returns them as a list'''
    data = []
    try:
        with open(file, 'r') as f:
            for line in f:
                data.append(int(line))
    except FileNotFoundError:
        print(f'File {file} not found')
    else:
        return data

def count(data):
    '''Counts the number of integers in a file'''
    try:
        data[0]
    except ValueError:
        print(f'Input data is not a list')
    return len(data)

def summation(data):
    '''Computes the sum of integers in a file'''
    try:
        sum(data)
    except TypeError:
        print(f'Input data is not a number list')
    return sum(data)

def average(data):
    '''Computes the average of integers in a file'''
    try:
        sum(data) / len(data)
    except ZeroDivisionError:
        print(f'Cannot divide by zero')
    return sum(data) / len(data)

def minimum(data):
    '''Computes the minimum of integers in a file'''
    try:
        min(data)
    except ValueError:
        print(f'Input data is not a number list')
    return min(data)

def maximum(data):
    '''Computes the maximum of integers in a file'''
    try:
        max(data)
    except ValueError:
        print(f'Input data is not a number list')
    return max(data)

def harmonic_mean(data):
    '''Computes the harmonic mean of integers in a file'''
    try:
        len(data) / sum(1 / n for n in data)
    except ZeroDivisionError:
        print(f'Cannot divide by zero')
    else:
        return len(data) / sum(1 / n for n in data)

def variance(data):
    '''Computes the variance of integers in a file'''
    try:
        mean = sum(data) / len(data)
    except ZeroDivisionError:
        print(f'Cannot divide by zero')
    else:
        return sum((n - mean) ** 2 for n in data) / len(data)

def standard_dev(data):
    '''Computes the standard deviation of integers in a file'''
    try:
        len(data)
    except TypeError:
        print(f'Input data is not a number list')
    return variance(data) ** 0.5

if __name__ == "__main__":
    data = read_ints()
    print(f'total = {count(data)}')
    print(f'summation = {summation(data)}')
    print(f'average = {average(data)}') 
    print(f'Minimum = {minimum(data)}')
    print(f'Maximum = {maximum(data)}')
    print(f'Harmonic Mean = {harmonic_mean(data)}')
    print(f'Variance = {variance(data)}')
    print(f'Standard Deviation = {standard_dev(data)}')