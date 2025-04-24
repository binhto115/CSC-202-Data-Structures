from __future__ import annotations

import unittest

from bears import bears


class Tests(unittest.TestCase):
    def test_bears_40(self):
        self.assertFalse(bears(40))

    def test_bears_42(self):
        self.assertTrue(bears(42))

    def test_bears_250(self):
        self.assertTrue(bears(250))

    def test_bears_53(self):
        self.assertFalse(bears(53))

    def test_bears_96(self):
        self.assertTrue(bears(96))

    def test_bears_90(self):
        self.assertFalse(bears(90))

    def test_bears_42_2__50(self):
        self.assertTrue(bears(42 * 2 ** 50))


if __name__ == "__main__":
    unittest.main()
