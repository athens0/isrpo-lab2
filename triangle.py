
def area(a, h): 
    '''принимает числа a и h, возвращает произведение a и h поделенное на 2'''
    return a * h / 2 

def perimeter(a, b, c): 
    '''принимает числа a, b, c, возвращает их сумму'''
    return a + b + c 

### tests
import unittest

class TriangleTestCase(unittest.TestCase):
    # area tests
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_equal_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_big_int_mul(self):
        res = area(1000000, 22222222)
        self.assertEqual(res, 11111111000000)

    def test_one_mul(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def test_prime_numbers_mul(self):
        res = area(5, 67)
        self.assertEqual(res, 167.5)
    
    def test_float_mul(self):
        res = area(1.2, 3.67)
        self.assertEqual(res, 2.202)

    def test_fraction_mul(self):
        a = 5 / 3
        b = 67 / 48
        s = a * b / 2
        res = area(a, b)
        self.assertEqual(res, s)

    # perimeter tests
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_equal_perimeter(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_big_int_perimeter(self):
        res = perimeter(1000000, 22222222, 1000000)
        self.assertEqual(res, 24222222)

    def test_one_perimeter(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_prime_numbers_perimeter(self):
        res = perimeter(5, 67, 2)
        self.assertEqual(res, 74)

    def test_float_perimeter(self):
        res = perimeter(1.2, 3.67, 2.0)
        self.assertEqual(res, 6.87)

    def test_fraction_perimeter(self):
        a = 5 / 3
        b = 67 / 48
        c = 13 / 2
        p = a + b + c
        res = perimeter(a, b, c)
        self.assertEqual(res, p)
