
#myCalculator.py
#22/04/10
#2245051 2학년 이승원

import os

def printMenu(title, contents):
    os.system('cls')
    print('\n'*3)
    print('\t\t'+title)
    i=0
    print('\n'*2)
    for content in contents:
        print('\t',end='')
        i+=1
        print(i,end='. ')
        print(content)
        print()

    print('\t',end='')
    print(len(contents)+1,end='. ')
    print('종   료')
    print('\n'*2)
    print('\t원하는 번호를 선택하세요  : ',end='')

def getValidNumber(contents):
    menuNumber=input()
    while menuNumber not in [str(i) for i in range(1, len(contents)+2)]:
        print('\t입력한 메뉴번호가 틀렸습니다. ')
        menuNumber=input()
    return menuNumber

def printResult(operand1,operand2,operator,result):
    print(f'\t{operand1} {operator} {operand2} = {result}')


