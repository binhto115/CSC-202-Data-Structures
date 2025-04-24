import unittest

# NOTE: Do not add more imports
from sorts import insertion_sort, merge_sort, selection_sort


class Tests(unittest.TestCase):
    def test_merge_sort_01(self):
        lst = [10]

        # Sorting an singleton list should do no comparisons
        self.assertEqual(merge_sort(lst), 0)

        # The list shouldn't change
        self.assertEqual(lst, [10])

    def test_merge_sort_02(self):
        lst = [50, 60, 10, 20, 80, 40, 30, 70]

        merge_sort(lst)

        # The list should now be sorted
        self.assertEqual(lst, [10, 20, 30, 40, 50, 60, 70, 80])

    def test_selection_sort_01(self):
        lst = [50, 20, 30, 100, 60, 40]
        selection_sort(lst)
        self.assertEqual(lst, [20, 30, 40, 50, 60, 100])

    def test_selection_sort_02(self):
        lst = [100, 20, 10, 40, 10, 70, 80, 90, 30]
        selection_sort(lst)
        self.assertEqual(lst, [10, 10, 20, 30, 40, 70, 80, 90, 100])

    def test_selection_sort_03(self):
        lst = [1, 2, 3, 4, 5]
        selection_sort(lst)
        self.assertEqual(lst, [1, 2, 3, 4 ,5])

    def test_selection_sort_04(self):
        lst = [2, 1]
        self.assertEqual(selection_sort(lst), 1)

    def test_insertion_sort_01(self):
        lst = [100, 20, 10, 40, 10, 70, 80, 90, 30]
        insertion_sort(lst)
        self.assertEqual(lst, [10, 10, 20, 30, 40, 70, 80, 90, 100])

    def test_insertion_sort_02(self):
        lst = [100, 20, 10, 40, 10, 70, 80, 90, 30]
        insertion_sort(lst)
        self.assertEqual(lst, [10, 10, 20, 30, 40, 70, 80, 90, 100])


if __name__ == "__main__":
    unittest.main()
