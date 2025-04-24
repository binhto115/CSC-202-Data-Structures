from __future__ import annotations

import unittest

from base_convert import convert


class Tests(unittest.TestCase):
    def test_conbert_base2_0(self):
        self.assertEqual(convert(0, 2), "0")

    def test_convert_base16_107(self):
        self.assertEqual(convert(107, 16), "6B")

    def test_convert_base16_2(self):
        self.assertEqual(convert(2, 16), "2")

    def test_convert_base4_30(self):
        self.assertEqual(convert(30, 4), "132")

    def test_convert_base16_54321(self):
        self.assertEqual(convert(54321, 16), "D431")

    def test_convert_base2_45(self):
        self.assertEqual(convert(45, 2), "101101")

    def test_convert_base16_316(self):
        self.assertEqual(convert(316, 16), "13C")


if __name__ == "__main__":
    unittest.main()
