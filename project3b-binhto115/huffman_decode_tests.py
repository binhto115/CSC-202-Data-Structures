import io
import unittest

# NOTE: Similar to part a, do not import anything else from huffman.
from huffman import huffman_decode, parse_header


class TestList(unittest.TestCase):
    def test_parse_header_01(self):
        header = "97 2 98 4 99 8 100 16 102 2\n"

        frequencies = parse_header(header)
        expected = [0] * 256
        expected[97:103] = [2, 4, 8, 16, 0, 2]

        self.assertEqual(frequencies, expected)

    def test_parse_header_02(self):
        header = "32 1\n"

        frequencies = parse_header(header)
        expected = [0] * 256
        expected[32:33] = [1]

        self.assertEqual(frequencies, expected)

    def test_huffman_decode_01(self):
        in_file = io.StringIO(
            "32 3 97 4 98 3 99 2 100 1\n11011011000011011010011010011"
        )
        out_file = io.StringIO()

        huffman_decode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        self.assertEqual(result, "abcd abc ab a")

    # NOTE: This is the same test as decode_01, but with real files
    def test_huffman_decode_02(self):
        out_file = io.StringIO()

        with open("file1_encoded.txt", encoding="utf8") as in_file:
            huffman_decode(in_file, out_file)

        result = out_file.getvalue()
        out_file.close()

        with open("file1.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_huffman_decode_03(self):
        out_file = io.StringIO()

        with open("multiline_encoded.txt", encoding="utf8") as in_file:
            huffman_decode(in_file, out_file)

        result = out_file.getvalue()
        out_file.close()

        with open("multiline.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_huffman_decode_04(self):
        out_file = io.StringIO()

        with open("declaration_encoded.txt", encoding="utf8") as in_file:
            huffman_decode(in_file, out_file)

        result = out_file.getvalue()
        out_file.close()

        with open("declaration.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_huffman_decode_05(self):
        in_file = io.StringIO("\n")
        out_file = io.StringIO()

        huffman_decode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        self.assertEqual(result, "")

    def test_huffman_decode_06(self):
        in_file = io.StringIO("32 3\n")
        out_file = io.StringIO()

        huffman_decode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()
