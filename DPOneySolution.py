"""
Author: Davide Pollicino
Date: 04/05/2020
Summary: Python script that having in input a number expressed in words, print out it's numerical version.
	Es: IN = 'nine' -> Output: 9
"""
# Thir Part applications
from word2number import w2n   # pip install word2number -> https://pypi.org/project/word2number/


def word_to_number_converter():
	print('Ready to get your input')
	# Read the input
	number_to_convert = input()

	try:
		# Print the string converted in number
		print (w2n.word_to_num(number_to_convert))
	except:
		# Error message in case you the input is wrong
		print('Probably you tried to give me a negative number or a wrong input,' + 
		'you asked me to manage just natural numbers N')
		print('try again')
		word_to_number_converter()


if __name__ == '__main__':
	word_to_number_converter()
