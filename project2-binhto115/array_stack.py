from __future__ import annotations

from typing import Any


class ArrayStack:
    def __init__(self) -> None:
        self.capacity = 4
        self.array: list[Any] = [None] * self.capacity
        self.size = 0


def empty_stack() -> ArrayStack:
    return ArrayStack()


def push(stack: ArrayStack, value: Any) -> None:
    """This function adds the given value into the stack"""
    if stack.size == stack.capacity:
        new_stack = [None] * (2 * stack.capacity)
        for i in range(0, stack.size):
            new_stack[i] = stack.array[i]
        stack.array = new_stack
        stack.capacity = stack.capacity * 2
    stack.array[stack.size] = value
    stack.size += 1


def pop(stack: ArrayStack) -> Any:
    """
    This function removes the top value of the stack. In terms of a list,
    this funtion removes the value at the end of a list.
    """
    if stack.size == 0:
        raise IndexError
    else:
        value = stack.array[stack.size - 1]
        stack.array[stack.size - 1] = None
    stack.size -= 1
    return value


def peek(stack: ArrayStack) -> Any:
    """
    This function takes a look at the top of the stack
    in terms of the end of the list.
    """
    if stack.size == 0:
        raise IndexError
    else:
        return stack.array[stack.size - 1]


def is_empty(stack: ArrayStack) -> bool:
    """
    This function takes a stack as argument and checks whether it is
    empty or not.
    """
    if stack.size == 0:
        return True
    else:
        return False


def size(stack: ArrayStack) -> int:
    """
    This function takes a stack in and returns a number that represents
    the number of items in the stack.
    """
    return stack.size
