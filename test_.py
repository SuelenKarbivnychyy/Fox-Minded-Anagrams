"""Run ```python3 -m unittest``` to run tests """


import unittest
from task import anagram


class MyTestCase(unittest.TestCase):

    def test_anagram(self):

        result = anagram("a1bcd efg!h")        

        self.assertEqual(result, "d1cba hgf!e")



    def test_sentence(self):

        result = anagram("a!b@c# d$e3f")

        self.assertEqual(result, "c!b@a# f$e3d")



    def test3(self):

        result = anagram("a!b@c#d$e5f")

        self.assertEqual(result, "f!e@d#c$b5a")



    def test4(self):

        result = anagram("abcd efgh")

        self.assertEqual(result, "dcba hgfe")

           

