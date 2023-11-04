"""
Author: Steven Sousa
Institution: Bridgewater State University - Analysis of Algorithms Section 02
Instructor: Dr. Haleh Khojasteh
Version: 1
Release Date: October 2023

Objective: This dependency will apply the Counting Sort algorithm to the Radix Sort on the sequence of numbers generated
in SequenceGenerator.py by the user and passed onto SortSelection.py
"""


def radix_sort(initial_array):
    print("\nYour custom array will be sorted using counting sort implementation.")
    print("Initial array: ", initial_array)

    # Find the maximum number to determine the number of digits and initialize the digit place to LSD
    max_num = max(initial_array)
    digit_place = 1

    while max_num // digit_place > 0:
        # Initialize counting array for each digit (0-9)
        counting_array = [0] * 10

        # Count occurrence of each digit at the current digit place
        for number in initial_array:
            digit = (number // digit_place) % 10
            counting_array[digit] += 1

        # Calculate cumulative counts to determine the correct positions
        for i in range(1, 10):
            counting_array[i] += counting_array[i - 1]

        # Build the sorted array
        sorted_array = [0] * len(initial_array)
        for number in reversed(initial_array):
            digit = (number // digit_place) % 10

            # Place the number in the correct position based on cumulative counts
            sorted_array[counting_array[digit] - 1] = number
            counting_array[digit] -= 1

        # Copy the sorted array back to initial array and move to the next digit place
        initial_array = sorted_array
        digit_place *= 10

    print("Sorted array: ", initial_array)
