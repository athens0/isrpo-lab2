
def area(a, b): 
    '''принимает числа a и b, возвращает произведение a и b'''
    return a * b 

def perimeter(a, b): 
    '''принимает числа a и b, возвращает их удвоенную сумму'''
    return (a + b) * 2

### tests
import unittest

class RectangleTestCase(unittest.TestCase):
    # area tests
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_big_int_mul(self):
        res = area(1000000, 22222222)
        self.assertEqual(res, 22222222000000)

    def test_one_mul(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_prime_numbers_mul(self):
        res = area(5, 67)
        self.assertEqual(res, 335)
    
    def test_float_mul(self):
        res = area(1.2, 3.67)
        self.assertEqual(res, 4.404)

    def test_fraction_mul(self):
        a = 5 / 3
        b = 67 / 48
        s = a * b
        res = area(a, b)
        self.assertEqual(res, s)

    # perimeter tests
    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    
    def test_square_perimeter(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_big_int_perimeter(self):
        res = perimeter(1000000, 22222222)
        self.assertEqual(res, 46444444)

    def test_one_perimeter(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_prime_numbers_perimeter(self):
        res = perimeter(5, 67)
        self.assertEqual(res, 144)

    def test_float_perimeter(self):
        res = perimeter(1.2, 3.67)
        self.assertEqual(res, 9.74)

    def test_fraction_perimeter(self):
        a = 5 / 3
        b = 67 / 48
        p = a * 2 + b * 2
        res = perimeter(a, b)
        self.assertEqual(res, p)
