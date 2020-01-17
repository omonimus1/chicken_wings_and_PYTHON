#!/usr/bin/env python3

# Author : Davide Pollicino
# Date: 17/01/2020
# Implementation of a function that check if a string is Palindrome or not 


def check_if_palindrome(string_test):
	z = string_test[::-1]
	if z == string_test:
		print_answer(1 , string_test)
	else:
		print_answer(0 , string_test)


def print_answer(result_elaboration , input_test):
	if result_elaboration:
		print("{0}is Palindrom".format(input_test))
	else:
		print("{0} is not palindrome".format(input_test))	


#test 1
check_if_palindrome("Davide")


#test 2
answer = check_if_palindrome("abba")


