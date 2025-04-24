from __future__ import annotations
from typing import Optional, TextIO
from ordered_list import OrderedList, insert, get, pop


class HuffmanNode:
    """A node in a Huffman tree.

    Attributes:
        char: The character as an integer ASCII value
        frequency: The frequency of the character in the file
        left: The left Huffman sub-tree
        right: The right Huffman sub-tree
    """

    def __init__(
        self, char: int, frequency: int, left: HuffmanTree, right: HuffmanTree
    ):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        """Return True if and only if self and other are equal."""
        return (
            isinstance(other, HuffmanNode) and
            self.char == other.char and
            self.frequency == other.frequency and
            self.left == other.left and
            self.right == other.right
        )

    def __lt__(self, other) -> bool:
        """Return True if and only if self < other."""
        return (
            self.frequency < other.frequency or
            self.frequency == other.frequency and self.char < other.char
        )

    def __repr__(self) -> str:
        return (
                "HuffmanNode(%r, %r, %r, %r)" % (self.char,
                                                 self.frequency,
                                                 self.left,
                                                 self.right)
        )


HuffmanTree = Optional[HuffmanNode]


def count_frequencies(file: TextIO) -> list[int]:
    """Read the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occured.
    """
    python_list = [0] * 256
    for line in file:
        for char in line:
            python_list[ord(char)] += 1
    return python_list


def build_huffman_tree(frequencies: list[int]) -> HuffmanTree:
    """Create a Huffman tree of the characters with non-zero frequency.

    Returns the root of the tree.
    """
    my_list = OrderedList()
    if frequencies == [0] * 256:
        return None
    for i in range(len(frequencies)):
        if frequencies[i] != 0:
            my_tree = HuffmanNode(i, frequencies[i], None, None)
            insert(my_list, my_tree)
    while my_list.size > 1:
        pop_first = pop(my_list, 0)
        pop_second = pop(my_list, 0)
        sum_frequency = pop_first.frequency + pop_second.frequency
        if pop_first.char < pop_second.char:
            new_node = HuffmanNode(pop_first.char, sum_frequency,
                                   pop_first, pop_second)
        else:
            new_node = HuffmanNode(pop_second.char, sum_frequency,
                                   pop_first, pop_second)
        insert(my_list, new_node)
    return get(my_list, 0)


def helper(tree: HuffmanTree, string_code: str, lst_of_chr: list[int]):
    if tree is None:
        return [""] * 256
    if tree.left is None and tree.right is None:
        lst_of_chr[(tree.char)] = string_code
    else:
        helper(tree.left, string_code + "0", lst_of_chr)
        helper(tree.right, string_code + "1", lst_of_chr)


def create_codes(tree: HuffmanTree) -> list[str]:
    """Traverse the tree creating the Huffman code for each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the Huffman code for that character.
    """
    lst = [''] * 256
    helper(tree, "", lst)
    return lst


def create_header(frequencies: list[int]) -> str:
    """Return the header for the compressed Huffman data.

    For example, given the file "aaabbbbcc", this would return:
    "97 3 98 4 99 2"
    """
    list_of_string = []
    for i in range(len(frequencies)):
        if frequencies[i] != 0:
            list_of_string.append(str(i))
            list_of_string. append(str(frequencies[i]))
    string = " ".join(list_of_string)
    return string


def huffman_encode(in_file: TextIO, out_file: TextIO) -> None:
    """Encode the data in the input file.

    This will write its result to the output file and won't return
    anything.
    """
    frequency = count_frequencies(in_file)
    in_file.seek(0)
    file_header = create_header(frequency)
    build_a_tree = build_huffman_tree(frequency)
    out_file.write(file_header + "\n")
    file_code = create_codes(build_a_tree)
    for line in in_file:
        for char in line:
            out_file.write(file_code[ord(char)])


def parse_header(header: str) -> list[int]:
    """
    This function takes the fist line of a file.

    This will return a list of frequencies
    """
    frequency_list = [0] * 256
    if header == "\n":
        return [0] * 256
    split_line = "".join(header.splitlines())
    split_var = split_line.split(" ")
    for i in range(0, len(split_var), 2):
        frequency_list[int(split_var[(i)])] = int(split_var[i + 1])
    return frequency_list


def huffman_decode(in_file: TextIO, out_file: TextIO) -> None:
    """
    This function decodes the data in the input file.

    This function will write the result to the output file and won't
    return anything
    """
    read_line = in_file.readline()
    parse_frequency = parse_header(read_line)
    build_tree = build_huffman_tree(parse_frequency)
    read_line_2 = in_file.readline()
    root = build_tree
    # Iterate through left and right
    for char in read_line_2:
        if char == "0":
            root = root.left
        elif char == "1":
            root = root.right
    # Write the code once encounters leaves
        if root.right is None and root.left is None:
            out_file.write(chr(root.char))
            root = build_tree
