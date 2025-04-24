import unittest

from two_colorable import is_two_colorable


class Tests(unittest.TestCase):
    def test_01(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v1"],
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_02(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v1"],
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_03(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v1"],
            ["v1", "v3"],
            ["v2", "v4"],
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_04(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v5"],
            ["v5", "v1"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_05(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v3", "v4"],
            ["v5", "v6"],
            ["v6", "v7"]
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_06(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v3", "v4"],
            ["v5", "v6"],
            ["v6", "v7"],
            ["v7", "v5"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_07(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v5"],
            ["v5", "v6"],
            ["v6", "v1"]
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_08(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v5"],
            ["v5", "v6"],
            ["v6", "v7"],
            ["v7", "v1"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_09(self) -> None:
        edge_list = []

        for i in range(4000):
            if i == 3999:
                edge = [str(i), "0"]
            else:
                edge = [str(i), str(i + 1)]
            edge_list.append(edge)

        self.assertTrue(is_two_colorable(edge_list))

    def test_10(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v1", "v3"],
            ["v1", "v4"],
            ["v3", "v6"],
            ["v4", "v6"],
            ["v6", "v5"]
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_11(self) -> None:
        edges = [[]]

        self.assertTrue(is_two_colorable(edges))

    def test_12(self) -> None:
        edges = [
            ["v1", "v2"]
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_13(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v1", "v3"],
            ["v1", "v4"],
            ["v5", "v6"]
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_14(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v2", "v5"],
            ["v3", "v5"],
            ["v5", "v6"],
            ["v3", "v7"],
            ["v7", "v6"],
            ["v1", "v3"],
            ["v1", "v4"],
            ["v5", "v6"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_15(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v1"],
            ["v4", "v5"],
            ["v5", "v6"],
            ["v7", "v8"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_16(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v5"],
            ["v5", "v1"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_17(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v5"],
            ["v5", "v6"],
            ["v6", "v1"]
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_18(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v3", "v4"],
            ["v5", "v6"],
            ["v6", "v7"]
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_19(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v3", "v4"],
            ["v5", "v6"],
            ["v6", "v7"],
            ["v7", "v5"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_20(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v5"],
            ["v5", "v6"],
            ["v6", "v7"],
            ["v7", "v1"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_21(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v1", "v3"],
            ["v1", "v4"],
            ["v3", "v6"],
            ["v4", "v6"],
            ["v6", "v5"],
            ["v7", "v8"],
            ["v7", "v9"],
            ["v8", "v9"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_22(self) -> None:
        edges = [
            ["v1", "v2"],
            ["v2", "v3"],
            ["v3", "v4"],
            ["v4", "v1"],
            ["v1", "v3"],
            ["v2", "v4"]
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_23(self) -> None:
        edges = [
            ["v2", "v5"],
            ["v1", "v3"],
            ["v4", "v5"],
            ["v3", "v6"],
            ["v6", "v2"]
        ]

        self.assertTrue(is_two_colorable(edges))


if __name__ == "__main__":
    unittest.main()
