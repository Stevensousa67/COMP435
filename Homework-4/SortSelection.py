"""
Author: Steven Sousa
Institution: Bridgewater State University - Analysis of Algorithms Section 02
Instructor: Dr. Haleh Khojasteh
Version: 1
Release Date: October 2023

Objective: This dependency will apply the Radix Sort algorithm on the sequence of numbers provided by the user in
SequenceGenerator.py and use either Counting Sort or Bucket Sort depending on which option the user selected.
"""

import RadixSort_Bucket
import RadixSort_Counting


def select_sort_type(initial_array):
    # Get sorting technique to be applied in Radix Sort from user
    while True:
        try:
            selection = int(input("\nNow that we have a fully populated array, which sorting technique would you like "
                                  "the Radix Sort to use? Type the number of the corresponding technique you'd like.\n"
                                  "1 - Counting Sort\n"
                                  "2 - Bucket Sort\n"))

            if selection not in [1, 2]:
                print("Please type 1 for Counting Sort or 2 for Bucket Sort.")
            else:
                break
        except ValueError:
            print("Please type a number for your selection (1 or 2).")

    if selection == 1:
        RadixSort_Counting.radix_sort(initial_array)
    elif selection == 2:
        RadixSort_Bucket.radix_sort(initial_array)
