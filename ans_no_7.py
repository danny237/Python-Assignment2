""" Program that print the name followed by old or young
    if they are above or below the average age.
"""

friends = [
    ('Anish', 'Silwal', 22),
    ('Kishor', 'Ghising', 23),
    ('Sharwan', 'Ghimire', 21),
    ('Amrit', 'Maharjhan', 24),
    ('Alisha', 'Magar', 13),
    ('Alins', 'Magar', 12),
    ('Susan', 'Prajapati', None)
]

def remove_none_age(list1):
    """ function to remove age having value of none """

    list_wo_age_none = list(filter(lambda a: a[2] is not None, list1))
    return list_wo_age_none


def find_average(list1):
    """ function that return the sum of all items in list. """

    age_list = [int(i[2]) for i in list1 if i[2] is not None]
    average = sum(age_list) // len(list1)
    return average


def below_avg(list1, avg):
    """
    Function that return the list of friends below the average.
        Parameters:
            list1(list): listr of all friends
            avg(int): average value
        Return:
            below_avg_list(list): list below the average
    """

    below_avg_list = list(filter(lambda a: a[2] < avg, list1))
    return below_avg_list

def above_avg(list1, avg):
    """
    Function that return the list of friends above the average.
        Parameters:
            list1(list): listr of all friends
            avg(int): average value
        Return:
            below_avg_list(list): list above the average
    """

    below_avg_list = list(filter(lambda a: a[2] > avg, list1))
    return below_avg_list

def main():
    """ Main function to print below or below the average age. """

    def take_age(item):
        """ return third item """
        return item[2]

    print(f'List of friends:  {friends}\n')

    # removing the age having none value
    list_wo_none_age = remove_none_age(friends)

    # findeing average
    avg = find_average(friends)
    print('Average value:', avg, '\n')

    # list below the average
    below_avg_list = below_avg(list_wo_none_age, avg)
    # sort the list
    below_avg_list.sort(key=take_age)
    print(f'Below Average (in shorted order): {below_avg_list}\n')

    # list above the average
    above_avg_list = above_avg(list_wo_none_age, avg)
    above_avg_list.sort(key=take_age)
    print(f'Above Average (in shorted order): {above_avg_list}')

if __name__ == '__main__':
    main()
