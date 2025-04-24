import unittest

from linked_list import Node, add, empty_list, get, length, remove, setitem


class Tests(unittest.TestCase):
    def test_repr(self) -> None:
        lst = Node(1, None)
        self.assertEqual(
            str(lst),
            "Node(1, None)"
        )

    def test_empty_list(self) -> None:
        self.assertEqual(empty_list(), None)

    def test_add_empty_list(self):
        # NOTE: You will need to efine __eq__ in your Node class for
        # this test to pass.
        self.assertEqual(
            add(empty_list(), 0, "hello"),
            Node("hello", None),
        )

    def test_add_list_1(self):
        with self.assertRaises(IndexError):
            add(empty_list(), 1, "World")

    def test_add_list_2(self):
        with self.assertRaises(IndexError):
            add(Node(0, Node(1, Node(2, Node(3, None)))), -1, 40),

    def test_add_list_3(self):
        self.assertEqual(
            add(Node(0, Node(1, Node(2, Node(3, None)))), 0, 40),
            Node(40, Node(0, Node(1, Node(2, Node(3, None))))),
        )

    def test_add_list_4(self):
        self.assertEqual(
            add(Node(0, Node(1, Node(2, Node(3, None)))), 3, 40),
            Node(0, Node(1, Node(2, Node(40, Node(3, None))))),
        )

    def test_add_list_5(self):
        self.assertEqual(
            add(Node(0, Node(1, Node(2, Node(3, None)))), 4, 40),
            Node(0, Node(1, Node(2, Node(3, Node(40, None)))))
        )

    def test_add_list_6(self):
        with self.assertRaises(IndexError):
            add(Node(0, Node(1, Node(2, Node(3, None)))), 5, 40)

    def test_add_list_7(self):
        self.assertEqual(
            add(Node(0, Node(1, Node(2, Node(3, None)))), 2, 40),
            Node(0, Node(1, Node(40, Node(2, Node(3, None)))))
            )

    def test_length_empty_list(self) -> None:
        self.assertEqual(
            length(empty_list()),
            0,
        )

    def test_length_list(self):
        self.assertEqual(
            length(Node(1, Node(2, Node(3, None)))),
            3,
        )

    def test_length_list_2(self):
        self.assertEqual(
            length(Node(1, Node(2, Node(3, Node(4, Node(5, None)))))),
            5,
        )

    def test_length_list_3(self):
        self.assertEqual(
            length(Node(1, Node(2, Node(3, Node(4, Node(5,
                   Node(6, Node(7, None)))))))),
            7,
        )

    def test_get_from_empty_list(self):
        with self.assertRaises(IndexError):
            get(None, 0)

    def test_get_from_empty_list_2(self):
        with self.assertRaises(IndexError):
            get(None, -2)

    def test_get_from_empty_list_3(self):
        with self.assertRaises(IndexError):
            get(None, 2)

    def test_get_list(self):
        self.assertEqual(
            get(Node(1, Node("Hello", Node(3, Node(4, Node(5, None))))), 1),
            "Hello"
        )

    def test_get_list_2(self):
        self.assertEqual(
            get(Node(1, Node("Hello", Node(3, Node(4, Node(5, None))))), 0),
            1
        )

    def test_get_list_3(self):
        self.assertEqual(
            get(Node(1, Node("Hello", Node(3, Node(4, Node(5, None))))), 4),
            5
        )

    def test_get_list_4(self):
        self.assertEqual(
            get(Node(1, Node("Hello", Node(3, Node(4, Node(5, None))))), 3),
            4
        )

    def test_get_list_5(self):
        with self.assertRaises(IndexError):
            get(Node(1, Node(2, Node(3, None))), -2)

    def test_get_list_6(self):
        with self.assertRaises(IndexError):
            get(Node(1, Node("Hello", Node(3, Node(4, Node(5, None))))), 5)

    def test_setitem_empty_list(self):
        with self.assertRaises(IndexError):
            setitem(None, 0, 104)

    def test_setitem_empty_list_2(self):
        with self.assertRaises(IndexError):
            setitem(None, 1, 104)

    def test_setitem_empty_list_3(self):
        with self.assertRaises(IndexError):
            setitem(None, -1, 105)

    def test_setitem_list(self):
        with self.assertRaises(IndexError):
            setitem(Node(1, Node(2, Node(3, None))), 4, 10)

    def test_setitem_list_2(self):
        self.assertEqual(
            setitem(Node(1, Node(4, Node(3, Node(4, None)))), 1, 2),
            Node(1, Node(2, Node(3, Node(4, None))))
        )

    def test_setitem_list_3(self):
        self.assertEqual(
            setitem(Node(1, Node(2, Node(3, None))), 2, 10),
            Node(1, Node(2, Node(10, None)))
        )

    def test_setitem_list_4(self):
        self.assertEqual(
            setitem(Node(1, Node(2, Node(3, None))), 0, 10),
            Node(10, Node(2, Node(3, None)))
        )

    def test_setitem_list_5(self):
        with self.assertRaises(IndexError):
            setitem(Node(1, Node(2, Node(3, None))), -3, 10)

    def test_remove_empty_list(self):
        with self.assertRaises(IndexError):
            remove(None, 1)

    def test_remove_empty_list_2(self):
        with self.assertRaises(IndexError):
            remove(None, 0)

    def test_remove_list(self):
        with self.assertRaises(IndexError):
            remove(Node(1, Node(2, Node(3, None))), 6)

    def test_remove_list_1(self):
        self.assertEqual(
            remove(Node(1, Node(3, Node(2, None))), 1),
            (3, Node(1, Node(2, None)))
            )

    def test_remove_list_2(self):
        self.assertEqual(
            remove(Node(1, Node(2, Node(3, None))), 2),
            (3, Node(1, Node(2, None)))
            )

    def test_remove_list_3(self):
        self.assertEqual(
            remove(Node(1, Node(2, Node(3, None))), 0),
            (1, Node(2, Node(3, None)))
        )

    def test_remove_list_4(self):
        with self.assertRaises(IndexError):
            remove(Node(1, Node(2, Node(3, None))), -4)


if __name__ == "__main__":
    unittest.main()
