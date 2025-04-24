import unittest

from heap import (
    MaxHeap,
    _contents,
    dequeue,
    enqueue,
    heap_sort,
    heapify,
    peek,
    size,
)


class Tests(unittest.TestCase):
    def test_heap_simple_operations(self):
        my_heap = MaxHeap()
        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

        enqueue(my_heap, 10)

        self.assertEqual(size(my_heap), 1)
        self.assertEqual(_contents(my_heap), [10])
        self.assertEqual(peek(my_heap), 10)

        self.assertEqual(dequeue(my_heap), 10)

        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

    def test_heap_operations(self):
        my_heap = MaxHeap()
        enqueue(my_heap, 46)
        enqueue(my_heap, 40)
        enqueue(my_heap, 46)
        enqueue(my_heap, 36)
        enqueue(my_heap, 14)
        enqueue(my_heap, 29)
        enqueue(my_heap, 10)
        enqueue(my_heap, 30)
        enqueue(my_heap, 30)
        enqueue(my_heap, 1)
        enqueue(my_heap, 13)
        enqueue(my_heap, 28)
        enqueue(my_heap, 47)
        enqueue(my_heap, 37)
        dequeue(my_heap)
        dequeue(my_heap)
        dequeue(my_heap)
        self.assertEqual(size(my_heap), 11)
        self.assertEqual(peek(my_heap), 40)
        self.assertEqual(_contents(my_heap), [40, 36, 37, 30, 14, 29, 10, 30, 28, 1, 13])

    def test_heapify_simple(self):
        my_heap = heapify([10, 20])
        self.assertEqual(size(my_heap), 2)
        self.assertEqual(_contents(my_heap), [20, 10])

    def test_heapify(self):
        my_heap = heapify([10, 20, 30, 40, 50, 60, 70])
        self.assertEqual(size(my_heap), 7)
        self.assertEqual(_contents(my_heap), [70, 50, 60, 40, 20, 10, 30])

    def test_heapify_2(self):
        my_heap = heapify([10, 20, 30, 40, 50, 60])
        self.assertEqual(size(my_heap), 6)
        self.assertEqual(_contents(my_heap), [60, 50, 30, 40, 20, 10])

    def test_heap_sort_simple(self):
        my_list = [20, 10]
        heap_sort(my_list)

        self.assertEqual(my_list, [10, 20])

    def test_heap_sort_simple_1(self):
        my_list = [10, 20]
        heap_sort(my_list)

        self.assertEqual(my_list, [10, 20])

    def test_heap_sort(self):
        my_list = [20, 10, 30, 50, 40, 60]
        heap_sort(my_list)

        self.assertEqual(my_list, [10, 20, 30, 40, 50, 60])

    def test_heap_sort_2(self):
        my_list = [20, 30, 50, 40, 60]
        heap_sort(my_list)

        self.assertEqual(my_list, [20, 30, 40, 50, 60])

    def test_heap_sort_3(self):
        my_list = []
        heap_sort(my_list)

        self.assertEqual(my_list, [])

    def test_heap_sort_4(self):
        my_list = [20]
        heap_sort(my_list)

        self.assertEqual(my_list, [20])

    def test_heap_sort_5(self):
        my_list = [20, 40, 60, 70, 90, 100, 30, 20, 10, 70, 80]
        heap_sort(my_list)

        self.assertEqual(my_list, [10, 20, 20, 30, 40, 60, 70, 70, 80, 90, 100])

    def test_peek_index_error(self):
        my_heap = MaxHeap()
        with self.assertRaises(IndexError):
            peek(my_heap)

    def test_dequeue_index_error(self):
        my_heap = MaxHeap()
        with self.assertRaises(IndexError):
            dequeue(my_heap)


if __name__ == "__main__":
    unittest.main()
