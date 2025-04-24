import unittest

from array_list import add, empty_list, get, length, remove, setitem


class Tests(unittest.TestCase):
    def test_length_empty_list(self) -> None:
        self.assertEqual(length(empty_list()), 0)

    def test_add_to_list1(self) -> None:
        my_list = empty_list()
        add(my_list, 0, "hello")
        self.assertEqual(my_list.array, ["hello"])

    def test_add_to_list2(self) -> None:
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        self.assertEqual(my_list.array, ["a", "b", "c", None])

    def test_add_to_list3(self):
        with self.assertRaises(IndexError):
            add(empty_list(), 1, 10)

    def test_add_to_list4(self):
        with self.assertRaises(IndexError):
            add(empty_list(), 10, 10)

    def test_add_to_list5(self) -> None:
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        self.assertEqual(my_list.array, ["a", "b", "c", "d"])

    def test_add_to_list6(self):
        my_list = empty_list()
        add(my_list, 0, "b")
        add(my_list, 0, "a")
        add(my_list, 1, "c")
        add(my_list, 1, 3)
        self.assertEqual(my_list.array, ["a", 3, "c", "b"])

    def test_doubling(self):
        my_list = empty_list()
        self.assertEqual(my_list.capacity, 1)

        add(my_list, 0, 10)
        self.assertEqual(my_list.capacity, 1)

        add(my_list, 0, 10)
        self.assertEqual(my_list.capacity, 2)

        add(my_list, 0, 10)
        self.assertEqual(my_list.capacity, 4)

        add(my_list, 0, 10)
        self.assertEqual(my_list.capacity, 4)

        add(my_list, 0, 10)
        self.assertEqual(my_list.capacity, 8)

    def test_length_list(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        self.assertEqual(my_list.size, 3)

    def test_length_list2(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        add(my_list, 4, "e")
        add(my_list, 5, "f")
        self.assertEqual(my_list.size, 6)

    def test_get_list(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        add(my_list, 4, "e")
        add(my_list, 5, "f")
        self.assertEqual(get(my_list, 0), "a")

    def test_get_list2(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        add(my_list, 4, "e")
        add(my_list, 5, "f")
        self.assertEqual(get(my_list, 3), "d")

    def test_get_list3(self):
        with self.assertRaises(IndexError):
            get(empty_list(), -1)

    def test_get_list4(self):
        with self.assertRaises(IndexError):
            get(empty_list(), 4)

    def test_get_list5(self):
        with self.assertRaises(IndexError):
            get(empty_list(), 10)

    def test_get_list6(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        self.assertEqual(get(my_list, 3), "d")

    def test_get_list7(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        with self.assertRaises(IndexError):
            get(my_list, 4)

    def test_setitem_list(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        add(my_list, 4, "e")
        add(my_list, 5, "f")
        setitem(my_list, 0, "ab")
        self.assertEqual(my_list.array,
                         ["ab", "b", "c", "d", "e", "f", None, None])

    def test_setitem_list2(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        add(my_list, 4, "e")
        add(my_list, 5, "f")
        setitem(my_list, 5, "ab")
        self.assertEqual(my_list.array,
                         ["a", "b", "c", "d", "e", "ab", None, None])

    def test_setitem_list3(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        add(my_list, 4, "e")
        add(my_list, 5, "f")
        setitem(my_list, 3, "ab")
        self.assertEqual(my_list.array,
                         ["a", "b", "c", "ab", "e", "f", None, None])

    def test_setitem_list4(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        add(my_list, 4, "e")
        add(my_list, 5, "f")
        with self.assertRaises(IndexError):
            setitem(my_list, 6, "ab")

    def test_setitem_list5(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        add(my_list, 3, "d")
        add(my_list, 4, "e")
        add(my_list, 5, "f")
        with self.assertRaises(IndexError):
            setitem(my_list, -1, "ab")

    def test_setitem_list6(self):
        with self.assertRaises(IndexError):
            setitem(empty_list(), -1, 10)

    def test_setitem_list7(self):
        with self.assertRaises(IndexError):
            setitem(empty_list(), 10, 10)

    def test_setitem_list8(self):
        with self.assertRaises(IndexError):
            setitem(empty_list(), 0, 10)

    def test_remove_list(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        (removed, my_list) = remove(my_list, 1)
        self.assertEqual(removed, "b")
        self.assertEqual(my_list.array, ["a", "c", None, None])

    def test_remove_list3(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        (removed, my_list) = remove(my_list, 0)
        self.assertEqual(removed, "a")
        self.assertEqual(my_list.array, ["b", "c", None, None])

    def test_remove_list7(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        (removed, my_list) = remove(my_list, 2)
        self.assertEqual(removed, "c")
        self.assertEqual(my_list.array, (["a", "b", None, None]))

    def test_remove_list4(self):
        with self.assertRaises(IndexError):
            remove(empty_list(), -1)

    def test_remove_list5(self):
        with self.assertRaises(IndexError):
            remove(empty_list(), 5)

    def test_remove_list6(self):
        with self.assertRaises(IndexError):
            remove(empty_list(), 0)

    def test_remove_list9(self):
        with self.assertRaises(IndexError):
            remove(empty_list(), -10)

    def test_remove_list10(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        with self.assertRaises(IndexError):
            remove(my_list, 3)

    def test_remove_list11(self):
        my_list = empty_list()
        add(my_list, 0, "a")
        add(my_list, 1, "b")
        add(my_list, 2, "c")
        with self.assertRaises(IndexError):
            remove(my_list, -1)


if __name__ == "__main__":
    unittest.main()
