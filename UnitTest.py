import unittest
import Generator


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

   def test_add(self):
       """Add operation test"""
       print("id: " + self.id())
       self.assertEqual(Generator.add(1, 2), 3)

   def test_sub(self):
       """Sub operation test"""
       print("id: " + self.id())
       self.assertEqual(Generator.sub(4, 2), 2)

   def test_mul(self):
       """Mul operation test"""
       print("id: " + self.id())
       self.assertEqual(Generator.mul(2, 5), 10)

   def test_div(self):
       """Div operation test"""
       print("id: " + self.id())
       self.assertEqual(Generator.div(8, 4), 2)


if __name__ == '__main__':
   unittest.main()
