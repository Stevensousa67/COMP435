# Steven Sousa - Bridgewater State University - COMP435: Algorithm Analysis - 11Sep2023
# This code performs the merge sort on a received list and returns the sorted list to calling code
# Best and worst case: O(n*log(n))

def merge(list1, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Create temp lists
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp lists L[] and R[]
    for i in range(0, n1):
        L[i] = list1[l + i]

    for j in range(0, n2):
        R[j] = list1[m + 1 + j]

    # Merge the temp arrays back into list[l..r]
    i = 0  # Initial index of first sublist
    j = 0  # Initial index of second sublist
    k = l  # Initial index of merged sublist

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list1[k] = L[i]
            i += 1
        else:
            list1[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        list1[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        list1[k] = R[j]
        j += 1
        k += 1

    # l is for left index and r is right index of the sublist of list1 to be sorted


def mergeSort(list1, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(list1, l, m)
        mergeSort(list1, m + 1, r)
        merge(list1, l, m, r)

    return list1
