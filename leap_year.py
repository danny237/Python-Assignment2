""" Program to check whether the given year is leap or not. """

def check_leap(year):
    """
    Returns True if it is leap year otherwise False.
        Parameter:
            year(int): Given year
        Returns:
            True(bool): if leap year
    """

    if ((year % 400 == 0) or ((year % 4 == 0) & (year % 100 != 0))):
        return True
    return False

# User Input
# It will ask for input until the integer value is provided.
while True:
    num = input('Please, enter the year to check whether it is leap year or not: ')
    try:
        val = int(num)
        break
    except ValueError:
        print('Given input is not number. Please enter a valid number.')

# function call and print result
if check_leap(val):
    print('It is leap year.')
else:
    print('Its is not a leap year.')
