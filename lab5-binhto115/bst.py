from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Optional


class TreeNode:
    def __init__(self, value: Any, left: BST, right: BST):
        self.value = value
        self.left = left
        self.right = right


    def __repr__(self) -> str:
        return "TreeNode(%r, %r, %r)" % (self.value, self.left, self.right)


    def __eq__(self, other) -> bool:
        return (
            isinstance(other, TreeNode) and
            self.value == other.value and
            self.left == other.left and
            self.right == other.right
        )


BST = Optional[TreeNode]


def is_empty(tree: BST) -> bool:
    """Return True if the tree is empty, False otherwise."""
    if tree is None:
        return True
    else:
        return False


def search(tree: BST, value: Any) -> bool:
    """Return True if value is in tree, False otherwise."""
    if tree is None:
        return False
    elif value < tree.value:
        return (value == tree.value or
            search(tree.left, value)
        )
    elif value >= tree.value:
        return (tree.value == value or
            search(tree.right, value)
        )


def insert(tree: BST, value: Any) -> BST:
    """Insert the value into the tree in the proper location."""
    if tree is None:
        return TreeNode(value, tree, tree)
    elif value < tree.value:
        if tree.left == None:
            tree.left = TreeNode(value, None, None)
        else:
            return TreeNode(tree.value, insert(tree.left, value), tree.right)
    elif value >= tree.value:
        if tree.right == None:
            tree.right = TreeNode(value, None, None)
        else:
            return TreeNode(tree.value, tree.left, insert(tree.right, value))
    return tree


def helper_find_smallest_of_biggest(tree: BST) -> int:
    go_right_once = tree.right
    while (go_right_once is not None and go_right_once.left is not None):
        go_right_once =  go_right_once.left
    return go_right_once.value


def delete(tree: BST, value: Any) -> BST:
    """Remove the value from the tree (if present).

    If the value is not present, this function does nothing; not returning 
    errors.
    """
    if tree is None:
        return None
    # Remove TreeNodes with one child
    elif tree.left is None and value == tree.value:
        tree = tree.right
    elif tree.right is None and value == tree.value:
        tree = tree.left
    # Remove TreeNodes with two children
    elif value == tree.value and tree.left is not None and tree.right is not None:
        tree.value = helper_find_smallest_of_biggest(tree)
        tree.right = delete(tree.right, tree.value)
    # Remove leaves O(log n) Removing leaves is easiest and fastest
    elif value < tree.value:
        return TreeNode(tree.value, delete(tree.left, value), tree.right)
    elif value >= tree.value:
        return TreeNode(tree.value, tree.left, delete(tree.right, value))
    return tree


def find_min(tree: BST) -> Any:
    """Return the smallest value in the tree."""
    if tree is None:
        raise ValueError
    while tree.left is not None:
        return find_min(tree.left)
    return tree.value


def find_max(tree: BST) -> Any:
    """Return the largest value in the tree."""
    if tree is None:
        raise ValueError
    while tree.right is not None:
        return find_max(tree.right)
    return tree.value


def height(tree: BST) -> int:
    """Return the height of the tree."""
    if tree is None:
        return -1
    count_left = height(tree.left)
    count_right = height(tree.right)
    if count_left > count_right:
        return count_left + 1
    else:
        return count_right + 1


def prefix_iterator(tree: BST) -> Iterator[Any]:
    """Return an iterator over the tree in prefix order."""
    if tree is not None:
        yield tree.value
        yield from prefix_iterator(tree.left)
        yield from prefix_iterator(tree.right)


def infix_iterator(tree: BST) -> Iterator[Any]:
    """Return an iterator over the tree in infix order."""
    if tree is not None:
        yield from infix_iterator(tree.left)
        yield tree.value
        yield from infix_iterator(tree.right)


def postfix_iterator(tree: BST) -> Iterator[Any]:
    """Return an iterator over the tree in postfix order."""
    if tree is not None:
        yield from postfix_iterator(tree.left)
        yield from postfix_iterator(tree.right)
        yield tree.value
