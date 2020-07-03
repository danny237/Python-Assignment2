""" Program that serves as a basic calculator """

class Calculator:
    def __init__(self, first, second):
        self.first = first 
        self.second = second

    @property
    def add(self):
        """return addition of two number"""
        return self.first + self.second

    @property
    def sub(self):
        """ Subtraction """
        return self.first - self.second

    @property
    def mul(self):
        """ Multiplication """
        return self.first * self.second


    @property
    def div(self):
        """ Division """
        try:
            ans = self.first / self.second
            return ans
        except ZeroDivisionError:
            print('Cant divide by 0')


def main():
    """ main function """

    print('\nEnter the space separated value.')
    print('(operand) (operator) (operand)')
    print('Example: 10 + 10\n')
    while True:
        
        # validation that the input is integer
        while True:
            x, op, y = [i for i in input().strip().split()]
            try:
                x, y = int(x), int(y)
                break
            except ValueError:
                print('Enter valid number.')

        obj = Calculator(x, y)
        
        if op not in '+-*/':
            print('Calculation not valid.')
            main()
        elif op == '+':
            print('Addition:', obj.add)
        elif op == '-':
            print('Subtract: ', obj.sub)
        elif op == '*':
            print('Multiplication: ', obj.mul)
        elif op == '/':
            print('Division: ', obj.div)
    
        do_continue = input('Continue ? Y / N').upper()
        if do_continue == 'Y':
            main()
        else:
            break

if __name__ == '__main__':
    main()