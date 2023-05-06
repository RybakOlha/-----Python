import unittest
from task_25 import analyze_input

class TestAnalyze_input(unittest.TestCase):
    def test_analyze_input(self):
        self.assertEqual(analyze_input("0"), "Ви ввели нуль")
        self.assertEqual(analyze_input("-6,7"),"Ви ввели відʼємне дробове число: -6.7")
        self.assertEqual(analyze_input("5"), "Ви ввели додатне ціле число: 5")
        self.assertEqual(analyze_input("5.4r"), "Ви ввели некоректне число: 5.4r")
        self.assertEqual(analyze_input("-.777"), "Ви ввели відʼємне дробове число: -0.777")
        self.assertEqual(analyze_input(".000"), "Ви ввели нуль")
        self.assertEqual(analyze_input("5.49.3"), "Ви ввели некоректне число: 5.49.3")
        self.assertEqual(analyze_input("--.49"), "Ви ввели некоректне число: --.49")
        self.assertEqual(analyze_input("001.23"), "Ви ввели дробове додатне число: 1.23")
        self.assertEqual(analyze_input("12."), "Ви ввели дробове додатне число: 12.0")
        self.assertEqual(analyze_input("-.5"), "Ви ввели відʼємне дробове число: -0.5")
        self.assertEqual(analyze_input("-.050"), "Ви ввели відʼємне дробове число: -0.05")

if __name__ == '__main__':
    unittest.main()