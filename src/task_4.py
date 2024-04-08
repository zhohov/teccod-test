from dataclasses import dataclass
from typing import List
import unittest


@dataclass(frozen=True)
class SortedArrays:
    sorted_array: List[str]
    reversed_sorted_array: List[str]


def sort_by_length(words: List[str]) -> SortedArrays:
    sorted_array:  List[str] = sorted(words, key=len)
    reversed_sorted_array: List[str] = sorted(words, key=len, reverse=True)

    return SortedArrays(
        sorted_array=sorted_array,
        reversed_sorted_array=reversed_sorted_array
    )


class TestSortByLength(unittest.TestCase):
    def test_sort_by_length_asc(self) -> None:
        words = ["apple", "banana", "grape", "kiwi"]
        result = sort_by_length(words)
        self.assertEqual(result.sorted_array, ["kiwi", "apple", "grape", "banana"])

    def test_sort_by_length_desc(self) -> None:
        words = ["apple", "banana", "grape", "kiwi"]
        result = sort_by_length(words)
        self.assertEqual(result.reversed_sorted_array, ["banana", "apple", "grape", "kiwi"])

    def test_sort_by_length_empty_list(self) -> None:
        words = []
        result = sort_by_length(words)
        self.assertEqual(result.sorted_array, [])
        self.assertEqual(result.reversed_sorted_array, [])


if __name__ == '__main__':
    unittest.main()
