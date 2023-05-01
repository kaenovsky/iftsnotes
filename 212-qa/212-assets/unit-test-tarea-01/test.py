import unittest
import demo

class mytest(unittest.TestCase):
    def test_name(self):
        name = demo.persona_name('alejandro')
        self.assertEqual(name, 'alejandro')

    def test_age(self):
        age = demo.persona_age(56)
        self.assertEqual(age, 56)

    def test_false_name(self):
        name = demo.persona_name('sean')
        self.assertEqual(name, 'jake')

    def test_false_age(self):
        age = demo.persona_age(89)
        self.assertEqual(age, 76)