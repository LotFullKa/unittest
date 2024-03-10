import unittest

from src.Geometry import Point, Flate

# Наследуемся от unittest.TestCase
class TestPoint(unittest.TestCase):
    
    # Запускается перед выполнением класса
    def setUpClass():
        print('\nНачинаем прогон test Point\n')
    
    # Запускается после выполнения класса
    def tearDownClass():
        print('\nЗакончили прогон test Point\n')
    
    # Запускается перед каждым тестом класса 
    def setUp(self):
        self.A = Point(5, 6)
        self.B = Point(6, 10)
        self.C = Point(5.0, 6.0)
        self.D = Point(-5, -6)
        
    
    # Запускается после каждого теста класса
    def tearDown(self) -> None:
        del self.A
        del self.B
        del self.C
        del self.D
    
    def test_init(self):
        self.assertEqual(
            (self.A.x, self.A.y),
            (float(5), float(6)),
            "Полученные значения не являются вещественными!!!",
        )
        self.assertEqual(
            (self.B.x, self.B.y),
            (float(6), float(10)),
            "Полученные значения не являются вещественными!!!",
        )
        self.assertEqual(
            (self.C.x, self.C.y),
            (float(5), float(6)),
            "Полученные значения не являются вещественными!!!",
        )
        self.assertEqual(
            (self.D.x, self.D.y),
            (float(-5), float(-6)),
            "Полученные значения не являются вещественными!!!",
        )

    def test_str(self):
        self.assertTrue(str(self.A) == "(5.0, 6.0)", "Неправильный вывод на экран!!!")
        self.assertTrue(str(self.B) == "(6.0, 10.0)", "Неправильный вывод на экран!!!")
        self.assertTrue(str(self.C) == "(5.0, 6.0)", "Неправильный вывод на экран!!!")
        self.assertTrue(str(self.D) == "(-5.0, -6.0)", "Неправильный вывод на экран!!!")

    def test_eq(self):
        self.assertTrue(
            self.A == self.C,
            "Данные две точки равны, а в результате тестирования, они оказались неравными!!!",
        )
        self.assertFalse(
            self.A == self.B,
            "Данные две точки неравны, а в результате тестирования, они оказались равными!!!",
        )
        self.assertFalse(
            self.A == self.D,
            "Данные две точки неравны, а в результате тестирования, они оказались равными!!!",
        )

    def test_ne(self):
        self.assertFalse(
            self.A != self.C,
            "Данные две точки равны, а в результате тестирования, они оказались неравными!!!",
        )
        self.assertTrue(
            self.A != self.B,
            "Данные две точки неравны, а в результате тестирования, они оказались равными!!!",
        )
        self.assertTrue(
            self.A != self.D,
            "Данные две точки неравны, а в результате тестирования, они оказались равными!!!",
        )

