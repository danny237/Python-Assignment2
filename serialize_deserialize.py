"""Program to serialize and deserialize JSON"""
import json

person1 = {
    'name': 'Daniel Thapa',
    'age': 22
}

with open('about_me.json', 'w') as f:
    json.dump(person1, f)

detail = open('about_me.json', 'r').read()
print(detail)
print('type of file:', type(detail))

print('\n')

with open('about_me.json', 'r') as f:
    person = json.load(f)

print(person)
print(type(person))
