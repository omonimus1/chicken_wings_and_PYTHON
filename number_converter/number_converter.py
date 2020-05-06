#!/usr/local/bin/python
"""
Author: Davide Pollicino 
Date: 06/05/2020
Summary: Python script that having in input a number conver it in string, hexadecimal , 
octal string prefixed with “0o” and binary, using the bin() method, that will 
provide a string with a 'ob' prefix.
"""

from num2words import num2words  # pip install num2words


def get_user_number():
    number_to_convert = int(input('Inset a number to convert: '))
    return number_to_convert


def convert_number(number_to_convert):
    print('Number in string ' + str(number_to_convert))
    print('Number in words: ' + num2words(number_to_convert))
    print('Number in decimal ' + bin(number_to_convert))
    print('Number in hexadecimal' + hex(number_to_convert))
    print('Number in oct ' + oct(number_to_convert))


if __name__ == '__main__': 
    number = get_user_number()
    convert_number(number)