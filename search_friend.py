""" Program to search the friend in the list """

friend_list = ['John']

def add_friend(friend):
    """ 
    Function to add the friends in list 
        Parameters:
            friend(str): name of friend
    """
    friend_list.append(friend)
    print(f'{friend} has been added')


def search_friend(friend):
    """
    Function to search the name of friend in the list
        Parameters:
            friend(str): name of friend
        
        Return:
            index(int): index of name in list
    """

    try:
        index = friend_list.index(friend)
        return index
    except ValueError:
        print(('Not Found'))

def display_all():
    """ Display all the friends in list. """
    return ', '.join(friend_list)


def main():
    """ main function """
    print('Choose the options:')
    print('1. Add a friend in list.')
    print('2. Search a friend in a list.')
    print('3. Display all friends.')
    while True:
        val = input('\nSelect: ')
        try:
            choice = int(val)
            break
        except ValueError:
            print('Only Integer Value is accepted.')

    if choice == 1:
        name = input('Enter the name of your friend.\n')
        add_friend(name)
    
    if choice == 2:
        name_search = input('Enter the name of your friend to search.\n')
        index = search_friend(name_search)
        print(f'{name_search} is in index {index}')

    if choice == 3:
        print(display_all())
    con = input('Do you want continue? Y/N: ').upper()
    if con == 'Y':
        main()

        
if __name__ == '__main__':
    main()



