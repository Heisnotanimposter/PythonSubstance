import os
from calculator import Plus, Minus, Multiply, Divide, Quotient, Remainder, Pow, getOperand
from myCalculator import printMenu,getValidNumber,printResult

menuTitle = '내가 만든 계산기 프로그램'
menuContents = ['더하기', '빼기', '곱하기', '나누기', '몫 구하기', '나머지 구하기', '승 구하기']
operator = ['+', '-', '*', '/', '//', '%', '**']
myCalc = [Plus, Minus, Multiply, Divide, Quotient, Remainder, Pow]

command = input('명령을 입력하세요: "\n" 1./h,/? : 도움말 보기 "\n"2.a버튼을 입력하면 프로그램이 시작됩니다.')
if command == '/?' or command == '/h':
    print('이 프로그램은 두 수를 입력받아 더하기, 빼기, 곱하기, 나누기, 몫구하기, 나머지 구하기, 승 구하기 연산을 수행합니다.')
    print('프로그램 제작자: 이승원')
    print('제작일: 2022년 4월 10일')
else:
    printMenu(menuTitle, menuContents)
    menuNumber = getValidNumber(menuContents)
while menuNumber != str(len(menuContents) + 1):
    operand1 = getOperand('첫 번째 피연산자를 입력하세요')
    operand2 = getOperand('두 번째 피연산자를 입력하세요')
    printResult(operand1, operand2, operator[int(menuNumber) - 1], 
                myCalc[int(menuNumber) - 1](operand1, operand2))