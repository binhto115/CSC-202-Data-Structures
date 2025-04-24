from __future__ import annotations

from typing import Any


class ArrayList:
    # NOTE: Initial capacity is somewhat arbitrary.  To making testing
    # resizing easier, you'll probably want a small initial capacity.
    # In practice, you'd probably have an initial capacity of 5–10.
    def __init__(self, capacity: int = 1):
        self.array: list[Any] = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def __repr__(self):
        return "%r" % (self.array)


def empty_list() -> ArrayList:
    """This function returns an empty array list."""
    return ArrayList()


def add(lst: ArrayList, index: int, value: Any) -> ArrayList:
    """
    This function returns the resulting array list with the value
    indicated by the given index. It raises IndexError if the given index
    is out ouf bounds.
    """
    if (index < 0) or (index > lst.size):
        raise IndexError
    elif lst.size == lst.capacity:
        new_array = [None] * (2 * lst.capacity)
        for i in range(0, lst.size):
            new_array[i] = lst.array[i]
        lst.array = new_array
        lst.capacity = lst.capacity * 2
    for i in range(lst.size - 1, index - 1, -1):
        lst.array[i + 1] = lst.array[i]
    lst.array[index] = value
    lst.size += 1
    return lst


def length(lst: ArrayList) -> int:
    """
    This function returns the number that represents elements in the list.
    """
    return lst.size


def get(lst: ArrayList, index: int) -> Any:
    """
    This function returns the value indicated by the given index.
    This function will raise IndexError if the given index is out of bounds.
    """
    if index >= lst.size:
        raise IndexError
    elif index < 0:
        raise IndexError
    else:   
        return lst.array[index]


def setitem(lst: ArrayList, index: int, value: Any) -> ArrayList:
    """
    This function returns the resulting arraylist after a value is replaced
    by the given value indicated by the given index.
    This function will raise IndexError if the given index is out of bounds.
    Take O(1) time because you know the index and so you can just get there
    """
    if index < 0:
        raise IndexError
    elif index >= lst.size:
        raise IndexError
    else:
        lst.array[index] = value
    return lst


def remove(lst: ArrayList, index: int) -> tuple[Any, ArrayList]:
    """
    This function removes a value indicated by the given index and returns
    the removed index and the resulting arraylist as a tuple.
    This function will raise IndexError if the index is out of bounds.
    """
    if (index < 0) or (index >= lst.size):
        raise IndexError
    else:
        removed_element = lst.array[index]
        for i in range(index, lst.size - 1):
            lst.array[i] = lst.array[i + 1]
    lst.array[lst.size - 1] = None
    lst.size -= 1
    return (removed_element, lst)
