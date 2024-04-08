from typing import Set, List
import unittest

def get_unique_numbers(numbers: List[int]) -> Set[int]:
    return set(numbers)


class TestGetUniqueNumbers(unittest.TestCase):
    def test_get_unique_numbers_empty_list(self) -> None:
        numbers = []
        unique_numbers = get_unique_numbers(numbers)
        self.assertEqual(unique_numbers, set())
        
    def test_get_unique_numbers_single_element(self) -> None:
        numbers = [5]
        unique_numbers = get_unique_numbers(numbers)
        self.assertEqual(unique_numbers, {5}) 

    def test_get_unique_numbers_multiple_elements(self) -> None:
        numbers = [2, 3, 5, 3, 7, 2, 5, 8]
        unique_numbers = get_unique_numbers(numbers)
        self.assertEqual(unique_numbers, {2, 3, 5, 7, 8})


if __name__ == '__main__':
    unittest.main()
