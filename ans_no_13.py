""" Program to write a comma separated value """

import csv

# user input
user_input = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

with open('student_details.csv', 'w') as test_file:
    file_writer = csv.writer(test_file)
    file_writer.writerow(['name', 'address', 'age'])

    for i in user_input:
        file_writer.writerow(i)
