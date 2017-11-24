import unittest

from Gener import *
from MathO import *

class GeneratorTest(unittest.TestCase):
   """Generator tests"""

   @classmethod
   def setUpClass(cls):
       """Set up for class"""
       print("setUpClass")
       print("==========")

   @classmethod
   def tearDownClass(cls):
       """Tear down for class"""
       print("==========")
       print("tearDownClass")

   def setUp(self):
       """Set up for test"""
       print("Set up for [" + self.shortDescription() + "]")

   def tearDown(self):
       """Tear down for test"""
       print("Tear down for [" + self.shortDescription() + "]")
       print("")

   def test_cut(self):
       """Add operation test"""
       print("id: " + self.id())
       self.assertEqual( Gen.cut( 0.8, 1.2 ), 4, 7 )

   def test_expected_value(self):
       print("id: " + self.id())
       self.assertEqual( Math1.expected_value(), )




if __name__ == '__main__':
   unittest.main()
