import unittest

from bst import (
    TreeNode,
    delete,
    find_max,
    find_min,
    height,
    insert,
    is_empty,
    search,
)


class Tests(unittest.TestCase):
    def test_is_empty(self):
        self.assertTrue(is_empty(None))

    def test_is_not_empty(self):
        my_tree = TreeNode(50,
        TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
        TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(150, None, TreeNode(200, None, None))))
        self.assertFalse(is_empty(my_tree))

    def test_height_empty(self):
        self.assertEqual(height(None), -1)

    def test_search_empty(self):
        self.assertFalse(search(None, 10))

    def test_delete_empty(self):
        self.assertEqual(delete(None, 10), None)

    def test_insert_empty(self):
        self.assertEqual(insert(None, 10), TreeNode(10, None, None))

    def test_search_root(self):
        self.assertTrue(search(TreeNode(10, None, None), 10))

    def test_find_min_root(self):
        self.assertEqual(find_min(TreeNode(10, None, None)), 10)

    def test_find_min_none(self):
        with self.assertRaises(ValueError):
            find_min(None)
    
    def test_find_m_naxone(self):
        with self.assertRaises(ValueError):
            find_max(None)

    def test_find_max_root(self):
        self.assertEqual(find_max(TreeNode(10, None, None)), 10)

    def test_search_left(self):
        my_tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
            TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)),
        )
        self.assertTrue(search(my_tree, 1))

    def test_insert_1(self):
        my_tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
            TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)),
        )
        insert(my_tree, 10)
        self.assertEqual(my_tree, TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
            TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, TreeNode(10, None, None))),)
        )
    def test_insert_2(self):
        my_tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
            TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)),
        )
        self.assertEqual(insert(my_tree, 2), TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, TreeNode(2, None, None), None)),
            TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None))))

    def test_delete_leaves(self):
        my_tree = TreeNode(50,
                TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(150, None, TreeNode(200, None, None))))

        self.assertEqual(delete(my_tree, 70), TreeNode(50,
                TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, None), TreeNode(150, None, TreeNode(200, None, None)))))

    def test_delete_leaves_2(self):
        my_tree = TreeNode(50,
            TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
            TreeNode(100, TreeNode(60, None, None), None))

        self.assertEqual(delete(my_tree, 35), TreeNode(50,
            TreeNode(40, None, TreeNode(45, None, None)), 
            TreeNode(100, TreeNode(60, None, None), None)))

    def test_delete_leaves_3(self):
        my_tree = TreeNode(50,
            TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
            TreeNode(100, TreeNode(60, None, None), None))

        self.assertEqual(delete(my_tree, 60), TreeNode(50,
            TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
            TreeNode(100, None, None)))

    def test_delete_leaves_4(self):
        my_tree = TreeNode(50,
            TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
            TreeNode(100, None, TreeNode(120, None, None)))

        self.assertEqual(delete(my_tree, 120), TreeNode(50,
            TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
            TreeNode(100, None, None)))

    def test_delete_nodes_w_one_children_1(self):
        my_tree = TreeNode(50,
                TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(150, None, TreeNode(200, None, None))))
        self.assertEqual(delete(my_tree, 60), TreeNode(50, 
                        TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                        TreeNode(100, TreeNode(70, None, None), TreeNode(150, None, TreeNode(200, None, None))))
        )

    def test_delete_nodes_w_one_children_2(self):
        my_tree = TreeNode(50,
                TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(150, None, TreeNode(200, None, None))))

        self.assertEqual(delete(my_tree, 150), TreeNode(50,
                TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(200, None, None)))
        )

    def test_delete_nodes_w_one_children_3(self):
        my_tree = TreeNode(50,
                TreeNode(40, TreeNode(35, TreeNode(25, None, None), None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(150, None, TreeNode(200, None, None))))

        self.assertEqual(delete(my_tree, 35), TreeNode(50,
                TreeNode(40, TreeNode(25, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(150, None, TreeNode(200, None, None))))
        )

    def test_delete_nodes_w_two_children_1(self):
        my_tree = TreeNode(50,
                TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(150, None, TreeNode(200, None, None))))

        self.assertEqual(delete(my_tree, 40), TreeNode(50,
                TreeNode(45, TreeNode(35, None, None), None), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)), TreeNode(150, None, TreeNode(200, None, None))))
        )

    def test_delete_nodes_w_two_children_2(self):
        my_tree = TreeNode(50,
                TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(60, None, TreeNode(70, None, None)),
                         TreeNode(150, None, TreeNode(200, None, None))))

        self.assertEqual(delete(my_tree, 50), TreeNode(60,
                TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)), 
                TreeNode(100, TreeNode(70, None, None), TreeNode(150, None, TreeNode(200, None, None))))
        )

    def test_find_min(self):
        my_tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
            TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)),
        )
        self.assertEqual(find_min(my_tree), 1)

    def test_find_max(self):
        my_tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
            TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)),
        )
        self.assertEqual(find_max(my_tree), 7)

    def test_find_height(self):
        my_tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
            TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)),
        )
        self.assertEqual(height(my_tree), 2)

    def test_find_height_2(self):
        my_tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
            TreeNode(6, TreeNode(5, None, None), None),
        )

        self.assertEqual(height(my_tree), 2)

    def test_find_height_3(self):
        my_tree = TreeNode(50,
        TreeNode(40, TreeNode(35, None, None), TreeNode(45, None, None)),
            TreeNode(100, TreeNode(60, None, None),
            TreeNode(150, None, TreeNode(200, None, None)))
        )
        self.assertEqual(height(my_tree), 3)


if __name__ == "__main__":
    unittest.main()
