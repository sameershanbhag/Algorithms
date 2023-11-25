from typing import List

########################################################################################
# Binary Search
# An efficient algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing in half the portion of the list that could contain the item,
# until you've narrowed down the possible locations to just one.
# Time Complexity:
# Best Case: O(1)
# Average Case: O(log N)
# Worst Case: O(log N)
# Space Complexity: O(1) for iterative approach, O(log N) for recursive due to call stack.
########################################################################################


def binary_search_element(array: List, left: int, right: int, target: int):
    """
    Perform binary search on a sorted array iteratively.

    Parameters:
    array (List[int]): The sorted list to search in.
    left (int): The starting index of the list.
    right (int): The ending index of the list.
    target (int): The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    while left <= right:
        mid = left + (right - left) // 2

        # See if mid == target: if so return index
        if target == array[mid]:
            return mid
        # See if mid > target: if so move the right pointer
        elif array[mid] > target:
            right = mid - 1
        # See if mid > target: if so move the left pointer
        else:
            left = mid + 1
    # Return -1 in case it's not found
    return -1


def binary_search_recursive(array: List, target: int):
    """
    Perform binary search on a sorted array recursively.

    Parameters:
    array (List[int]): The sorted list to search in.
    target (int): The value to search for.

    Returns:
    bool: True if target is found, otherwise False.
    """
    if len(array) == 1:
        return array[0] == target

    mid = len(array) // 2

    # Check if the mid > target or less than target
    # This will determine which half to continue search in

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search_recursive(array[:mid], target)
    elif array[mid] < target:
        return binary_search_recursive(array[mid:], target)

    return False


if __name__ == '__main__':
    ar = [1, 2, 3, 4, 5, 6, 7]
    search_for = 5

    if binary_search_recursive(ar, search_for):
        print(f"{search_for} : Found")
    else:
        print(f"{search_for} : Not Found")

    index = binary_search_element(ar, 0, len(ar), search_for)

    print(f"Found at: {index}")
