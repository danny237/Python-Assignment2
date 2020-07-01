""" Program to append friends to a list. """

class ColleagueFriend:
    """
    This is a class for adding and displaying the list items
    """

    def __init__(self):
        """ Constructor for initilizing empty list """
        self.list1 = []

    @property
    def sort_list(self):
        """ Function to sort the list """
        return self.list1.sort()

    def add_friend(self, item):
        """ function that add the item """
        self.list1.append(item)

    def display_all(self):
        """ function that return list """
        return self.list1

    def individual_friend(self, index):
        """ function that display individual list item """
        self.sort_list
        return self.list1[index]

# creating object
college = ColleagueFriend()

# main
def main():
    """Option to choose from given list"""
    print('**************')
    print('1. Append Friend.\n2. Display all_friends.')
    print('3. Display the individual (select the index of item)\n')

    # run until the answer is n/N (no)
    while True:
        val = input('Select: ')
        try:
            choice = int(val)
            break
        except ValueError:
            print('You have selected 1.')
            print('Accepts only integer value.\nPlease select again.\n')
    if choice == 1:
        name = input('Enter the name of your friend: ')
        college.add_friend(name)
    elif choice == 2:
        print('You have selected 2. \nYour friends in sorted order are: ')
        all_friends = college.display_all()
        all_friends.sort()
        for i, j in enumerate(all_friends):
            print(i, '.', j)
    elif choice == 3:
        print('You have selected 3')
        while True:
            college.sort_list
            print('Your Friends are: ', college.list1)
            index = int(input('Enter the index of friend.'))
            try:
                friend = college.individual_friend(index-1)
                print(friend)
                break
            except ValueError:
                print('Out of range / Doesn\'t have any in given index.')

    last_choice = input('Do you want to continue? Y / N: ').upper()
    if last_choice == 'Y':
        main()


if __name__ == '__main__':
    main()
