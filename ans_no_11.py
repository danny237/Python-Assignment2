""" Program that return the file name without extension. """

def remove_extension(str1):
    """
    Function to remove extension
        Parameter:
            str1(string): given input string
        Return:
            file_name(string): file name in string
    """

    file_name = str1.split('.')
    return file_name[0]

# user input
filename = input('Enter the name of file: ')
filename_wo_extension = remove_extension(filename)
print(filename_wo_extension)
