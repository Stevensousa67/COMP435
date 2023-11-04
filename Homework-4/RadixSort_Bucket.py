"""
Author: Steven Sousa
Institution: Bridgewater State University - Analysis of Algorithms Section 02
Instructor: Dr. Haleh Khojasteh
Version: 1
Release Date: October 2023

Objective: This dependency will apply the Bucket Sort algorithm to the Radix Sort on the sequence of numbers generated
in SequenceGenerator.py by the user and passed onto SortSelection.py
"""


def radix_sort(initial_array):
    print("\nYour custom array will be sorted using bucket sort implementation.")
    print("Initial array: ", initial_array)

    # Find the max number in the array to determine the number of passes and initialize digit place to LSD
    max_num = max(initial_array)
    digit_place = 1

    while max_num // digit_place > 0:
        # Create 10 buckets (0 - 9) for each digit place
        buckets = [[] for _ in range(10)]

        # Distribute elements into buckets based on the current digit place
        for number in initial_array:
            current_digit = (number // digit_place) % 10
            buckets[current_digit].append(number)

        # Reconstruct the array by combining the elements from the buckets
        initial_array = []
        for bucket in buckets:
            initial_array.extend(bucket)

        # Move to the next digit place
        digit_place *= 10

    print("Sorted array: ", initial_array)
