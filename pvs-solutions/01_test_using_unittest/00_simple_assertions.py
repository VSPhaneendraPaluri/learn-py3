'''
This tutorial presents the user on an alternative mode of testing avaiable
in Python, namely, testing using 'unittest' module

This is inspired from JUnit test(s)

'unittest' module presents the following concepts
1. test fixture
2. test case
3. test suite
4. test runner

The current file presents how to write test cases (#3) using 'unittest' module

NOTE:
* Note the way the test class is 'subclass'('ed) from 'TestCase' class
* Note the naming convention of the test cases written (tests start using 'test_')

'''

# Import Python Modules
import unittest


class SampleClass(object):
  language = "Python"
  piValue = 3.14159
  firstTenPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  languageDetails = {language : "Guido van Rossum"}
  radius = 2   # (in units)


class TestSampleClass(unittest.TestCase):

  '''
  This test illustrates the user on how to use the 'assertEqual' method
  >>> test_assertEqual("Pytho")
  '''
  def test_assertEqual(self, valueObject):
    sampleClassObject = SampleClass()
    self.assertEqual(sampleClassObject.language, "Python")

  '''
  This test illustrates the user on how to use the 'assertAlmostEqual' method
  '''
  def test_assertAlmostEqual(self):
    sampleClassObject = SampleClass()
    numberOfDecimalPlaces = 2
    self.assertAlmostEqual(sampleClassObject.piValue, 3.14, numberOfDecimalPlaces)

  '''
  This test illustrates the user on how to use the 'assertCountEqual' method
  '''
  def test_assertCountEqual(self):
    sampleClassObject = SampleClass()
    tenPrimesInDecendingOrder = [29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
    self.assertCountEqual(sampleClassObject.firstTenPrimes, tenPrimesInDecendingOrder)

  '''
  This test illustrates the user on how to use the 'assertDictEqual' method 
  '''
  def test_assertDictEqual(self):
    sampleClassObject = SampleClass()
    self.assertDictEqual(sampleClassObject.languageDetails, {"Python" : "Guido van Rossum"})

  '''
  This test illustrates the user on how to use the 'assertTrue' method
  '''
  def test_assertTrue(self):
    sampleClassObject = SampleClass()
    self.assertTrue((2*sampleClassObject.piValue*sampleClassObject.radius) > 0)

  '''
  This test illustrates the user on how to use the 'assertGreater' method
  '''
  def test_assertGreater(self):
    sampleClassObject = SampleClass()
    # 2*pi*radius = 2 * 3.14159 * 2 = 12.56636
    self.assertGreater((2*sampleClassObject.piValue*sampleClassObject.radius), 12.0)

  '''
  This test illustrates the user on how to use the 'assertGreaterEqual' method
  '''
  def test_assertGreaterEqual(self):
    sampleClassObject = SampleClass()
    self.assertGreaterEqual((2 * sampleClassObject.piValue * sampleClassObject.radius), 12.56636)

  '''
  This test illustrates the user on how to use the 'assertFalse' method
  '''
  def test_assertFalse(self):
    sampleClassObject = SampleClass()
    self.assertFalse(sampleClassObject.piValue < 3.0, "Pi value should not be less than 3.14xxx")
  
  '''
  This test illustrates the user on how to use the 'assertLess' method
  '''
  def test_assertLess(self):
    sampleClassObject = SampleClass()
    self.assertLess((2 * sampleClassObject.piValue * sampleClassObject.radius), 13.0)

  '''
  This test illustrates the user on how to use the 'assertLessEqual' method
  '''
  def test_assertLessEqual(self):
    sampleClassObject = SampleClass()
    # 2*pi*radius = 2 * 3.14159 * 2 = 12.56636
    self.assertLessEqual(sampleClassObject.piValue, 3.1415926535)

  '''
  This test illustrates the user on how to use the 'assertIn' method
  '''
  def test_assertIn(self):
    sampleClassObject = SampleClass()
    self.assertIn(2, sampleClassObject.firstTenPrimes)
    self.assertIn(11, sampleClassObject.firstTenPrimes)

  '''
  This test illustrates the user on how to use the 'assertIs' method
  '''
  def test_assertIs(self):
    sampleClassObject = SampleClass()
    self.assertIs(type(sampleClassObject.languageDetails[sampleClassObject.language]), str, "type of value of languageDetails dict is not of string type")

  '''
  This test illustrates the user on how to use the 'assertIsInsance' method
  '''
  def test_assertIsInstance(self):
    sampleClassObject = SampleClass()
    self.assertIsInstance(sampleClassObject, SampleClass, "sampleClassObject is not an instance of SampleClass")

  '''
  This test illustrates the user on how to use the 'assertIsNone' method
  '''
  def test_assertIsNone(self):
    sampleClassObject = None
    self.assertIsNone(sampleClassObject, "Object is not NULL")
    
  '''
  This test illustrates the user on how to use the 'assertIsNot' method
  '''
  def test_assertIsNot(self):
    sampleClassObject1 = SampleClass()
    sampleClassObject2 = None
    self.assertIsNot(sampleClassObject1, sampleClassObject2, "Both the instances are of the same type")

  '''
  NOTE:  Likewise, there are few more methods that are available.
         Check Python documentation for further details.
  '''


# DO NOT EDIT ANYTHING BEYOND THIS !
if __name__ == "__main__":
  unittest.main()