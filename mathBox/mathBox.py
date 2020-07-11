class mathBox:

	def __init__(self, name):

		self.name = name

	def add(self, num1, num2, printBoolean):

		res = num1 + num2

		if printBoolean == True:

			print()

			print(res)

		return res

	def multiple(self, num1, num2, printBoolean):

		res = num1 * num2

		if printBoolean == True:

			print()

			print(res)

		return res

	def minus(self, num1, num2, printBoolean):

		res = num1 - num2

		if printBoolean == True:

			print()

			print(res)

		return res


	def divide(self, num1, num2, printBoolean):

		res = num1 / num2

		if printBoolean == True:

			print()

			print(res)

		return res

	def pow(self, num1, num2, printBoolean):

		res = num1 ** num2

		if printBoolean == True:

			print()

			print(res)

		return res
