
def area(a):
    '''принимает число a, возвращает квадрат числа a'''
    return a * a


def perimeter(a):
    '''принимает число a, возвращает a * 4'''
    return 4 * a

### tests
import unittest

class SquareTestCase(unittest.TestCase):
    # area tests
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_big_int_mul(self):
        res = area(1000000)
        self.assertEqual(res, 1000000000000)

    def test_one_mul(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_prime_numbers_mul(self):
        res = area(5)
        self.assertEqual(res, 25)
    
    def test_float_mul(self):
        res = area(1.5)
        self.assertEqual(res, 2.25)

    def test_fraction_mul(self):
        b = 67 / 48
        s = b * b
        res = area(b)
        self.assertEqual(res, s)
    
    def test_negative_mul(self):
        b = -5
        s = b * b
        res = area(b)
        self.assertEqual(res, s)

    # perimeter tests
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_square_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_big_int_perimeter(self):
        res = perimeter(22222222)
        self.assertEqual(res, 88888888)

    def test_one_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_prime_numbers_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_float_perimeter(self):
        res = perimeter(1.2)
        self.assertEqual(res, 4.8)

    def test_fraction_perimeter(self):
        b = 67 / 48
        p = b * 4
        res = perimeter(b)
        self.assertEqual(res, p)
    
    def test_negative_perimeter(self):
        b = -5
        p = b * 4
        res = perimeter(b)
        self.assertEqual(res, p)
