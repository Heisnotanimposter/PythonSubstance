#week10.pyweek10.py
#22/05/11
#2245051 2학년 이승원

#object and class

class ClassName:
  pass
class ClassName(object) :
  pass

dir(object)

class Cat:
    def __init__(self, name, color):
        self.__name=name
        self.color=color
    def __str__(self):
        return f"여기는 __str__()입니다. 나는 클래스 Cat의 객체 {self.color} 고양이 {self.__name}입니다."

tom=Cat("톰","하양")
print(str(tom))
print(tom)

class Dog:
    def __init__(self, name, color):
        self.__name=name
        self.color=color
    def __repr__(self):
        return f"여기는 str()입니다. 나는 클래스 Dog의 객체 {self.color} 강아지 {self.__name}입니다."

baDugI=Dog("바둑이","하양")
print(repr(baDugI))
print(baDugI)

class strNrepr(object):
    def __str__(self):
        return f'여기는 __str__() 메서드입니다.'
    def __repr__(self):
        return f'여기는 __repr__() 메서드입니다.'

a = strNrepr()
b = strNrepr()
print(str(a))
print(repr(a))
print(a)

class Person:
    def __init__(self,name):
        self.__name=name
    @property
    def Name(self):
        return self.__name
def WhoAreYou(self):
        print(f"여기는 class Person의 WhoAreYou() 메서듭니다. 내 이름은"
             +"{self.Name}입니다. 반갑습니다. ")
def __repr__(self):
    repr1= f"나는 클래스 Person의 객체 {self.Name}입니다."\
        + "\n나를 좋아하지도 미워하지도 마세요."\
        + "\n이 몸은 번뇌의 근원이나니"\
        + "\n나를 미워해 보았자..."
    return repr1

gilDong= Person("홍길동")
print(gilDong)

class Mammal:
    def __init__(self, name,color):
        self.name = name
        self.color = color
class Dog(Mammal):
    def __init__(self, name, color):
        super().__init__(name,color)
    def __str__(self):
        return "종류:강아지, 이름:{0}, 색깔:{1}".format(self.name, self.color)
    def Bark(self):
        print("{0}는 멍멍 짖습니다.".format(self.name))
class Cat(Mammal):
    def __init__(self, name,color):
        super().__init__(name,color)
    def __str__(self):
        return "종류:고양이, 이름:{0}, 색깔:{1}".format(self.name, self.color)
    def Meow(self):
        print("{0}는 야옹~ 하고 웁니다.".format(self.name))

tom=Cat("톰","하양")
print(tom)
baDugI=Dog("바둑이","하양")
print(baDugI)

class Poetry:
    def __init__(self, title, poet, contents):
        self.__title=title
        self.__poet=poet
        self.__contents=contents

    def __repr__(self):
        repr1= f"이 시는 {self.__poet}님의 {self.__title}이란 시입니다."\
            + f"\n{len(self.__contents)} 줄로 이루어진 시이고요, 첫 소절은 이렇게 시작합니다."\
            + f"\n{self.__contents[0]}..."
        return repr1

title = "그리움"
poet = "유치환"
contents = ["파도야 어쩌란 말이냐", "파도야 어쩌란 말이냐",
          "임은 뭍같이 까딱 않는데", "파도야 어쩌란 말이냐", "날 어쩌란 말이냐"]
myPoetry=Poetry(title, poet, contents)
print()
print(myPoetry)

class Double(object):
    def __init__(self, value):
        self.value = value
    def __add__(self, number):
        return self.value * 2 + 2 * number
    def __sub__(self, number):
        return self.value * 2 - 2 * number
    def __mul__(self, number):
        return self.value * 2 * 2 * number
    def __truediv__(self, number):
        return self.value * 2 / (2 * number)

d= Double(10)
print(f'10 + 3 = {d + 3}')
print(f'10 - 4 = {d - 4}')
print(f'10 * 5 = {d * 5}')
print(f'10 / 6 = {d / 6}')

class Test:
    def __repr__(self):
        return str(id(self))

a = Test()
print(a)

class Test:
    def __repr__(self):
        return str(id(self))

class NewInt(Test, int):
    pass

int1= NewInt(5)
print(int1)
print(int1 + 5)
print(str(int1))
print(repr(int1))

help(repr)

class ChaosNumber(object):
    def __init__(self, data):
        self.data=data
    def __add__(self, other):
        return  self.data * other.data
    def __neg__(self):
        return self.data * -1000
    def __gt__(self, other):
        return self.data <= other.data
    def __le__(self, other):
        return self.data > other.data
    def __ne__(self, other):
        return self.data == other.data
    def __eq__(self, other):
        return self.data != other.data
    def __str__(self):
        return str(self.data)

a = ChaosNumber(20)
b = ChaosNumber(10)
print(f'ChaosNumber a = {a}')
print(f'ChaosNumber a가 {a}일 때'+' - {(a)} =  {-a} : '+f"- {(a)} =  {-a}")
print(f'ChaosNumber a가 {a}, b는 {b}일 때, a + b = {a+b}')
print(f'ChaosNumber a가 {a}, b는 {b}일 때, a > b = {a>b}')
print(f'ChaosNumber a가 {a}, b는 {b}일 때, a <= b = {a<=b}')
print(f'ChaosNumber a가 {a}, b는 {b}일 때 a != b = {a!=b}')
print(f'ChaosNumber a가 {a}, b는 {b}일 때 a == b = {a==b}')

