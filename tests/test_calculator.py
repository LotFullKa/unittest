import unittest

from src.Calculator import Calculator


# Test cases to test Calulator methods
# Всегда наследуемся от класса unittest.TestCase 
class TestCalculator(unittest.TestCase):

    # Запускается перед каждый тестом класса
    def setUp(self):
        self.calculator = Calculator()

    # Запускается после каждого теста класса
    def tearDown(self):
        del self.calculator

    # метод теста должен начинаться с "test_"
    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)
    
    def test_cumsum(self):
        for i in range(0, 10):
            f"""test the sum from 0 to {i}"""
            with self.subTest(i=i):
                summ = 0
                for k in range(i):
                    summ = self.calculator.add(summ, k)
                if i != 2:
                    self.assertEqual(summ, i*(i-1)/2, "wrong sum in cumulutive sum")
                else:
                    self.assertEqual(summ, 0, "bad iteartion")

    @unittest.skipIf(Calculator.__version__ < (1, 3), "not supported in this library version")
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    @unittest.skip("demonstrating skipping")
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)


