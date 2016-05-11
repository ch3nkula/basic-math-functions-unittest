#######################################################
# Author: Alangi Derick (d3r1ck), B.Eng, CM			  #
# Date: 11th May, 2016. 							  #
# Aim: Practicing my skills on Unit testing in Python #
#######################################################

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

	# Divide function
	def divide(self, a, b):
		"""Division function"""
		return a / b

	# Subtract function
	def subtract(self, a, b):
		"""Subtraction function"""
		return a - b

# Creating an object of the ArithmeticFunctions Class
arithmetic_object = ArithmeticFunctions()

# Call the various methods to test operations
result_add = arithmetic_object.addition(3, 3)
result_mult = arithmetic_object.multiply(3, 3)
result_div = arithmetic_object.divide(10, 5)
result_sub = arithmetic_object.subtract(3, 10)

# printing the results
print "The Sum is: ", result_add
print "The Product is: ", result_mult
print "The Divident is: ", result_div
print "The Difference is: ", result_sub

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

	# test for division
	def test_division(self):
		"""Division test function"""
		self.assertTrue(arithmetic_object.divide(10, 5) == 2)

	# test for subtraction
	def test_subtraction(self):
		"""Subtraction test function"""
		self.assertTrue(arithmetic_object.subtract(5, 5) == 0)