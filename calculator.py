#calculator.py  
#22/04/10
#2245051 2학년 이승원

class Calculator:
    def __init__(self):
        self.operators = {
            "0": self.plus,
            "1": self.minus,
            "2": self.multiply,
            "3": self.divide,
            "4": self.quotient,
            "5": self.remainder,
            "6": self.pow,
        }

    def get_operand(self, message):
        operand=input('\t' + message + ' : ')
        isValidNumber=False
        while not isValidNumber:
            list1=operand.split('.')
            if len(list1) == 1:
                if not list1[0].isdigit():
                    print('\t숫자가 아님')
                else:
                    isValidNumber=True
                    number= int(operand)
            elif len(list1) > 2:
                print('\t점 많음 에러~')
            elif not list1[0].isdigit():
                print('\t점 앞이 숫자가 아님')
            elif not list1[1].isdigit():
                print('\t점 뒤가 숫자가 아님')
            else:
                isValidNumber=True
                number= float(operand)
            if not isValidNumber:
                operand=input('\t' + message + ' : ')
        return Number(number)

    def perform_operation(self, operation, a, b):
        return self.operators[operation](a, b)

    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b.value == 0:
            raise ValueError('0 나눔 오류')
        return a / b

    @staticmethod
    def quotient(a, b):
        return a // b

    @staticmethod
    def remainder(a, b):
        return a % b

    @staticmethod
    def pow(a, b):
        return a ** b
