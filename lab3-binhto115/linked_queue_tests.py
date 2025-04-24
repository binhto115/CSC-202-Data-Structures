from __future__ import annotations

import unittest

from linked_queue import (
    Node,
    dequeue,
    empty_queue,
    enqueue,
    is_empty,
    peek,
    size,
)


class Tests(unittest.TestCase):
    def test_enqueue_one_value(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)

        self.assertEqual(my_queue.head, Node(10, None))
        self.assertEqual(my_queue.tail, Node(10, None))
        self.assertEqual(my_queue.size, 1)

    def test_enqueue_multiple_values(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)

        self.assertEqual(my_queue.head, Node(10, Node(20, Node(30, None))))
        self.assertEqual(my_queue.tail, Node(30, None))
        self.assertEqual(my_queue.size, 3)

    def test_dequeue_one_value(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        dequeue(my_queue)

        self.assertEqual(my_queue.head, Node(20, Node(30, None)))
        self.assertEqual(my_queue.tail, Node(30, None))
        self.assertEqual(my_queue.size, 2)

    def test_dequeue_multiple_values(self):
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        dequeue(my_queue)
        dequeue(my_queue)

        self.assertEqual(my_queue.head, Node(30, None))
        self.assertEqual(my_queue.tail, Node(30, None))
        self.assertEqual(my_queue.size, 1)

    def test_dequeue_empty_queue(self):
        my_queue = empty_queue()
        with self.assertRaises(IndexError):
            dequeue(my_queue)

    def test_dequeue_multiple_values_2(self):
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        self.assertEqual(dequeue(my_queue), 10)

    def test_peek_queue(self):
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)

        self.assertEqual(peek(my_queue), 10)

    def test_peek_empty_queue(self):
        my_queue = empty_queue()
        with self.assertRaises(IndexError):
            peek(my_queue)

    def test_is_empty(self):
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)

        self.assertFalse(is_empty(my_queue))

    def test_is_empty_2(self):
        my_queue = empty_queue()

        self.assertTrue(is_empty(my_queue))

    def test_size(self):
        my_queue = empty_queue()

        self.assertEqual(size(my_queue), 0)

    def test_size_2(self):
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)

        self.assertEqual(size(my_queue), 2)


if __name__ == "__main__":
    unittest.main()
