import io
import unittest

from concordance import (
    build_concordance_table,
    build_stop_words_table,
    write_concordance_table,
)
from hash_table import keys


class Tests(unittest.TestCase):
    def test_stop_words_small(self):
        small_stop_words_file = io.StringIO("a\nan\nthe\n")

        stop_words = build_stop_words_table(small_stop_words_file)

        self.assertEqual(sorted(keys(stop_words)), ["a", "an", "the"])

    def test_build_concordance_small(self):
        small_stop_words_file = io.StringIO("a\nan\nthe\n")
        small_file = io.StringIO("this is a file\n")

        stop_words = build_stop_words_table(small_stop_words_file)
        concordance_table = build_concordance_table(small_file, stop_words)

        self.assertEqual(
            sorted(keys(concordance_table)), ["file", "is", "this"]
        )

    def test_build_concordance_small_2(self):
        small_stop_words_file = io.StringIO("a\nan\nthe\n")
        small_file = io.StringIO("this is a file\n")

        stop_words = build_stop_words_table(small_stop_words_file)
        concordance_table = build_concordance_table(small_file, stop_words)

        self.assertEqual(
            sorted(keys(concordance_table)), ["file", "is", "this"]
        )

    def test_build_concordance_small_3(self):
        small_stop_words_file = io.StringIO("a\nan\nthe\n")
        small_file = io.StringIO("alex binh alex alex, alex\nalex\
                                 \nalex\nalex alex, binh binh binh\
                                 \n binh this this is me")

        stop_words = build_stop_words_table(small_stop_words_file)
        concordance_table = build_concordance_table(small_file, stop_words)

        self.assertEqual(
            sorted(keys(concordance_table)), ["alex", "binh",
                                              "is", "me", "this"]
        )

    def test_build_concordance_small_4(self):
        small_stop_words_file = io.StringIO("a\nan\nthe\n")
        small_file = io.StringIO("")

        stop_words = build_stop_words_table(small_stop_words_file)
        concordance_table = build_concordance_table(small_file, stop_words)

        self.assertEqual(
            sorted(keys(concordance_table)), []
        )

    def test_build_concordance_small_5(self):
        small_stop_words_file = io.StringIO("a\nan\nthe\n")
        small_file = io.StringIO("A AN THE")

        stop_words = build_stop_words_table(small_stop_words_file)
        concordance_table = build_concordance_table(small_file, stop_words)

        self.assertEqual(
            sorted(keys(concordance_table)), []
        )

    def test_build_concordance_small_6(self):
        small_stop_words_file = io.StringIO("a\nan\nthe\n")
        small_file = io.StringIO("Catching a bug in the \
                                 morning\n but bug too buggy")

        stop_words = build_stop_words_table(small_stop_words_file)
        concordance_table = build_concordance_table(small_file, stop_words)

        self.assertEqual(
            sorted(keys(concordance_table)), ["bug", "buggy",
                                              "but", "catching",
                                              "in", "morning", "too"]
        )

    def test_write_concordance_small(self):
        small_stop_words_file = io.StringIO("a\nan\nthe\n")
        small_file = io.StringIO("this is a file\n")
        out_file = io.StringIO()

        stop_words = build_stop_words_table(small_stop_words_file)

        concordance_table = build_concordance_table(small_file, stop_words)

        write_concordance_table(out_file, concordance_table)
        result = out_file.getvalue()

        self.assertEqual(result, "file: 1\nis: 1\nthis: 1\n")

    def test_file1(self) -> None:
        with open("stop_words.txt", encoding="utf8") as stop_words_file:
            stop_words = build_stop_words_table(stop_words_file)

        with open("file1.txt", encoding="utf8") as in_file:
            concordance_table = build_concordance_table(in_file, stop_words)

        out_file = io.StringIO()
        write_concordance_table(out_file, concordance_table)
        result = out_file.getvalue()

        with open("file1_sol.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())

    def test_file2(self) -> None:
        with open("stop_words.txt", encoding="utf8") as stop_words_file:
            stop_words = build_stop_words_table(stop_words_file)

        with open("file2.txt", encoding="utf8") as in_file:
            concordance_table = build_concordance_table(in_file, stop_words)

        out_file = io.StringIO()
        write_concordance_table(out_file, concordance_table)
        result = out_file.getvalue()

        with open("file2_sol.txt", encoding="utf8") as correct_out:
            self.assertEqual(result, correct_out.read())


if __name__ == "__main__":
    unittest.main()
