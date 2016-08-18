import unittest
from sum import my_sum

class MySumTests(unittest.TestCase):

	def setUp(self):
		#setting up
		self.numbers = [4,5,1,3,8]

	def test_sum_of_numbers(self):
		'''
		Test sum of digits/numbers
		'''

		self.assertEqual(my_sum(10,15), 25)
		self.assertEqual(my_sum(20,15), 35)
		self.assertEqual(my_sum(2,3), 5)
		self.assertEqual(my_sum(1,2), 3)
		self.assertEqual(my_sum(3,3), 6)

	def test_non_numbers(self):
		self.assertEqual(my_sum('a', 'a'), "invalid")
		





if __name__ == '__main__':
	unittest.main()