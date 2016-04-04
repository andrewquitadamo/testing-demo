import unittest
from gc_calc import *

class GcTests(unittest.TestCase):
    def test_gc(self):
        self.assertEqual(gc('ACTG'), 0.5)
    def test_empty(self):
        self.assertRaises(TypeError, gc, )
    def test_long(self):
        self.assertAlmostEqual(gc('ACTGCAGATCTGAAATTCAGTAAGGG'), 0.4230769)
    def test_do_nothing(self):
        self.assertEqual(do_nothing(), "Reduce test coverage")

if __name__ == '__main__':
    unittest.main()

