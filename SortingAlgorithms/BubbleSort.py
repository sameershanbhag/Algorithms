from typing import List

########################################################################################
# Bubble Sort
# A simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements and swaps them if they are in the wrong order.
# Time Complexity: Generally O(n^2) in the worst case.
# Space Complexity: O(1), as it's an in-place sorting algorithm.
# Note: Due to its simplicity, it is mostly used for educational purposes and
# small data sets. Not recommended for large datasets due to inefficiency.
########################################################################################


def bubble_sort(array: List) -> List:
    """
    Sort an array using the bubble sort algorithm.

    Parameters:
    array (List[int]): A list of integers to be sorted.

    Returns:
    List[int]: The sorted list.

    This function iteratively steps through the list, compares adjacent elements,
    and swaps them if they are in the incorrect order. The process is repeated
    until the list is sorted.
    """
    counter = len(array) - 1
    i = 0
    while counter > 0:
        if i == counter:
            counter -= 1
            i = 0
            continue
        if array[i] > array[i+1]:
            array[i], array[i + 1] = array[i + 1], array[i]

        i += 1
    return array


if __name__ == '__main__':
    current_unsorted = [4, 5, 3, 6, 2, 7, 1]

    print(bubble_sort(current_unsorted))