"""
ChaosNumber a = 20
ChaosNumber a가 20일 때 - {(a)} =  {-a} : - 20 =  -20000
ChaosNumber a가 20, b는 10일 때, a + b = 200
ChaosNumber a가 20, b는 10일 때, a > b = False
ChaosNumber a가 20, b는 10일 때, a <= b = True
ChaosNumber a가 20, b는 10일 때 a != b = False
ChaosNumber a가 20, b는 10일 때 a == b = True
"""

#inheritance

class BaseClass:
  {
    # 멤버 선언
}
class DrivedClass(BaseClass):
  {
    # 아무 멤버를 선언하지 않아도 
    # 기반 클래스의 모든 것을 물려받아 갖게 됩니다.
}

class Base:
  def BaseMethod(self):
    print("나는 기반클래스의 BaseMethod입니다." )

class Derived(Base):
     pass

myBase= Base()
myBase.BaseMethod()
myDrived=Derived()
myDrived.BaseMethod()

class Base:
    def _BaseMethod(self):
        print( "나는 기반클래스의 BaseMethod입니다." )
    def BaseMethod(self):
         self._BaseMethod()

class Derived(Base):
    def BaseMethod(self):
        super()._BaseMethod()

myBase= Base()
myBase.BaseMethod()
myDrived=Derived()
myDrived.BaseMethod()

class Base:
    def __init__(self,  name   ):
        self.__a=a

class Drived(Base):
    def __init__(self, name):
        super().__init__(name)

class X:
    def __init__(self,  a):
        self.a=a
class Y(X):
    def __init__(self, a, b):
        self.b=b
        super().__init__(a)
class Z(Y):
    def __init__(self, a, b, c):
        self.c=c
        super().__init__(a, b)

myData= X(1000)
print("myData= X(100) a={myData.a}")
myData= Y(100,200)
print("myData= Y(100,200) a={myData.a}, b={myData.b}")
myData= Z(10,20,30)
print("myData= Z(10,20,30) a={myData.a}, b={myData.b}, c={myData.c}")

class X:
    def __init__(self):
        self._i=10
        self.message='나는 X입니다.'
    def _print(self):
        print(self.message)
    def _play(self):
        print('Play..'+ self.message)

class Y(X):
    def __init__(self):
        self._i=20
        self.message='나는 Y입니다.'
    def _print(self):
        print(self.message)

class Z(Y):
    def __init__(self):
        self._i=30
        self.message='나는 Z입니다.'
    def _print(self):
        print(self.message)
    def _play(self):
        print('Play..'+ self.message)
    def doZ(self):
        print('Z안에서 작업중입니다.')
    def test(self,i):
        x=X()
        x._print()
        x._play()
        print('x.i='+str(i))
        print('x._i='+str(x._i))     
        y=Y()
        y._print()
        y._play()
        print('y.i='+str(y._i))

#class Z(Y):
def test(self,i):
        z=Z()
        y=z
        x=z
        z._print()
        y._print()
        x._print()
        z._play()
        y._play()
        x._play()

        #super()._print()
        self._play()
        #super()._play()
        print('i='+str(i))
        print('y._i='+str(y._i))
        print('x._i='+str(x._i))
        print('z._i='+str(z._i))

class Mammal:
    def __init__(self, name):
        self._name = name
    def Nurse(self):
        print("{0}는 수유동물입니다.".format(self._name))
class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)
    def Bark(self):
        print("{0}는 멍멍 짖습니다.".format(self._name))
class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)
    def Meow(self):
        print("{0}는 야옹~ 하고 웁니다.".format(self._name))

myMammal=Mammal("포유동물")
myMammal.Nurse()
myDog=Dog("바둑이")
myDog.Nurse()
myDog.Bark()
print()
myCat=Cat("네로")
myCat.Nurse()
myCat.Meow()
print()
myMammals=[myMammal, myDog, myCat]
for myMammal in  myMammals:
    myMammal.Nurse()
    if isinstance(myMammal, Dog):
        myMammal.Bark()
    if isinstance(myMammal, Cat):
        myMammal.Meow()
    print()

myMammals=[myMammal, myDog, myCat]
for myMammal in myMammals:
  myMammal.Nurse()
  myMammal.Bark()
  myMammal.Meow()
  print()

myMammals=[myMammal, myDog, myCat]
for myMammal in myMammals:
  myMammal.Nurse()
  if isinstance(myMammal, Dog):
    myMammal.Bark()
  if isinstance(myMammal, Cat):
    myMammal.Meow()
  print()

class A:
  pass

class B:
  pass
class C:
  pass
class D(A, B, C):
  pass

class Tiger:
  def __init__(self):
    self._name="엄마"
  def WhoAreYou(self):
    print( "나는 {0}클래스 Tiger 입니다.".format(self.name))
class Lion:
  def __init__(self):
    self._name="아빠"
  def WhoAreYou(self):
    print( "나는 {0}클래스 Lion 입니다.".format(self.name))
class Liger(Tiger, Lion):
  def __init__(self):
    self._name="아가"
  def WhoAreYou(self):
    print( "나는 서브클래스 Liger {0}입니다.".format(self.name))
    super().WhoAreYou()

class A:
  def method(self):
    print("A")
class B(A):
  def method(self):
    print("B")
class C(A):
  def method(self):
    print("C")
class D(B, C):
  pass

myDiamond=D()
myDiamond.method()

class Ridable:
  def Ride():
    pass
class Car(Ridable):
  def Run(self):
    print("Run!!!")
  def Ride(self):
    self.Run()
class Plane(Ridable):
  def Ply(self):
    print("Ply!!!")
  def Ride(self):
    self.Ply
class myVehicle(Car,Plane):
  def __init__(self):
    super().Ride()

