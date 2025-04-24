import io
import unittest

# NOTE: Do not import anything else from huffman.  If you do, your tests
# will crash when I test them.  You shouldn't need to test your helper
# functions directly, just via testing the required functions.
from huffman import (
    HuffmanNode,
    build_huffman_tree,
    count_frequencies,
    create_codes,
    create_header,
    huffman_encode,
)


class TestList(unittest.TestCase):
    def test_count_frequencies_01(self) -> None:
        # Create fake file to use for testing
        in_file = io.StringIO("ddddddddddddddddccccccccbbbbaaff")
        frequencies = count_frequencies(in_file)
        in_file.close()

        expected = [0] * 256
        expected[97:103] = [2, 4, 8, 16, 0, 2]

        self.assertEqual(frequencies, expected)

    # NOTE: This is the same test as count_frequencies_01 but with a
    # real file
    def test_count_frequencies_02(self) -> None:
        with open("file2.txt", encoding="utf8") as in_file:
            frequencies = count_frequencies(in_file)

        expected = [0] * 256
        expected[97:103] = [2, 4, 8, 16, 0, 2]

        self.assertEqual(frequencies, expected)

    def test_count_frequencies_03(self) -> None:
        in_file = io.StringIO("")
        frequencies = count_frequencies(in_file)
        in_file.close()

        self.assertEqual(frequencies, [0] * 256)

    def test_node_lt_01(self) -> None:
        node1 = HuffmanNode(97, 10, None, None)
        node2 = HuffmanNode(65, 20, None, None)

        self.assertLess(node1, node2)
        self.assertGreater(node2, node1)

    def test_build_huffman_tree_01(self) -> None:
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        huffman_tree = build_huffman_tree(frequencies)

        # NOTE: This also requires a working __eq__ for your HuffmanNode
        self.assertEqual(
            huffman_tree,
            HuffmanNode(
                97,
                15,
                HuffmanNode(97, 5, None, None),
                HuffmanNode(98, 10, None, None),
            ),
        )

    def test_build_huffman_tree_02(self) -> None:
        frequencies = [0] * 256
        huffman_tree = build_huffman_tree(frequencies)

        self.assertEqual(huffman_tree, None)

    def test_build_huffman_tree_03(self) -> None:
        in_file = io.StringIO("ddddddddddddddddccccccccbb")
        frequencies = count_frequencies(in_file)
        huffman_tree = build_huffman_tree(frequencies)
        self.assertEqual(
            huffman_tree,
            HuffmanNode(98, 26,
                        HuffmanNode(98, 10,
                                    HuffmanNode(98, 2, None, None),
                                    HuffmanNode(99, 8, None, None)),
                        HuffmanNode(100, 16, None, None))
        )

    def test_build_huffman_tree_04(self) -> None:
        in_file = io.StringIO("d")
        frequencies = count_frequencies(in_file)
        huffman_tree = build_huffman_tree(frequencies)
        self.assertEqual(huffman_tree, HuffmanNode(100, 1, None, None))

    def test_build_huffman_tree_05(self) -> None:
        in_file = io.StringIO("ddddddddddddddddccccccccbbaaff")
        frequencies = count_frequencies(in_file)
        huffman_tree = build_huffman_tree(frequencies)
        self.assertEqual(
            huffman_tree,
            HuffmanNode(97, 30,
                        HuffmanNode(97, 14,
                                    HuffmanNode(97, 6,
                                                HuffmanNode(102, 2,
                                                            None,
                                                            None),
                                                HuffmanNode(97, 4,
                                                            HuffmanNode(97, 2,
                                                                        None,
                                                                        None),
                                                            HuffmanNode(98, 2,
                                                                        None,
                                                                        None))
                                                ),
                                    HuffmanNode(99, 8, None, None)),
                        HuffmanNode(100, 16, None, None))
        )

    def test_create_codes_01(self) -> None:
        huffman_tree = HuffmanNode(
            97,
            15,
            HuffmanNode(97, 5, None, None),
            HuffmanNode(98, 10, None, None),
        )

        codes = create_codes(huffman_tree)
        self.assertEqual(create_codes(huffman_tree), codes)
        self.assertEqual(len(codes), 256)
        self.assertEqual(codes[ord("a")], "0")
        self.assertEqual(codes[ord("b")], "1")

    def test_create_codes_02(self) -> None:
        huffman_tree = HuffmanNode(
            97,
            15,
            HuffmanNode(97, 5, None, None),
            HuffmanNode(98, 10, None, None),
        )

        expected = [''] * 256
        expected[97:99] = ['0', '1']
        codes = create_codes(huffman_tree)
        self.assertEqual(len(codes), 256)
        self.assertEqual(codes, expected)

    def test_create_codes_03(self) -> None:
        huffman_tree = HuffmanNode(
            32,
            13,
            HuffmanNode(32, 6,
                        HuffmanNode(32, 3, None, None),
                        HuffmanNode(98, 3, None, None)),
            HuffmanNode(97, 7,
                        HuffmanNode(99, 3,
                                    HuffmanNode(100, 1, None, None),
                                    HuffmanNode(99, 2, None, None)),
                        HuffmanNode(97, 4, None, None)),
        )

        expected = [''] * 256
        expected[ord(' ')] = "00"
        expected[32:33] = ["00"]
        expected[97:101] = ['11', '01', '101', "100"]
        codes = create_codes(huffman_tree)
        self.assertEqual(len(codes), 256)
        self.assertEqual(codes, expected)

    def test_create_codes_04(self) -> None:
        huffman_tree = HuffmanNode(97, 5, None, None)
        expected = [''] * 256
        codes = create_codes(huffman_tree)
        self.assertEqual(len(codes), 256)
        self.assertEqual(codes, expected)

    def test_create_codes_05(self) -> None:
        huffman_tree = None
        expected = [''] * 256
        codes = create_codes(huffman_tree)
        self.assertEqual(len(codes), 256)
        self.assertEqual(codes, expected)

    def test_create_header_01(self) -> None:
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        self.assertEqual(create_header(frequencies), "97 5 98 10")

    def test_huffman_encode_01(self) -> None:
        # Create fake files to use for testing
        in_file = io.StringIO("abcd abc ab a")
        out_file = io.StringIO()

        huffman_encode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        correct_out_text = (
            "32 3 97 4 98 3 99 2 100 1\n11011011000011011010011010011"
        )

        self.assertEqual(result, correct_out_text)

    # NOTE: This is the same test as encode_01, but with real files
    def test_huffman_encode_02(self) -> None:
        out_file = io.StringIO()

        with open("file1.txt", encoding="utf8") as in_file:
            huffman_encode(in_file, out_file)

        result = out_file.getvalue()
        out_file.close()

        with open("file1_encoded.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_huffman_encode_03(self) -> None:
        # Create fake files to use for testing
        in_file = io.StringIO("aaaaa")
        out_file = io.StringIO()

        huffman_encode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        correct_out_text = (
            "97 5\n"
        )

        self.assertEqual(result, correct_out_text)

    def test_huffman_encode_04(self) -> None:
        # Create fake files to use for testing
        in_file = io.StringIO("")
        out_file = io.StringIO()

        huffman_encode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        correct_out_text = ("\n")

        self.assertEqual(result, correct_out_text)

    def test_huffman_encode_05(self) -> None:
        out_file = io.StringIO()

        with open("multiline.txt", encoding="utf8") as in_file:
            huffman_encode(in_file, out_file)

        result = out_file.getvalue()
        out_file.close()

        with open("multiline_encoded.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_huffman_encode_06(self) -> None:
        out_file = io.StringIO()

        with open("declaration.txt", encoding="utf8") as in_file:
            huffman_encode(in_file, out_file)

        result = out_file.getvalue()
        out_file.close()

        with open("declaration_encoded.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_huffman_encode_07(self) -> None:
        # Create fake files to use for testing
        in_file = io.StringIO("a")
        out_file = io.StringIO()

        huffman_encode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        correct_out_text = (
            "97 1\n"
        )

        self.assertEqual(result, correct_out_text)


if __name__ == "__main__":
    unittest.main()
