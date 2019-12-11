# Author: Davide Pollicino
# 11/12/2019

"""
	Program that calculat if a year is a Leap year or not
	between the year 0 and 2020
"""

def isLeap(year):
    if year % 400 == 0 :
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def main():
    for year in range(2021):
        if isLeap(year):
            print("{0} ,It's a leap yer" .format(year))
        else:
            print("{0} ,It's not a leap yer".format(year))


main()
