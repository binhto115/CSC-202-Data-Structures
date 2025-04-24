from __future__ import annotations

from typing import Any


class CircularQueue:
    def __init__(self) -> None:
        self.capacity = 4
        self.array: list[Any] = [None] * self.capacity
        self.start = 0
        self.size = 0


def empty_queue() -> CircularQueue:
    return CircularQueue()


def enqueue(queue: CircularQueue, value: Any) -> None:
    if queue.size == queue.capacity:
        new_queue = [None] * (2 * queue.capacity)
        for i in range(0, queue.size):
            new_queue[i] = queue.array[(queue.start + i) % queue.capacity]
        queue.array = new_queue
        queue.capacity = queue.capacity * 2
        queue.start = 0
    queue.array[(queue.start + queue.size) % queue.capacity] = value
    queue.size += 1


def dequeue(queue: CircularQueue) -> Any:
    if queue.size == 0:
        raise IndexError
    else:
        removed_value = queue.array[queue.start]
        queue.array[queue.start] = None
        queue.start = queue.start + 1
        queue.size -= 1
        return removed_value


def peek(queue: CircularQueue) -> Any:
    if queue.array[queue.start] is None or queue.size == 0:
        raise IndexError
    else:
        return queue.array[queue.start]


def is_empty(queue: CircularQueue) -> bool:
    if queue.size == 0:
        return True
    else:
        return False


def size(queue: CircularQueue) -> int:
    return queue.size
