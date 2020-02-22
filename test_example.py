# This is not intended to test functionality but rather can be used an example for to use unittest

import unittest

# Realistically we would import our modules and test their actual usage against oracles

# Classes are used to have a bundle of test cases that all should base for a given functionality 
class TestBasicMath(unittest.TestCase):

	#These next two will pass
	def test_addition(self):
		self.assertEqual(1+1, 2)

	def test_subtraction(self):
		self.assertEqual(1-1, 0)

	#These next two will fail, and we will see 2 failures of 4
	def test_addition_wrong(self):
		self.assertEqual(1+1, 3)

	def test_subtraction_wrong(self):
		self.assertEqual(1-1, 1)

if __name__ == '__main__':
	# This runs every class and method with test in the name, don't forget to name your tests 'test'
	unittest.main()

# Run this file with <python3 test_example.py> (at least on ix-dev)
