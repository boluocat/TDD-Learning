import pathlib

parent_path = pathlib.Path(__file__).parent.absolute()
file = f'{parent_path}/random_nums.txt'

def read_ints():
    '''Reads integers from a file and returns them as a list'''
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(int(line))
    return data

def count(data):
    '''Counts the number of integers in a file'''
    return len(data)

def summation(data):
    '''Computes the sum of integers in a file'''
    return sum(data)

def average(data):
    '''Computes the average of integers in a file'''
    return sum(data) / len(data)

def minimum(data):
    '''Computes the minimum of integers in a file'''
    return min(data)

def maximum(data):
    '''Computes the maximum of integers in a file'''
    return max(data)

def harmonic_mean(data):
    '''Computes the harmonic mean of integers in a file'''
    return len(data) / sum(1 / n for n in data)

def variance(data):
    '''Computes the variance of integers in a file'''
    mean = sum(data) / len(data)
    return sum((n - mean) ** 2 for n in data) / len(data)

def standard_dev(data):
    '''Computes the standard deviation of integers in a file'''
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