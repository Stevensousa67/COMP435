"""
Author: Steven Sousa
Institution: Bridgewater State University - Analysis of Algorithms Section 02
Instructor: Dr. Haleh Khojasteh
Version: 1
Release Date: October 2023

Objective: This dependency will ask the user to provide a sequence of numbers that will be sorted by choosing either
Counting Sort or Bucket Sort.
"""

import SortSelection

print("Welcome to the Radix Sort program. I will request a few inputs from you, but they are easy. Please follow my "
      "instructions carefully.")

# Get array size from user
while True:
    try:
        array_size = int(input("What will be the size of the array? "))
        if array_size <= 1:
            print("Array size must greater than 1.")
        else:
            break
    except ValueError:
        print("Please enter a valid array size.")

# Populate array using numbers provided by user
initial_array = []
print("Now we will populate the array with the numbers you want.\n")
for index in range(array_size):
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input for number. Please provide a valid number for the array.")
    initial_array.append(number)

print("Initial array: ", initial_array)

# Send initial array to SortSelection.py
SortSelection.select_sort_type(initial_array)
