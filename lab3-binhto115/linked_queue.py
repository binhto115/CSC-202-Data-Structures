from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, nxt: Optional[Node]) -> None:
        self.value = value
        self.next = nxt

    def __repr__(self) -> str:
        return "Node(%r, %r)" % (self.value, self.next)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Node)
            and self.value == other.value
            and self.next == other.next
        )


class LinkedQueue:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0


def empty_queue() -> LinkedQueue:
    return LinkedQueue()


def enqueue(queue: LinkedQueue, value: Any) -> None:
    if queue.tail is None:
        queue.head = Node(value, None)
        queue.tail = queue.head
    else:
        queue.tail.next = Node(value, None)
        queue.tail = queue.tail.next
    queue.size += 1


def dequeue(queue: LinkedQueue) -> Any:
    if queue.head is None or queue.size == 0:
        raise IndexError
    else:
        removed_value = queue.head.value
        queue.head = queue.head.next
        if queue.head is None:
            queue.tail = queue.head
        queue.size -= 1
        return removed_value


def peek(queue: LinkedQueue) -> Any:
    if queue.size == 0:
        raise IndexError
    else:
        return queue.head.value


def is_empty(queue: LinkedQueue) -> bool:
    if queue.tail is None or queue.head is None:
        return True
    else:
        return False


def size(queue: LinkedQueue) -> int:
    return queue.size
