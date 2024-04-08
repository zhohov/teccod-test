from abc import ABC, abstractmethod
import unittest


class IPoint(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_x(self) -> float:
        pass
    
    @abstractmethod
    def get_y(self) -> float:
        pass
    
    @abstractmethod
    def set_x(self, value: float) -> None:
        pass
    
    @abstractmethod
    def set_y(self, value: float) -> None:
        pass
    
    @abstractmethod
    def distance_to(self, other: 'IPoint') -> float:
        pass


class Point(IPoint):
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = x
        self._y = y

    @property
    def get_x(self) -> float:
        return self._x
    
    @property
    def get_y(self) -> float:
        return self._y
    
    @get_x.setter
    def set_x(self, value: float) -> None:
        self._x = value
    
    @get_y.setter
    def set_y(self, value: float) -> None:
        self._y = value

    def distance_to(self, other: 'Point') -> float:
        a = self.get_x - other.get_x
        b = self.get_y - other.get_y
        return ((a ** 2) + (b ** 2)) ** 0.5
    

class TestPoint(unittest.TestCase):
    def test_distance_to_same_point(self) -> None:
        point1 = Point(3, 4)
        point2 = Point(3, 4)
        self.assertEqual(point1.distance_to(point2), 0)

    def test_distance_to_different_points(self) -> None:
        point1 = Point(1, 2)
        point2 = Point(4, 6)
        self.assertEqual(point1.distance_to(point2), 5)

    def test_distance_to_negative_coordinates(self) -> None:
        point1 = Point(-2, -3)
        point2 = Point(-5, -7)
        self.assertEqual(point1.distance_to(point2), 5)


if __name__ == '__main__':
    unittest.main()
    
    