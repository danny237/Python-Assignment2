""" Program to check the given word is palindrome or not """

# check using reverse method
# def is_palindrome(str1):
#     reverse_string = list(reversed(str1))
#     if list(str1) == reverse_string:
#         return True
#     else:
#         return False


def is_palindrome(str1):
    """
    Function to check palindrome
        Parameter:
            str1(string): given string
        Return:
            Boolean: True or False
    """
    length = len(str1)
    middle = length // 2
    for i in range(middle):
        if str1[i] != str1[length-i-1]:
            return False
        return True

def main():
    """ Main Function """

    # user input
    user_input = input('Enter the string: ')
    if is_palindrome(user_input):
        print(user_input, ' is palindrome.')
    else:
        print(user_input, ' is not palindrome.')

if __name__ == '__main__':
    main()
