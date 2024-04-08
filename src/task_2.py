from typing import List
import unittest

def is_prime(number: int) -> bool:
    if number <= 1: 
        return False

    denominator: int = 2

    while pow(denominator, 2) < number and number % denominator != 0:
        denominator += 1
    
    return pow(denominator, 2) > number

def get_prime_numbers(start: int, end: int) -> List[int]:
    return [num for num in range(start, end) if is_prime(num)]


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self) -> None:
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2)) 
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))

class TestGetPrimeNumbers(unittest.TestCase):
    def test_get_prime_numbers_from_1_to_20(self) -> None:
        primes = get_prime_numbers(1, 20)
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19])
        
    def test_get_prime_numbers_from_10_to_30(self) -> None:
        primes = get_prime_numbers(10, 30)
        self.assertEqual(primes, [11, 13, 17, 19, 23, 29])

    def test_get_prime_numbers_from_50_to_70(self) -> None:
        primes = get_prime_numbers(50, 70)
        self.assertEqual(primes, [53, 59, 61, 67])


if __name__ == '__main__':
    unittest.main()
