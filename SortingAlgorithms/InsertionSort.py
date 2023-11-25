from typing import List

########################################################################################
# Insertion Sort
# A simple sorting algorithm that builds the final sorted array one item at a time.
# It is much less efficient on large lists than more advanced algorithms such as quicksort.
# Time Complexity: O(n^2) in the worst case.
# Best suited for small data sets or partially sorted data.
########################################################################################


def insertion_sort(array: List) -> List:
    """
    Sort an array using the insertion sort algorithm.

    Parameters:
    array (List[int]): A list of integers to be sorted.

    Returns:
    List[int]: The sorted list.

    The function iteratively considers each element of the list (starting from the second element)
    and inserts it into the correct position in the already sorted part of the list.
    This process is repeated until the entire list is sorted.
    """
    for i in range(1, len(array)):
        current_counter = i
        while current_counter > 0 and array[current_counter] < array[current_counter - 1]:
            array[current_counter], array[current_counter - 1] = array[current_counter - 1], array[current_counter]
            current_counter -= 1
    return array

########################################################################################
#              i
# Steps 1: [4, 5, 3, 6, 2, 7, 1]
#                 i
# Steps 2: [4, 5, 3, 6, 2, 7, 1] -> [4, 3, 5, 6, 2, 7, 1] -> [3, 4, 5, 6, 2, 7, 1]
#                    i
# Steps 3: [3, 4, 5, 6, 2, 7, 1]
#                       i
# Steps 4: [3, 4, 5, 6, 2, 7, 1] -> [3, 4, 5, 2, 6, 7, 1] -> [3, 4, 2, 5, 6, 7, 1]
#          -> [3, 2, 4, 5, 6, 7, 1] -> [2, 3, 4, 5, 6, 7, 1]
#                          i
# Steps 5: [2, 3, 4, 5, 6, 7, 1]
#                             i
# Steps 5: [2, 3, 4, 5, 6, 7, 1] => 4 Steps => [1, 2, 3, 4, 5, 6, 7]
########################################################################################

if __name__ == '__main__':
    current_unsorted = [4, 5, 3, 6, 2, 7, 1]

    print(insertion_sort(current_unsorted))
