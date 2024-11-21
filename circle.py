import math


def area(r):
    '''принимает число r, возвращает число пи умноженное на квадрат числа r'''
    return math.pi * r * r


def perimeter(r):
    '''принимает число r, возвращает число пи умноженное на 2 и на r'''
    return 2 * math.pi * r

### tests
import unittest

class CircleTestCase(unittest.TestCase):
    # area tests
    def test_zero_mul(self):
        r = 0
        s = math.pi * r * r
        res = area(r)
        self.assertEqual(res, s)

    def test_pi_mul(self):
        r = math.pi
        s = math.pi * r * r
        res = area(r)
        self.assertEqual(res, s)

    def test_big_int_mul(self):
        r = 22222222
        s = math.pi * r * r
        res = area(r)
        self.assertEqual(res, s)

    def test_one_mul(self):
        r = 1
        s = math.pi * r * r
        res = area(r)
        self.assertEqual(res, s)

    def test_prime_numbers_mul(self):
        r = 67
        s = math.pi * r * r
        res = area(r)
        self.assertEqual(res, s)
    
    def test_float_mul(self):
        r = 1.7
        s = math.pi * r * r
        res = area(r)
        self.assertEqual(res, s)

    def test_fraction_mul(self):
        r = 5 / 3
        s = math.pi * r * r
        res = area(r)
        self.assertEqual(res, s)

    # perimeter tests
    def test_zero_perimeter(self):
        r = 0
        s = 2 * math.pi * r
        res = perimeter(r)
        self.assertEqual(res, s)
    
    def test_pi_perimeter(self):
        r = math.pi
        s = 2 * math.pi * r
        res = perimeter(r)
        self.assertEqual(res, s)

    def test_big_int_perimeter(self):
        r = 22222222222
        s = 2 * math.pi * r
        res = perimeter(r)
        self.assertEqual(res, s)

    def test_one_perimeter(self):
        r = 1
        s = 2 * math.pi * r
        res = perimeter(r)
        self.assertEqual(res, s)

    def test_prime_numbers_perimeter(self):
        r = 67
        s = 2 * math.pi * r
        res = perimeter(r)
        self.assertEqual(res, s)

    def test_float_perimeter(self):
        r = 5.6
        s = 2 * math.pi * r
        res = perimeter(r)
        self.assertEqual(res, s)

    def test_fraction_perimeter(self):
        r = 67 / 13
        s = 2 * math.pi * r
        res = perimeter(r)
        self.assertEqual(res, s)
