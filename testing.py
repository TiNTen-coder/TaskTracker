import unittest
import os


class Testing(unittest.TestCase):
    def test_login1(self):
        os.system('python3 -m TaskTracker admin123 admin123 > result1.txt')
        with open("result1.txt", 'r') as f:
            self.assertEqual(f.readline(), 'Unknown user\n')

    def test_login2(self):
        os.system('python3 -m TaskTracker admin admin123 > result2.txt')
        with open("result2.txt", 'r') as f:
            self.assertEqual(f.readline(), 'Incorrect password. Try again\n')

    def test_login3(self):
        os.system('python3 -m TaskTracker admin > result3.txt')
        with open("result3.txt", 'r') as f:
            self.assertEqual(f.readline(), 'Incorrect positional arguments\n')

    def test_login4(self):
        os.system('python3 -m TaskTracker > result4.txt')
        with open("result4.txt", 'r') as f:
            self.assertEqual(f.readline(), 'Using superuser mode\n')

    def test_login5(self):
        os.system('python3 -m TaskTracker admin admin > result5.txt')
        with open("result5.txt", 'r') as f:
            self.assertEqual(f.readline(), '')