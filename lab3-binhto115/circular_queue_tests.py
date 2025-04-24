from __future__ import annotations

import unittest

from circular_queue import dequeue, empty_queue, enqueue, is_empty, peek, size


class Tests(unittest.TestCase):
    def test_enqueue_one_value(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)

        self.assertEqual(my_queue.capacity, 4)
        self.assertEqual(my_queue.array[0], 10)
        self.assertEqual(my_queue.start, 0)
        self.assertEqual(my_queue.size, 1)

    def test_enqueue_multiple_values(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        self.assertEqual(my_queue.capacity, 4)
        self.assertEqual(my_queue.array[0], 10)
        self.assertEqual(my_queue.start, 0)
        self.assertEqual(my_queue.size, 3)

    def test_enqueue_multiple_values_2(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        enqueue(my_queue, 40)
        enqueue(my_queue, 50)
        self.assertEqual(my_queue.capacity, 8)
        self.assertEqual(my_queue.array[0], 10)
        self.assertEqual(my_queue.start, 0)
        self.assertEqual(my_queue.size, 5)

    def test_enqueue_multiple_values_3(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        enqueue(my_queue, 40)
        dequeue(my_queue)
        dequeue(my_queue)
        enqueue(my_queue, 50)
        enqueue(my_queue, 60)
        enqueue(my_queue, 70)
        self.assertEqual(my_queue.capacity, 8)
        self.assertEqual(my_queue.array[0], 30)
        self.assertEqual(my_queue.start, 0)
        self.assertEqual(my_queue.size, 5)

    def test_dequeue_one_value(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        enqueue(my_queue, 50)
        dequeue(my_queue)
        self.assertEqual(my_queue.capacity, 4)
        self.assertEqual(my_queue.array[0], None)
        self.assertEqual(my_queue.start, 1)
        self.assertEqual(my_queue.size, 3)

    def test_dequeue_multiple_values(self) -> None:
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        enqueue(my_queue, 50)
        enqueue(my_queue, 60)
        enqueue(my_queue, 70)
        dequeue(my_queue)
        dequeue(my_queue)
        self.assertEqual(my_queue.capacity, 8)
        self.assertEqual(my_queue.array[0], None)
        self.assertEqual(my_queue.start, 2)
        self.assertEqual(my_queue.size, 4)

    def test_dequeue_empty_queue(self):
        my_queue = empty_queue()
        with self.assertRaises(IndexError):
            dequeue(my_queue)

    def test_peek_queue(self):
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        enqueue(my_queue, 50)
        enqueue(my_queue, 60)
        enqueue(my_queue, 70)
        self.assertEqual(peek(my_queue), 10)

    def test_peek_queue_2(self):
        my_queue = empty_queue()
        with self.assertRaises(IndexError):
            peek(my_queue)

    def test_is_empty(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))

    def test_is_empty_2(self):
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        self.assertFalse(is_empty(my_queue))

    def test_size(self):
        my_queue = empty_queue()
        enqueue(my_queue, 10)
        enqueue(my_queue, 20)
        enqueue(my_queue, 30)
        self.assertEqual(size(my_queue), 3)

    def test_size_2(self):
        my_queue = empty_queue()
        self.assertEqual(size(my_queue), 0)


if __name__ == "__main__":
    unittest.main()
