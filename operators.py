# Importing unittest
import unittest

class ArithmeticFunctions():
	"""Class to handle arithmetic operations in 
	functions. Add, Multiply, Subtract and Divide"""

	# Add function
	def addition(self, a, b):
		"""Addition function"""
		return a + b

	# Multiply function
	def multiply(self, a, b):
		"""Multiplication function"""
		return a * b

arithmetic_object = ArithmeticFunctions()

# Call the addition() method
result_add = arithmetic_object.addition(3, 3)
result_mult = arithmetic_object.multiply(3, 3)

# printing the results
print "The Sum is: ", result_add
print "The Product is: ", result_mult

# Test class
class TestClass(unittest.TestCase):
	"""TestClass used to Test arithmetic operations"""

	# test for addition function
	def test_addition(self):
		"""Addition test function"""
		self.assertTrue(arithmetic_object.addition(2, 3) == 5)

	# test for multiplication
	def test_multiplication(self):
		"""Multiplication test function"""
		self.assertTrue(arithmetic_object.multiply(3, 3) == 9)