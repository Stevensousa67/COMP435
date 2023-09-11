# Steven Sousa - Bridgewater State University - COMP435: Algorithm Analysis - 11Sep2023
# This code performs the insertion sort on a received list and returns the sorted list to calling code
# Best case: O(n). Worst case: O(n^2)
def insertionSort(list1):
    """This function performs the insertion sort algorithm on a given list"""

    if len(list1) <= 0:     # Check if list is empty
        print("List is empty")
        return list1    # return to main program if empty

    elif len(list1) == 1:
        print("List contains 1 element, therefore it is sorted.")
        return list1

    else:   # Perform Insertion Sort algorithm
        n = len(list1)  # set n to the size of list to avoid calling len(x) every time in for loop
        for i in range(1, n):   # Iterate over list starting at the second element of the list
            key = list1[i]  # Save current element as key to be inserted in correct position
            j = i - 1
            while j >= 0 and key < list1[j]:    # Move elements greater than key one position ahead
                list1[j + 1] = list1[j] # Shift items to the right
                j -= 1
            list1[j + 1] = key  # Insert key into correct index

    return list1