import random
from typing import List

########################################################################################
# Binary Search
# Works only on `Sorted Data`
# It divides the array in half for every iteration
# Allowing it to search faster for a number
# Time Complexity:
# Best Case: O(1)
# Average Case: O(log N)
# Worst Case: O(log N)
# Auxiliary Space: O(1),
# If the recursive call stack is considered then the auxiliary space will be O(logN).
########################################################################################


def merge_sort(array: List):
    if len(array) > 1:
        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    ar = random.sample(range(10, 70), 15)
    print(f"Unsorted: {ar}")
    merge_sort(ar)
    print(f"Sorted: {ar}")
