import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42) == 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42) == -42, "Should be absolute value of a number")

if __name__ == "__main__": # Необходимо для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля.
    unittest.main()