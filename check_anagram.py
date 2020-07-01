""" Program that checks the given two strings are anagram or not """

def check_anagram(str1, str2):
    """
    Check the length of two args, if not equal return False.
    Take two args and return True if anagram otherwise False.

        Parameters:
            str1(string): first string
            str2(stirng): second string

        Returns:
            True(bool): if anagram
            false(bool): if not anagram
    """

    if len(str1) != len(str2):
        return False
    list_str1 = (list(str1)).sort()
    list_str2 = (list(str2)).sort()
    return list_str1 == list_str2

# main function
def main():
    # user input untile it is string
    user_input1 = input('Enter the first string to check anagram: ')
    user_input2 = input('Enter the second string to check anagram: ')

    # display the result
    if check_anagram(user_input1, user_input2):
        print('The given strings are anagram.')

    else:
        print('The given strings are not anagram.')

if __name__ == '__main__':
    # execute only if run as a script
    main()
