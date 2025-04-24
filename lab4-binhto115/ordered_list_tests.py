import unittest

from ordered_list import (
    OrderedList,
    contains,
    get,
    index_of,
    insert,
    is_empty,
    pop,
    remove,
    size,
)


class Tests(unittest.TestCase):
    def test_simple(self) -> None:
        my_list = OrderedList()

        self.assertEqual(size(my_list), 0)
        self.assertTrue(is_empty(my_list))

        insert(my_list, 10)
        insert(my_list, 20)
        self.assertEqual(index_of(my_list, 10), 0)
        self.assertEqual(index_of(my_list, 20), 1)

        insert(my_list, 30)
        self.assertEqual(size(my_list), 3)
        self.assertTrue(contains(my_list, 30))
        self.assertFalse(is_empty(my_list))
        self.assertEqual(get(my_list, 0), 10)

        insert(my_list, 25)
        insert(my_list, 15)
        self.assertEqual(get(my_list, 2), 20)
        self.assertEqual(index_of(my_list, 25), 3)
        self.assertTrue(contains(my_list, 25))

        insert(my_list, 40)
        self.assertEqual(index_of(my_list, 40), 5)

        insert(my_list, 5)
        self.assertEqual(index_of(my_list, 5), 0)

        self.assertEqual(size(my_list), 7)

        remove(my_list, 10)

        self.assertEqual(size(my_list), 6)
        self.assertFalse(contains(my_list, 10))
        self.assertFalse(is_empty(my_list))

        insert(my_list, 10)

        self.assertEqual(pop(my_list, 1), 10)
        self.assertFalse(contains(my_list, 10))

    def test_remove_value_error(self):
        my_list = OrderedList()
        with self.assertRaises(ValueError):
            remove(my_list, 10)

    def test_remove_value_error_2(self):
        my_list = OrderedList()
        with self.assertRaises(ValueError):
            remove(my_list, None)

    def test_pop_index_error(self):
        my_list = OrderedList()
        with self.assertRaises(IndexError):
            pop(my_list, 1)

    def test_index_of_value_error_1(self):
        my_list = OrderedList()
        with self.assertRaises(ValueError):
            index_of(my_list, 1)

    def test_index_of_value_error_2(self):
        my_list = OrderedList()
        with self.assertRaises(ValueError):
            index_of(my_list, -1)

    def test_index_of_value_error_3(self):
        my_list = OrderedList()
        insert(my_list, 10)
        with self.assertRaises(ValueError):
            index_of(my_list, 0)

    def test_get_value_error_3(self):
        my_list = OrderedList()
        with self.assertRaises(IndexError):
            get(my_list, 10)

    def test_get_index_error(self):
        my_list = OrderedList()
        with self.assertRaises(IndexError):
            get(my_list, -1)

    def test_get_index_error_2(self):
        my_list = OrderedList()
        with self.assertRaises(IndexError):
            get(my_list, 1)

    def test_pop_index_error_3(self):
        my_list = OrderedList()
        insert(my_list, 10)
        with self.assertRaises(IndexError):
            get(my_list, 1)

    def test_pop_index_error_4(self):
        my_list = OrderedList()
        insert(my_list, 10)
        with self.assertRaises(IndexError):
            get(my_list, -1)

    def test_pop_index_error_5(self):
        my_list = OrderedList()
        with self.assertRaises(IndexError):
            get(my_list, 0)


if __name__ == "__main__":
    unittest.main()
