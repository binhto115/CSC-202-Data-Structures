from __future__ import annotations

from typing import Any, Optional


class Node:
    """A node to be used in a doubly linked list."""

    def __init__(self, value: Any, prev: Optional[Node], nxt: Optional[Node]):
        self.value = value

        # NOTE: This means that if prev and nxt are None, self.prev and
        # self.next will be self.  You may find this useful.  This means
        # that self.prev and self.next aren't Optional Nodes, they are
        # always Nodes.
        self.prev: Node = prev or self
        self.next: Node = nxt or self


class OrderedList:
    """A circular, doubly linked list, ordered from lowest to highest.

    The contents of the list *must* have an accurate notation of less
    than and of equality.  That is to say, the contents of the list must
    implement both __lt__ and __eq__.  This *does not* mean that your
    OrderedList (or your Nodes) should have __lt__ and __eq__.

    Your implementation should use a single dummy node as the "head".
    """
    def __init__(self) -> None:
        self.head = Node(1, None, None)
        self.head.prev = self.head
        self.head.next = self.head
        self.size = 0


def insert(lst: OrderedList, value: Any) -> None:
    """Insert the value into the list in the proper (ordered) location."""
    new_node = Node(value, lst.head.prev, lst.head.next)
    curr = lst.head.next
    while (curr is not lst.head and value > curr.value):
        curr = curr.next
    new_node.next = curr
    new_node.prev = curr.prev
    curr.prev.next = new_node
    curr.prev = new_node
    lst.size += 1


def remove(lst: OrderedList, value: Any) -> None:
    """Remove the first occurrence of value from the list.

    Raises ValueError if the value is not present.
    """
    curr = lst.head.next
    while curr is not lst.head and value != curr.value:
        curr = curr.next
    if (curr is not lst.head and value == curr.value):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = curr
        curr.prev = curr
    else:
        raise ValueError
    lst.size -= 1


def contains(lst: OrderedList, value: Any) -> bool:
    """Return True if the value is in the list, False otherwise."""
    curr = lst.head.next
    while curr is not lst.head:
        if value == curr.value:
            return True
        else:
            curr = curr.next
    return False


def index_of(lst: OrderedList, value: Any) -> int:
    """
    Return the index of the first occurrence of value in the list.
    Raises ValueError if the value is not present.
    """
    curr = lst.head.next
    count = 0
    while curr is not lst.head and value != curr.value:
        count += 1
        curr = curr.next
    if curr is not lst.head and value == curr.value:
        return count
    else:
        raise ValueError


def get(lst: OrderedList, index: int) -> Any:
    """Return the value at index in the list.

    Raises IndexError if the index is out of range.
    """
    curr = lst.head.next
    count = 0
    if index >= lst.size or index < 0:
        raise IndexError
    else:
        while curr is not lst.head:
            if count == index:
                return curr.value
            else:
                count += 1
                curr = curr.next


def pop(lst: OrderedList, index: int) -> Any:
    """Remove and returns the value at index in the list.

    Raises IndexError if the index is out of range.
    """
    curr = lst.head.next
    count = 0
    while curr is not lst.head and index != count:
        count += 1
        curr = curr.next
    if curr is not lst.head and count == index:
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = curr
        curr.prev = curr
    else:
        raise IndexError
    lst.size -= 1
    return curr.value


def is_empty(lst: OrderedList) -> bool:
    """Return True if the list is empty, False otherwise."""
    if lst.size == 0:
        return True
    else:
        return False


def size(lst: OrderedList) -> int:
    """Return the number if items in the list."""
    return lst.size
