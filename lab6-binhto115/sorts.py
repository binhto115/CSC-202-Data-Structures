from __future__ import annotations

from typing import Any


def selection_sort(lst: list[Any]) -> int:
    """Sorts the given list with selection sort.

    Returns the number of comparisons made.
    """
    comparison_count = 0
    for i in range(0, len(lst)):
        min_index = i
        # Loop to find the minimum value
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
            comparison_count += 1
        temp_value = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp_value
    return comparison_count


def insertion_sort(lst: list[Any]) -> int:
    """Sorts the given list with insertion sort.

    Returns the number of comparisons made.
    """
    count = 0
    # Setting up the value at the first index
    # for comparisons to previous values
    for i in range(1, len(lst)):
        temp_value = lst[i]
        temp_index = i - 1
        # While the previous value is greater than the set-temp value,
        # Move it up by one index
        while temp_index >= 0 and lst[temp_index] > temp_value:
            count += 1
            lst[temp_index + 1] = lst[temp_index]
            temp_index -= 1
        count += 1
        # Count when the values are already sorted
        lst[temp_index + 1] = temp_value
    return count

# NOTE: you shouldn't need to change any of the merge sort code.
def merge_sort(lst: list[Any]) -> int:
    """Sorts the given list with merge sort.

    Returns the number of comparisons made.
    """
    # Make a copy of the given list and use it as the source for the
    # sort.  The sorted results will then be placed back into the given
    # list.
    return merge_sort_partial(lst[:], lst, 0, len(lst))


def merge_sort_partial(
    source_list: list[Any], target_list: list[Any], start: int, end: int
) -> int:
    """Sorts the elements in source_list between the start and end.

    Places the sorted result in target_list.

    Returns the number of comparisons made.
    """
    comparisons = 0

    # If there are at least 2 things to sort
    if end - start > 1:
        mid = (start + end) // 2

        # Recursively sort both halves.  We sort from the target_list
        # into the source_list here so that in the merge step, we merge
        # from the source_list back into the target list.
        comparisons += merge_sort_partial(target_list, source_list, start, mid)
        comparisons += merge_sort_partial(target_list, source_list, mid, end)

        # Merge the sorted source_list[start:mid] and
        # source_list[mid:end] into the target_list[start:end].
        comparisons += merge(source_list, target_list, start, mid, end)

    return comparisons


def merge(
    source_list: list[Any],
    target_list: list[Any],
    start: int,
    mid: int,
    end: int,
) -> int:
    """Merge the sorted source_list[start:mid] and source_list[mid:end].

    Places the result into target_list[start:end] in sorted order.

    Returns the number of comparisons made.
    """
    left = start
    right = mid
    target_index = start
    comparisons = 0

    # While both sides still have more data
    while left < mid and right < end:
        # Compare to see which is the smaller value, and put that next
        # into the target_list.
        comparisons += 1
        if source_list[left] < source_list[right]:
            target_list[target_index] = source_list[left]
            left += 1
        else:
            target_list[target_index] = source_list[right]
            right += 1
        target_index += 1

    # Transfer the rest of the items in the left to sorted list.
    while left < mid:
        target_list[target_index] = source_list[left]
        target_index += 1
        left += 1

    # Transfer the rest of the items in the right to sorted list.
    while right < end:
        target_list[target_index] = source_list[right]
        target_index += 1
        right += 1

    return comparisons
