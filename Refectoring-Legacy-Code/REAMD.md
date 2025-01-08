In this lab you can get some practice with refactoring legacy code by refactoring the same script used in the video which is `compute_stats.py`.

Create a new file called **compute_stats_refactor.py** that breaks down the function in **compute_stats.py** into several smaller functions. The same text file of integers used in the video is included as well in **random_nums.txt**. 

Re-factor the function compute_stats into the following functions:

- **read_ints**: Reads in the data from random_nums.txt and convert them into a list of integers
- **count**: Returns the total number of elements in random_nums.txt
- **summation**: Returns the sum of all of the elements in random_nums.txt
- **average**: Returns the average of all of the elements in random_nums.txt
- **minimum**: Returns the smallest integer in random_nums.txt
- **maximum**: Returns the largest integer in random_nums.txt 

Once you refactored **compute_stats.py** the next step is to add new functionality to compute_stats_refactor.py using the TDD approach:
- **harmonic_mean**: Returns the harmonic mean of the elements in random_nums.txt
- **variance**: Returns the variance of the elements in random_nums.txt 
- **standard_dev**: Returns the standard deviation of all of the elements in random_nums.txt