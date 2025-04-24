# NOTE: Do not import anything else.
from __future__ import annotations

from typing import Any


class MaxHeap:
    def __init__(self) -> None:
        self.items: list[Any] = [None]

    def __repr__(self) -> str:
        return "%r" % self.items


def enqueue(heap: MaxHeap, item: Any) -> None:
    heap.items.append(item)
    # index of the newly added value
    new_i = len(heap.items) - 1
    # root value
    root = new_i // 2
    while root > 0 and heap.items[new_i] > heap.items[root]:
        heap.items[new_i], heap.items[root] = heap.items[root], heap.items[new_i]
        new_i = new_i // 2
        root = new_i // 2


def dequeue(heap: MaxHeap) -> Any:
    if len(heap.items) == 1:
        raise IndexError
    remove_largest = heap.items[1]
    heap.items[1] = heap.items[len(heap.items) - 1]
    heap.items.pop(len(heap.items) -1)

    root_index = 1
    left_child_index = 2 * root_index
    right_child_index = 2 * root_index + 1
    while left_child_index < len(heap.items) and right_child_index < len(heap.items) and ((heap.items[root_index] < heap.items[left_child_index]) or (heap.items[root_index] < heap.items[right_child_index])):
        if heap.items[left_child_index] > heap.items[right_child_index]:
            bigger_child = left_child_index
            heap.items[root_index], heap.items[bigger_child] = heap.items[bigger_child], heap.items[root_index]
            root_index *= 2
            left_child_index = 2 * root_index
            right_child_index = 2 * root_index + 1
        else:
            bigger_child = right_child_index
            heap.items[root_index], heap.items[bigger_child] = heap.items[bigger_child], heap.items[root_index]
            root_index = root_index * 2 + 1
            left_child_index = 2 * root_index
            right_child_index = 2 * root_index + 1
    else:
        if left_child_index < len(heap.items) and heap.items[root_index] < heap.items[left_child_index] and right_child_index >= len(heap.items):
            heap.items[root_index], heap.items[left_child_index] = heap.items[left_child_index], heap.items[root_index]
    return remove_largest


def peek(heap: MaxHeap) -> Any:
    if len(heap.items) == 1:
        raise IndexError
    else:
        return heap.items[1]


def size(heap: MaxHeap) -> Any:
    return len(heap.items) - 1


# NOTE: To be used for testing
def _contents(heap: MaxHeap) -> list[Any]:
    if len(heap.items) == 1:
        return []
    return heap.items[1:]


def heapify(lst: list[Any]) -> MaxHeap:
    heap = MaxHeap()
    heap.items += lst
    # TODO: Fix the heap property and return
    for i in range(len(heap.items)-1, 0, -1):
        parent = i
        left_child = (2 * i) 
        right_child = (2 * i) + 1
        while ((left_child < len(heap.items)
                and right_child < len(heap.items))
            and(heap.items[parent] < heap.items[left_child]
                or heap.items[parent] < heap.items[right_child])):
            if heap.items[left_child] > heap.items[right_child]:
                bigger_child = left_child 
                heap.items[parent], heap.items[bigger_child] = heap.items[bigger_child], heap.items[parent]
                parent *= 2
                left_child = 2 * parent
                right_child = 2 * parent + 1
            else:
                bigger_child = right_child
                heap.items[parent], heap.items[bigger_child] = heap.items[bigger_child], heap.items[parent]
                parent = parent * 2 + 1
                left_child = 2 * parent
                right_child = 2 * parent + 1
        if left_child < len(heap.items) and heap.items[parent] < heap.items[left_child] and right_child >= len(heap.items):
            heap.items[parent], heap.items[left_child] = heap.items[left_child], heap.items[parent]
    return heap


def heap_sort(lst: list[Any]) -> None:
    build_tree = heapify(lst)
    for i in range(len(lst) -1, -1, -1):
        big_value = dequeue(build_tree)
        lst[i] = big_value
