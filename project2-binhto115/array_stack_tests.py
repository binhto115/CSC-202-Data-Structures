from __future__ import annotations

import unittest

from array_stack import empty_stack, is_empty, peek, pop, push, size


class Tests(unittest.TestCase):

    def test_push_one_value(self) -> None:
        my_stack = empty_stack()
        push(my_stack, 10)
        self.assertEqual(my_stack.capacity, 4)
        self.assertEqual(my_stack.array[0], 10)
        self.assertEqual(my_stack.size, 1)

    def test_push_multiple_values(self) -> None:
        my_stack = empty_stack()
        push(my_stack, 1)
        push(my_stack, 2)
        push(my_stack, 3)
        push(my_stack, 4)
        self.assertEqual(my_stack.capacity, 4)
        self.assertEqual(my_stack.array[0], 1)
        self.assertEqual(my_stack.array[3], 4)
        self.assertEqual(my_stack.size, 4)

    def test_push_multiple_values_2(self) -> None:
        my_stack = empty_stack()
        push(my_stack, 1)
        push(my_stack, 2)
        push(my_stack, 3)
        push(my_stack, 4)
        push(my_stack, 5)
        push(my_stack, 6)
        self.assertEqual(my_stack.capacity, 8)
        self.assertEqual(my_stack.array[0], 1)
        self.assertEqual(my_stack.array[5], 6)
        self.assertEqual(my_stack.size, 6)

    def test_pop_a_value(self):
        my_stack = empty_stack()
        push(my_stack, 1)
        push(my_stack, 2)
        push(my_stack, 3)
        push(my_stack, 4)
        pop(my_stack)
        self.assertEqual(my_stack.size, 3)

    def test_pop_values(self):
        my_stack = empty_stack()
        push(my_stack, 1)
        push(my_stack, 2)
        push(my_stack, 3)
        push(my_stack, 4)
        push(my_stack, 5)
        pop(my_stack)
        pop(my_stack)
        self.assertEqual(my_stack.size, 3)

    def test_pop_empty_stack(self):
        my_stack = empty_stack()
        with self.assertRaises(IndexError):
            pop(my_stack)

    def test_peek_a_value(self):
        my_stack = empty_stack()
        push(my_stack, 1)
        push(my_stack, 2)
        push(my_stack, 3)
        self.assertEqual(peek(my_stack), 3)

    def test_peek_empty_stack(self):
        my_stack = empty_stack()
        with self.assertRaises(IndexError):
            peek(my_stack)

    def test_is_empty(self):
        my_stack = empty_stack()
        self.assertTrue(is_empty(my_stack))

    def test_is_empty2(self):
        my_stack = empty_stack()
        push(my_stack, 1)
        self.assertFalse(is_empty(my_stack))

    def test_size1(self):
        my_stack = empty_stack()
        push(my_stack, 1)
        push(my_stack, 2)
        self.assertEqual(size(my_stack), 2)

    def test_size2(self):
        my_stack = empty_stack()
        self.assertEqual(size(my_stack), 0)


if __name__ == "__main__":
    unittest.main()
