import unittest
from main import divide

class testdivide(unittest.TestCase):
  def testdivide1(self):
    self.assertEqual(divide (10, 5), 2)
    
if __name__ == '__main__':
  unittest.main()
