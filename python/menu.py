#menu.py
#22/05/16
#2245051 2학년 이승원
from number import Number
from myCalculator import Calculator

def menu():
    menu = ('더하기', '빼기', '곱하기', '나누기', '나머지', '계수', '지수')
    calculator = Calculator()

    for i in range(20):
        print("도움이 필요하면 /h 또는 /help를 누르십시오.")
        print("종료하려면 /q를 입력하세요.")
        menu.printMenu()

        userinput = input("입력: ")
        if userinput in ['/h', '/help']:
            print(menu)
            print(Number(0))
        elif userinput == '/q':
            break
        else:
            try:
                userinput = int(userinput) - 1
                if userinput not in range(len(menu.options)):
                    raise ValueError
                num1 = Calculator.get_operand("1번째 숫자")
                num2 = Calculator.get_operand("2번째 숫자")

                operator_map = {0: '+', 1: '-', 2: '*', 3: '/', 4: '//', 5: '%', 6: '**'}
                operator = operator_map[userinput]
                result = Calculator.perform_operation(operator, num1, num2)

                print(f"결과: {result.value}")

            except ValueError:
                print("에러발생, 다시 시도해보세요.")
