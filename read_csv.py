""" Program that reads csv file and return list of dictionary """

import csv

def main():
    """ main function """
    with open('student_details.csv', 'r') as file:
        csv_reader = csv.reader(file)
        new_list = []
        line_count = 0
        for i, row in enumerate(csv_reader):
            if i >= 1:
                dict1 = dict()
                dict1['name'], dict1['address'], dict1['age'] = row[0], row[1], row[2]
                line_count += 1
                new_list.append(dict1)
                # print(type(dict1))

    # pritn(type(new_list))
    print(new_list)
    print(f'Processed {line_count} lines')

if __name__ == '__main__':
    main()
