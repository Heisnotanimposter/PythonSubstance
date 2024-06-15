import os
from time import sleep
import sys

import human

rabit = 30
my = 20



if os.path.exists('./info.txt'):
    print("불러오기할 파일이 있습니다. 파일을 불러오시겠습니까?")
    print('1. 불러온다. 2. 새로 시작')

    choice = input()
    if choice == '1':

        #이름, 나이, 레벨, hp, mp
        f = open('./info.txt', 'r', encoding='cp949')

        line = f.readlines()
        f.close()
        # 이름, 나이, 레벨, hp, mp
        actor = human.Human(line[0].strip(), int(line[1].strip()), int(line[2].strip()), int(line[3].strip()), int(line[4].strip()))
        print("이름:{}, 나이:{}, 레벨:{}, hp:{}, mp:{}".format(actor.name, actor.age, actor.level, actor.hp, actor.mp))
        sleep(1)
        print("데이터 정보를 불러왔습니다.")
        sleep(1)
    else:
        print("새로 게임을 시작합니다.")
        sleep(1)
        print('이름을 입력해주세요 : ')
        name = input()
        sleep(1)
        print('나이를 입력해주세요 : ')
        age = input()
        sleep(1)

        actor = human.Human(name, age, 1, 30, 100)
        print("이름:{}, 나이:{}, 레벨:{}, hp:{}, mp:{}".format(actor.name, actor.age, actor.level, actor.hp, actor.mp))
        print("캐릭터 생성이 완료되었습니다.")
        sleep(1)
else:
    print('이름을 입력해주세요 : ')
    name = input()
    sleep(1)
    print('나이를 입력해주세요 : ')
    age = input()
    sleep(1)

    actor = human.Human(name, age, 1, 30, 100)
    print("이름:{}, 나이:{}, 레벨:{}, hp:{}, mp:{}".format(actor.name, actor.age, actor.level, actor.hp, actor.mp))
    print("캐릭터 생성이 완료되었습니다.")
    sleep(1)



print("{}님! 교통대 나라에 오신걸 환영합니다.".format(actor.name))
sleep(1.5)
print('강한 자만이 살아남는 이 곳에서 당신의 힘을 키워보세요')
sleep(1)
print('\n')
sel = ['1.계속한다', '2.나간다']
print(sel)
sel = input()
if sel == '2':
    print('게임에서 종료합니다.')
elif sel == '1':
    print('게임을 계속 진행합니다.')
    choice = 0

    while choice != '1':
        sel = ['1.밖으로 나간다.', '2.상황을 지켜본다']
        print(sel)
        choice = input()
        if choice == '1':
            print('야외로 나왔습니다.')
            break
        else:
            print("이곳에 계속 있을 생각인가?")

    print('\n')


    print("몽둥이가 있습니다.")
    sel = ['1.몽둥이를 챙긴다', '2.주인이 있겠지, 내버려 둔다.']
    print(sel)
    choice = input()


    if choice == '1':
        print('"혹시 모르니 챙겨놔야지..!"')
        print('\n\n')
        sleep(1)

        print("야생 토끼를 만났습니다!")
        while rabit > 0:
            sel = ['1.주먹 공격', '2.몽둥이 공격', '3.약올리기', '4.도망치기']
            print(sel)
            choice = input()
            if choice == '1':
                rabit -= 1
                print('토끼가 간지러워 합니다 -1. 토끼 HP = {}'.format(str(rabit)))
                sleep(1)

            elif choice == '2':
                rabit -= 10
                print('토끼가 고통스러워 합니다 -10. 토끼 HP = {}'.format(str(rabit)))
                sleep(1)
            elif choice == '3':
                rabit += 5
                print('토끼가 분노합니다 +5. 토끼 HP = {}'.format(str(rabit)))
                sleep(1)
            elif choice == '4':
                print('도망에 실패합니다.')
                sleep(1)
            else:
                print('잘못 선택하였습니다.')
                sleep(1)

            if rabit < 0:
                break

            actor.hp -= 3
            print("토끼의 공격에 나의 HP가 3 소모됩니다. 나의HP : {}".format(str(actor.hp)))
            print('\n')
            sleep(1)
            if actor.hp < 0:
                sleep(1)
                print('토끼와 싸움에 져서 게임에 종료됩니다.')
                break

        if actor.hp < 0:
            pass
        else:
            sleep(1)
            print('토끼를 잡았습니다. 레벨이 오릅니다!')
            print("레벨 up {} -> {}".format(actor.level, (actor.level + 1)))
            actor.level += 1
    elif choice == '2':
        print('"이건 점유물횡령이야! 그냥 두자!"')
        print('\n\n')
        sleep(1)

        print("야생 토끼를 만났습니다!")
        while rabit > 0:
            sel = ['1.주먹 공격', '2.약올리기', '3.도망치기']
            print(sel)
            choice = input()
            if choice == '1':
                rabit -= 1
                print('토끼가 간지러워 합니다 -1. 토끼 HP = {}'.format(str(rabit)))
                sleep(1)
            elif choice == '2':
                rabit += 5
                print('토끼가 분노합니다 +5. 토끼 HP = {}'.format(str(rabit)))
                sleep(1)
            elif choice == '3':
                print('도망에 실패합니다.')
                sleep(1)
            else:
                print('잘못 선택하였습니다.')
                sleep(1)

            if rabit < 0:
                break

            actor.hp -= 3
            print("토끼의 공격에 나의 HP가 3 소모됩니다. 나의HP : {}".format(str(actor.hp)))
            print('\n')
            sleep(1)
            if actor.hp < 0:
                sleep(1)
                print('토끼와 싸움에 져서 게임에 종료됩니다.')
                break

        if actor.hp < 0:
            pass
        else:
            sleep(1)
            print('토끼를 잡았습니다. 레벨이 오릅니다!')
            print("레벨 up {} -> {}".format(actor.level, (actor.level + 1)))
            actor.level += 1
    else:
        print("잘못 선택하여 게임에서 종료합니다.")

    sleep(1)
    print("데이터를 저장하시겠습니까? \n1. 저장, 2. 저장안함\n")
    choice = input()
    if choice == '1':
        f = open('./info.txt', 'w')



        """ 방법. 1
        f.write(actor.name)
        f.write(str(actor.age))
        f.write(str(actor.level))
        f.write(str(actor.hp))
        f.write(str(actor.mp))
        """

        # 방법. 2
        #f.writelines([actor.name, str(actor.age),  str(actor.level),  str(actor.hp),  str(actor.mp)])


        # 방법. 3
        f.writelines('\n'.join([actor.name, str(actor.age),  str(actor.level),  str(actor.hp),  str(actor.mp)]))

        f.close()


        print("데이터를 저장하였습니다. 게임을 종료합니다.")
    else:
        print("데이터를 저장하지 않습니다. 게임을 종료합니다.")

else:
    print("잘못 선택하여 게임에서 종료합니다.")

os.system('pause')


