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


