from __future__ import annotations

from collections.abc import Callable
from typing import Any, List, Tuple

# Each entry in the hash table array will be a list of key, value pairs
HashChain = List[Tuple[Any, Any]]

# NOTE: READ THE GIVEN TESTS FIRST.  Before you can write any code, you
# need to have a solid understanding of what each function is doing and
# why.


class HashTable:
    """A hash table with separate chaining."""

    def __init__(self, hash_function: Callable[[Any], int]):
        """Create an empty hash table.

        Args:
            hash_function:
                The function to compute hash values for the given keys.
        """
        self.capacity: int = 5
        self.table: list[HashChain] = [[] for _ in range(self.capacity)]

        self.size: int = 0
        self.hash_function = hash_function


def set_item(hash_table: HashTable, key: Any, value: Any) -> None:
    hash_key = (hash_table.hash_function(key) % hash_table.capacity)
    for item in hash_table.table[hash_key]:
        if item[0] == key:
            hash_table.table[hash_key].pop()
            hash_table.table[hash_key].append((key, value))
            return
    hash_table.table[hash_key].append((key, value))
    hash_table.size += 1  
    if (hash_table.size / hash_table.capacity) > 1.0:
        hash_table.capacity *= 2
        new_ht = [[] for _ in range(hash_table.capacity)]
        for item in hash_table.table:
            for itemitem in item:
                new_hash_key = hash_table.hash_function(itemitem[0]) % hash_table.capacity
                new_ht[new_hash_key].append((itemitem[0], itemitem[1]))
        hash_table.table = new_ht


def get_item(hash_table: HashTable, key: Any) -> Any:
    hash_key = (hash_table.hash_function(key) % hash_table.capacity)
    for item in hash_table.table[hash_key]:
        if item[0] == key:
            return item[1]
    raise KeyError


def contains(hash_table: HashTable, key: Any) -> bool:
    hash_key = (hash_table.hash_function(key) % hash_table.capacity)
    for item in hash_table.table[hash_key]:
        if item[0] == key:
            return True
    return False


def remove(hash_table: HashTable, key: Any) -> tuple[Any, Any]:
    hash_key = (hash_table.hash_function(key) % hash_table.capacity)
    counter = 0
    for item in hash_table.table[hash_key]:
        if item[0] == key:
            pop_it = hash_table.table[hash_key].pop(counter)
            hash_table.size -= 1
            return pop_it
        counter += 1
    raise KeyError


def size(hash_table: HashTable) -> int:
    return hash_table.size


def keys(hash_table: HashTable) -> list[Any]:
    lst_of_keys = []
    for item in hash_table.table:
        for itemitem in item:
            lst_of_keys.append(itemitem[0])
    return lst_of_keys


def values(hash_table: HashTable) -> list[Any]:
    lst_of_values = []
    for item in hash_table.table:
        for itemitem in item:
            lst_of_values.append(itemitem[1])
    return lst_of_values


def _contents(hash_table: HashTable) -> list[HashChain]:
    return hash_table.table
