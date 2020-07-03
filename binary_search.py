""" Binary search """

# List of number
list1 = [-3, 0, 1, 3, 6, 7, 8, 9]

def binary_search(list1, n):
    """
    Function for binary search
        Parameters:
            list1(list): list of item
            n(int): integer to search
        Return:
            index(int): index of search element
    """
    index = -1
    L = 0
    R = len(list1) - 1
    print('Length of list : ', R)
    while L <= R:
        mid = (L+R) // 2
        if list1[mid] == n:
            return mid
        else:
            if list1[mid] < n:
                L = mid + 1
            else:
                R = mid -1

    return index


def main():
    while True:
        input_val = input('Enter the number to search in list: ')
        try:
            val = int(input_val)
            break
        except ValueError:
            print('Only Inter value acceptes. Please, Try again.')

    returned_index = binary_search(list1, val)
    if returned_index == -1:
        print('Value not found.')
    else:
        print(f'Index of {val} in list is {returned_index}')

if __name__ == '__main__':
    main()