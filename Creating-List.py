# Steven Sousa - Bridgewater State University - COMP435: Algorithm Analysis - 11Sep2023
# This code generates a List for the purpose of being sorted by calling the InsertionSort program.

from InsertionSort import *     # Import InsertionSort.py, so we can call insertionSort()
from MergeSort import *         # Import MergeSort.py, so we can call mergeSort()
from SelectionSort import *     # Import SelectionSort.py, so we can call selectionSort()

listLength = int(input("How long will the list be? "))  # Gather how long the list will be
list1 = list()  # Creating the list

for n in range(listLength):   # For loop to populate list
    x = int(input("What will the number be? "))  # Ask user what will the number at current n be
    list1.append(x)     # Add that number to the list

print("\nList prior to sorting: ", list1)

mergeSort(list1, 0, len(list1) - 1)
#insertionSort(list1)    # Call insortionSort()

print("List post sort: ", list1)

