from __future__ import annotations
import string
from typing import TextIO

# Add more imports here as you use functions from your hash table.
from hash_table import HashTable, keys, contains, set_item, get_item


def djbx33a(s: str) -> int:
    """Return a modified DJBX33A hash of the given string.

    See the project specification for the formula.
    """
    n = min(len(s), 8)
    hash_int = (5381 * (33 ** n) + sum([ord(s[i]) *
                (33 ** (n - 1 - i))
                for i in range(0, n)]))
    return hash_int


def build_stop_words_table(stop_words_file: TextIO) -> HashTable:
    """Return a hash table whose keys are the stop words.

    This will read the stop words from the file and add them to the stop
    words table.  The values stored in the table will not matter.

    Args:
        stop_words_file: the open stop words file.

    Returns:
        A hash table whose keys are the stop words.
    """
    create_hash = HashTable(djbx33a)
    for line in stop_words_file:
        new_line = line.replace("\n", "")
        hash_key = (create_hash.hash_function(new_line) %
                    create_hash.capacity)
        create_hash.table[hash_key].append((new_line, ""))
    return create_hash


def build_concordance_table(file: TextIO, stop_table: HashTable) -> HashTable:
    """Return the concordance table for the given file.

    This will read the given file and build a concordance table
    containing all valid words in the file.

    Args:
        file: the open file to read
        stop_table: a hash table whose keys are the stop words

    Returns:
        A concordance table built from the given file.
    """
    new_hash_table = HashTable(djbx33a)
    count_line = 0
    for line in file:
        line = line.replace("'", "")
        for punctuation in string.punctuation:
            line = line.replace(punctuation, " ")
        line = line.lower()
        line = line.split()
        count_line += 1
        for word in line:
            if word.isalpha() and not contains(stop_table, word):
                if not contains(new_hash_table, word):
                    set_item(new_hash_table, word, [count_line])
                else:
                    line_nums = get_item(new_hash_table, word)
                    if (count_line != line_nums[-1]):
                        line_nums.append(count_line)
                        set_item(new_hash_table, word, line_nums)
    return new_hash_table


def write_concordance_table(file: TextIO, concordance: HashTable) -> None:
    """Write the concordance table to the given file.

    This will sort the strings in the concordance table alphabetically
    and write them to the given file along with the line numbers on
    which they occurred.

    Args:
        file: the open file in which to store the table
        concordance: the concordance table
    """
    lst_of_keys = sorted(keys(concordance))
    for key in lst_of_keys:
        get_the_item = get_item(concordance, key)
        file.write(str(key) + ": "
                   + str(" ".join(str(num)for num in get_the_item)) + "\n")
