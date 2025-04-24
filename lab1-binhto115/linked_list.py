from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, nxt: LinkedList):
        self.value = value
        self.next = nxt

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Node) and
            self.value == other.value and self.next == other.next
            )

    def __repr__(self) -> str:
        return "Node(%r, %r)" % (self.value, self.next)


LinkedList = Optional[Node]


def empty_list() -> LinkedList:
    """
    This function returns an empty list
    """
    return None


def add(lst: LinkedList, index: int, value: Any) -> LinkedList:
    """This function returns a new list after the given value is
    added to a Node indicated by the given index. Raise IndexError
    if the index is greater than the length of the list or less than zero.
    """
    if lst is None and index == 0:
        return Node(value, lst)
    elif lst is None and index > 0:
        raise IndexError
    elif index < 0:
        raise IndexError
    else:
        if index == 0:
            return Node(value, lst)
        else:
            return Node(lst.value, add(lst.next, index - 1, value))


def length(lst: LinkedList) -> int:
    """This function returns the length of the given list"""
    if lst is None:
        return 0
    else:
        return 1 + length(lst.next)


def get(lst: LinkedList, index: int) -> Any:
    """This function returns the value in the linked list
    indicated by the given index. If the index is greater
    than the length of the list, or less than 0, the function
    raises an IndexError. The function also raises an IndexError
    if the list is empty and an index is given.
    """
    if lst is None:
        raise IndexError
    elif index < 0:
        raise IndexError
    else:
        if index == 0:
            return lst.value
        else:
            return get(lst.next, index - 1)


def setitem(lst: LinkedList, index: int, value: Any) -> LinkedList:
    """This function returns a new list after a value indicated by the
    index is replaced by the given value. If the list is empty, or the index
    is out of range, the function will raise an IndexError.
    """
    if lst is None:
        raise IndexError
    elif index < 0:
        raise IndexError
    else:
        if index == 0:
            return Node(value, lst.next)
        else:
            return Node(lst.value, setitem(lst.next, index - 1, value))


def remove(lst: LinkedList, index: int) -> tuple[Any, LinkedList]:
    """This function returns a tuple of the removed element and a new list
    indicated by the index. If the list is empty or the index is out of range,
    the function will raise an IndexError.
    """
    if lst is None:
        raise IndexError
    else:
        if index == 0:
            removed_element = lst.value
            return (removed_element, lst.next)

        else:
            removed_element, new_rest = remove(lst.next, index - 1)
            return (removed_element, Node(lst.value, new_rest))
