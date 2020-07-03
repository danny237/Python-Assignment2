""" Program to check the given number is prime or not """

def is_prime(n):
    """
    Function to check prime number
        Parameter:
            n(int): integer

        Return:
            bool: True or False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

def main():
    """main function to check the prime"""

    while True:
        input_val = input('Enter the number: ')
        try:
            val = int(input_val)
            break
        except ValueError:
            print('Only Inter value acceptes. Please, Try again.')

    if is_prime(val):
        print(f'{val} is prime number.')
    else:
        print(f'{val} is not a prime number.')

if __name__ == '__main__':
    main()
