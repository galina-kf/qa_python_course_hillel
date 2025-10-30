from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    def get_area(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_perimeter(self):
        return self.__a + self.__b + self.__c

    def get_area(self):
        p = self.get_perimeter()/2
        s = math.sqrt(p*(p-self.__a)*(p-self.__b)*(p-self.__c))
        return s


class Square(Figure):
    def __init__(self, a):
        self.__a = a

    def get_perimeter(self):
        return self.__a*4

    def get_area(self):
        return self.__a**2


class Trapezium(Figure):
    def __init__(self, a, b, h):
        self.__a = a
        self.__b = b
        self.__h = h

    def get_perimeter(self):
        return (self.__a + self.__b)*2

    def get_area(self):
        return (self.__a+self.__b)/2*self.__h


figure_list = [Triangle(3, 4, 5), Square(7), Trapezium(6,9,4)]
for item in figure_list:
    print(f'Perimeter: {item.get_perimeter()}, Area: {item.get_area()}')

