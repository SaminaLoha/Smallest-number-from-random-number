import random

from inputData import InputData


# Function to generate random number
# random.sample will take in range and size of sample and generate unique random numbers
def generator(start, end, number):
    numbers = random.sample(range(start, end), number)
    return numbers


# Function to find nth smallest number from given random number list
def smallestNumber(list_numbers, index):
    list_numbers.sort()
    print("Sorted list of random numbers - " + str(list_numbers))
    return numberList[index - 1]


# Input for range and nth number is taken from inputData.py file
# Validation messages are written for input data
low = InputData.testInput["start_range"]
high = InputData.testInput["end_range"]
if high < low:
    print("End range for sample should be greater than start range.\nChange values in inputData.py file!")
    exit()

size = 500
if high - low < size:
    print("The range of numbers(sample size) should be greater than equal to 500.\nChange values in inputData.py file!")
    exit()

nth_index = InputData.testInput["nth_index"]
if nth_index > 500:
    print("The value of n should be less than or equal to 500.\nChange value of nth_index in inputData.py file!")
    exit()

numberList = generator(low, high, size)
print("Smallest " + str(nth_index) + "th number from random list is -  " + str(smallestNumber(numberList, nth_index)))
