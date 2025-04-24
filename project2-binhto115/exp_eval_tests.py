from __future__ import annotations

import unittest

from exp_eval import infix_to_postfix, postfix_eval


class Tests(unittest.TestCase):
    def test_postfix_eval_01(self):
        # NOTE: When testing for equality between values that could be
        # floats, we should use assertAlmostEqual
        self.assertAlmostEqual(postfix_eval("1 2 +"), 3)

    def test_postfix_eval_02(self):
        self.assertEqual(postfix_eval("5 1 2 + 4 ^ + 3 -"), 83)

    def test_postfix_eval_03(self):
        self.assertEqual(postfix_eval("5 1 *"), 5)

    def test_postfix_eval_04(self):
        self.assertEqual(postfix_eval("5 5 /"), 1)

    def test_postfix_eval_05(self):
        self.assertEqual(postfix_eval("4 2 -"), 2)

    def test_postfix_eval_06(self):
        self.assertEqual(postfix_eval("4 2 //"), 2)

    def test_postfix_eval_07(self):
        self.assertEqual(postfix_eval("4 2 ^"), 16)

    def test_postfix_eval_08(self):
        self.assertEqual(postfix_eval("5 5 * 10 // 2 +"), 4.0)

    def test_postfix_eval_09(self):
        self.assertEqual(postfix_eval("12.0"), 12.0)

    def test_postfix_eval_10(self):
        self.assertAlmostEqual(postfix_eval("12 7 /"), 1.7142857142857142)

    def test_postfix_eval_empty_input(self):
        with self.assertRaises(ValueError):
            postfix_eval("")

    def test_postfix_eval_invalid_token(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 2 a +")

    def test_postfix_eval_insufficient_operands(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 +")

    def test_postfix_eval_insufficient_operands_2(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 -")

    def test_postfix_eval_insufficient_operands_3(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 *")

    def test_postfix_eval_insufficient_operands_4(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 /")

    def test_postfix_eval_insufficient_operands_5(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 //")

    def test_postfix_eval_insufficient_operands_6(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 ^")

    def test_postfix_eval_too_many_operands(self):
        with self.assertRaises(ValueError):
            postfix_eval("2 1 5 6 *")

    def test_postfix_eval_too_many_operands_2(self):
        with self.assertRaises(ValueError):
            postfix_eval("* * * * *")

    def test_postfix_eval_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            postfix_eval("2 0 /")

    def test_postfix_eval_division_by_zero_2(self):
        with self.assertRaises(ZeroDivisionError):
            postfix_eval("2 0 //")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("1 + 2"), "1 2 +")

    def test_infix_to_postix_02(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"),
                         "3 4 2 * 1 5 - 2 3 ^ ^ / +")

    def test_infix_to_postix_03(self):
        self.assertEqual(infix_to_postfix("5 * 5 * 5 * ( 5 + 9 ) ^ 2 * 3"),
                         "5 5 * 5 * 5 9 + 2 ^ * 3 *")

    def test_infix_to_postix_04(self):
        with self.assertRaises(ValueError):
            infix_to_postfix("")

    def test_infix_to_postix_05(self):
        self.assertEqual(infix_to_postfix("12.0"), "12.0")
    
    def test_infix_to_postix_06(self):
        self.assertEqual(infix_to_postfix("5 - 2 ^ ( 10 * 4 + 2 ) // 3"), "5 2 10 4 * 2 + ^ 3 // -")


if __name__ == "__main__":
    unittest.main()
