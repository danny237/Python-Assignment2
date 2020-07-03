""" Program that take camelcase case string and convert to snake case """


def camel_to_snake(str1):
    """
    Function to convert camel case to snake case
        Parameter:
            str1(string): camel case string
        Return:
            snake_case(string): snake case string
            kebab_ccase(string): kebab case string
    """

    camel_case = list(str1)
    snake_case = [camel_case[0].lower()]
    for i in range(1, len(camel_case)):
        char = camel_case[i]
        if char.islower():
            snake_case.append(char)
        else:
            snake_case.append('_')
            snake_case.append(char.lower())
    snake_case_string = ''.join(snake_case)
    kebab_case_string = snake_case_string.replace('_', '-')
    return snake_case_string, kebab_case_string

def main():
    """ main function """

    # user input
    user_input = input('Enter the string: ').strip()

    snake_case, kebab_case = camel_to_snake(user_input)
    print('String in snake case: ', snake_case)
    print('String in kebab case: ', kebab_case)


if __name__ == '__main__':
    main()
