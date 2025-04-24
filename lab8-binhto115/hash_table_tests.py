import unittest

from hash_table import (
    HashTable,
    _contents,
    contains,
    get_item,
    keys,
    remove,
    set_item,
    size,
    values,
)


def bad_hash(val) -> int:
    return 3


def identity_hash(x: int) -> int:
    return x

def identity_hash_power(x: int) -> int:
    return x ** 2

class Tests(unittest.TestCase):
    def test_hash_table_set_item_proto(self):
        ht = HashTable(identity_hash)
        set_item(ht, 0, "cat")
        set_item(ht, 0, "dog")
        set_item(ht, 1, "cow")
        self.assertEqual(_contents(ht), [[(0, "dog")], [(1, "cow")], [], [], []])

    def test_hash_table_set_item_proto_2(self):
        ht = HashTable(identity_hash)
        set_item(ht, 0, "cat")
        set_item(ht, 1, "cow")
        self.assertEqual(_contents(ht), [[(0, "cat")], [(1, "cow")], [], [], []])
        self.assertEqual(size(ht), 2)

    def test_hash_table_set_item_proto_3(self):
        ht = HashTable(identity_hash)
        set_item(ht, 0, "cat")
        set_item(ht, 0, "dog")
        set_item(ht, 1, "cow")
        self.assertEqual(keys(ht), [0 , 1])
        self.assertEqual(values(ht), ["dog", "cow"])
        self.assertEqual(get_item(ht, 0), "dog")
        self.assertEqual(_contents(ht), [[(0, "dog")], [(1, "cow")], [], [], []])
        self.assertEqual(size(ht), 2)    

    def test_hash_table_set_item_proto_4(self):
        ht = HashTable(identity_hash)
        set_item(ht, 0, "cat")
        set_item(ht, 1, "dog")
        set_item(ht, 2, "cow")
        set_item(ht, 3, "chicken")
        self.assertTrue(contains(ht, 0))
        self.assertFalse(contains(ht, 4))
        self.assertEqual(keys(ht), [0, 1, 2, 3])
        self.assertEqual(get_item(ht, 1), "dog")
        self.assertEqual(values(ht), ["cat", "dog", "cow", "chicken"])
        self.assertEqual(_contents(ht), [[(0, "cat")], [(1, "dog")], [(2, "cow")], [(3, "chicken")], []])
        self.assertEqual(size(ht), 4)

    def test_hash_table_set_item_proto_5(self):
        ht = HashTable(identity_hash)
        set_item(ht, 0, "a")
        set_item(ht, 5, "d")
        set_item(ht, 1, "b")
        set_item(ht, 4, "e")
        set_item(ht, 6, "f")
        set_item(ht, 3, "c")
        self.assertEqual(keys(ht), [0, 1, 3, 4, 5, 6])
        self.assertEqual(values(ht), ["a", "b", "c", "e", "d", "f"])
        self.assertEqual(get_item(ht, 3), "c")
        self.assertEqual(_contents(ht), [[(0, "a")], [(1, "b")], [], [(3, "c")], [(4, "e")], [(5, "d")], [(6, "f")], [], [], []])
        self.assertEqual(size(ht), 6)

    def test_hash_table_set_item_proto_6(self):
        ht = HashTable(identity_hash_power)
        set_item(ht, 0, "a")
        set_item(ht, 5, "d")
        set_item(ht, 1, "b")
        set_item(ht, 6, "f")
        set_item(ht, 4, "e")
        set_item(ht, 3, "c")
        self.assertEqual(keys(ht), [0, 1, 5, 6, 4, 3])
        self.assertEqual(values(ht), ["a", "b", "d", "f", "e", "c"])
        self.assertEqual(get_item(ht, 3), "c")
        self.assertEqual(_contents(ht), [[(0, "a")], [(1, "b")], [], [], [], [(5, "d")], [(6, "f"), (4, "e")], [], [], [(3, "c")]])
        self.assertEqual(size(ht), 6)

    def test_hash_table_empty(self) -> None:
        ht = HashTable(identity_hash)

        self.assertEqual(size(ht), 0)
        self.assertFalse(contains(ht, 0))
        self.assertCountEqual(keys(ht), [])
        self.assertCountEqual(values(ht), [])
        self.assertEqual(_contents(ht), [[], [], [], [], []])

    def test_hash_table_insert(self) -> None:
        ht = HashTable(identity_hash)
        set_item(ht, 0, "cat")

        self.assertEqual(get_item(ht, 0), "cat")
        self.assertEqual(size(ht), 1)
        self.assertTrue(contains(ht, 0))
        self.assertCountEqual(keys(ht), [0])
        self.assertCountEqual(values(ht), ["cat"])
        self.assertEqual(_contents(ht), [[(0, "cat")], [], [], [], []])

        # re-insert the same key
        set_item(ht, 0, "dog")

        self.assertEqual(get_item(ht, 0), "dog")
        self.assertEqual(size(ht), 1)
        self.assertTrue(contains(ht, 0))
        self.assertCountEqual(keys(ht), [0])
        self.assertCountEqual(values(ht), ["dog"])
        self.assertEqual(_contents(ht), [[(0, "dog")], [], [], [], []])

    def test_hash_table_remove(self) -> None:
        ht = HashTable(identity_hash)
        set_item(ht, 0, "cat")

        self.assertEqual(remove(ht, 0), (0, "cat"))

        self.assertEqual(size(ht), 0)
        self.assertFalse(contains(ht, 0))
        self.assertCountEqual(keys(ht), [])
        self.assertCountEqual(values(ht), [])
        self.assertEqual(_contents(ht), [[], [], [], [], []])

        with self.assertRaises(KeyError):
            get_item(ht, 0)

    def test_hash_table_remove_2(self) -> None:
        ht = HashTable(identity_hash)
        with self.assertRaises(KeyError):
            remove(ht, 0)

    def test_hash_table_remove_3(self) -> None:
        ht = HashTable(identity_hash)
        set_item(ht, 0, "a")
        set_item(ht, 5, "d")
        self.assertEqual(remove(ht, 5), (5, "d"))

    def test_hash_table_remove_4(self) -> None:
        ht = HashTable(identity_hash_power)
        set_item(ht, 0, "a")
        set_item(ht, 1, "b")
        set_item(ht, 5, "d")
        set_item(ht, 4, "e")
        set_item(ht, 6, "f")
        self.assertEqual(_contents(ht), [[(0, "a"), (5, "d")], [(1, "b"), (4, "e"), (6, "f")], [], [], []])
        self.assertEqual(remove(ht, 4), (4, "e"))
        self.assertEqual(_contents(ht), [[(0, "a"), (5, "d")], [(1, "b"), (6, "f")], [], [], []])

    def test_hash_table_remove_5(self) -> None:
        ht = HashTable(identity_hash)
        set_item(ht, 0, "a")
        set_item(ht, 5, "d")
        set_item(ht, 1, "b")
        set_item(ht, 4, "e")
        set_item(ht, 6, "f")
        self.assertEqual(_contents(ht), [[(0, "a"), (5, "d")], [(1, "b"), (6, "f")], [], [], [(4, "e")]])
        self.assertEqual(remove(ht, 0), (0, "a"))
        self.assertEqual(_contents(ht), [[(5, "d")], [(1, "b"), (6, "f")], [], [], [(4, "e")]])

    def test_hash_table_bad_hash_function(self) -> None:
        # Use a bad hashing function for the keys
        ht = HashTable(bad_hash)

        for i in range(5):
            set_item(ht, "k%d" % i, i)

        # All the keys are inserted into the chain at index 3
        self.assertEqual(
            _contents(ht),
            [
                [],
                [],
                [],
                [("k0", 0), ("k1", 1), ("k2", 2), ("k3", 3), ("k4", 4)],
                [],
            ],
        )


if __name__ == "__main__":
    unittest.main()
