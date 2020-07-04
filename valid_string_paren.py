"""Program to valid a string of parenthese."""

class Parenthese:
    """
    Class for validating parenthese
    Attribute:
        str1(string): given parentheses
    """
    def __init__(self, str1):
        self.str1 = str1

    def is_valid(self):
        """function that return True if valid parenthese"""
        stack = []
        para_char = {"(": ")", "{": "}", "[": "]"}
        for parenthese in self.str1:
            if parenthese in para_char:
                stack.append(parenthese)
            elif len(stack) == 0 or para_char[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

# user input
user_input = input('Enter the string of parenthesse: ')
obj = Parenthese(user_input)
if obj.is_valid():
    print('Valid.')
else:
    print('Not Valid.')
