# until
# https://www.w3schools.com/python/python_sets_methods.asp

""" 주석
if 5 < 2:
    print("5가 2보다 큼")
else  :
    print("아님")
    
x, y = str(3), 5
print(type(x)) #<class 'str'>
print(y)

fruits = ["apple", "banana", "grape"]
x, y, z = fruits
print(x, y, z)


x = "sf9"
def myfunc():
    global x #전역변수
    x = "fantasy"

print(x) #sf9
myfunc()
print(x) #fantasy

x = 20
print(type(x))
x = x + 0.4
print(type(x))


# 파이썬에서 cmd 실행하기
import subprocess

print("test start")
sudoPassword = 'telescope48'
subprocess.call('echo %s|sh kill.sh' % (sudoPassword), shell=True)
print("test done")


# -------- numbers ----------

x = 1
y = 395259034329487239858
z = -223948
print(type(x))
print(type(y))
print(type(z)) # all <class 'int'>

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z)) # all <class 'float'>
print(x, y, z ) # 35000.0 120000.0 -8.77e+101


x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z)) # type <class 'complex'>

import random

print(random.randrange(1, 10325))

# ---------- string -----------

# multiline strings
a = " " "wlekwnrlksl lkdmlrknwl 
w
g
w
clkldknql lkdmlrkn" " " 
a = '''wlkenlfk 
s
g
we
lknlg '''
print(a)

print(a)

a = "hello, world"
print(a[1]) # e

for x in "banana":
    print(x)


txt = "the best thins in life is free"
print("free" in txt) # true
if("free" in txt):
    print("yes, free is in txt")
print("apple" not in txt) # true

b = "Hello, World! "
print(b[-5:-2])  # wor. 뒤에서 다섯번째에서 뒤에서 두번째까지 출력

print(b.upper(), b.lower())
print(b.strip()) # 앞뒤 공백 제거
print(b.split(",")) # ['Hello','World! ']


q = 3
i = 567
p = 49.92
myorder= "i want to pay {2} dollars form {0} pieces of item {1}"
print(myorder.format(q, i, p))
print(bool(123)) #true
# False, None, 0, "", (), [], {} 를 넣으면 false 나옴
class myClass():
    def __len__(self):
        return 0
myobj = myClass()
print(bool(myobj))

x =200
print(isinstance(x, int))

x = 3
print(x < 5 or x < 4)


# ------ list --------

thislist = list(("apple", "banana", "cherry"))
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # orange kiwi melon

txt = "something applth skenrl"
if "th" in txt:
    print("true") #true

thislist = ["apple", "banana"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist.pop(1) #remove second item 
thislist.pop() #remove list item
del thislist[0] #remove first item
print(thislist)
del thislist #remove all

fruits = ["apple", "ten", "banana"]
newlist = [x for x in fruits] # apple ten banana
newlist = [x for x in range(10)] # 0 ~ 9
newlist = [x for x in range(10) if x < 5]
newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist) 
fruits.sort() # 알파벳순 정렬 fruits.sort(reverse=True) 역순
print(fruits)


def myfunc(n):
    return abs(n-50) # 절대값 함수
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) # 절대값이 작은 순서대로 정렬됨
print(thislist)


han = ["바나나", "사과", "가지"]
han.sort()
print(han) # 한글순 정렬됨

thislist = ["banana", "Orange", "kiwi", "Cherry"]
# thislist.sort(key=str.lower) # banana Cherry kiwi Orange
# thislist.sort(reverse=True) #kiwi banana Orange Cherry
# thislist.reverse() # Cherry kiwi Orange banana
# print(thislist)
# mylist = thislist.copy()
# mylist = list(thislist) # 위랑 동일함


list1 = ["a", "b", "c"]
list2 = [1,2,3]
list3 = list1 + list2
# print(list3) # ['a', 'b', 'c', 1, 2, 3]
# list1.extend(list2)
# print(list1) # ['a', 'b', 'c', 1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
print(len(list1))

# ---- 튜플 --------
thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon")
# print(thistuple)

nottuple = ("apple")
# print(type(nottuple)) # class 'str'
# print(thistuple[1]) # banana
# print(thistuple[:4]) # 4 부터 출력안함

x = ("apple", "banana", "cherry")
y = list(x) # ["apple", "banana", "cherry"]
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple=("apple", "banana")
y = ("orange",)
thistuple += y
print(thistuple)

# 튜플에서는 아이템 삭제가 불가능해서 list 로 바꿔서 지운다음 다시 튜플로 바꾼다
z = list(thistuple)
z.remove("banana")
thistuple = tuple(z)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #error

(r, g, b) = thistuple # unpacking
print(r)
print(b)
thistuple = ("apple", "banana", "cherry", "strawberry", "melon")
(r, g, *b) = thistuple
print(b) # ['cherry', 'strawberry', 'melon']

for i in range(len(thistuple)): # 자동으로 0 부터 늘어남...
    print(thistuple[i])
    print(i)


fruits = ("apple", "banana")
mytuple = fruits * 2
print(mytuple)


# ------ set ---------

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # apple banana cherry
# set은 중복 불가

set1 = {"ab", 123, True, "w3r4f"}
print(set1)
set2 = set(("this is another", "way to make", "a set"))
for x in set2:
    print(x)
print("a set" in set2) # true
print("set" in set2) # false


thisset = {"apple", "banana", "kiwi"}
# thisset.remove("cherry")
# print(thisset)
# thisset.discard("cherry") 
print(thisset) 
# remove는 삭제할 아이템이 없으면 오류
# discard는 삭제할 아이템이 없어도 ㅇㅋ

x = thisset.pop()
print(x) # kiwi 출력
print(thisset) # {apple, banana} 출력

# thisset.clear()
# print(thisset) # set() 라고 출력됨

del thisset
print(thisset) # naem 'thisset' is not defined 출력


set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3) # 순서 무작위
set1.update(set2)
print(set1) # set3과 동일함


x = {"apple", "banana", "cherry"}
y = {"google", "naver", "apple"}
# x.intersection_update(y)
# print(x) # {'apple'} 중복 값만 출력하는듯..
# z = x.intersection(y) # 중복 값의 새로운 set를 출력함
# print(z)
# x.symmetric_difference_update(y)
print(x) #{'naver', 'banana', 'cherry', 'google'}
# 중복값을 뺴고 합치는듯..
z = x.symmetric_difference(y)
print(z) # 역시 set 반환



x = {"apple", "banana", "cherry", False}
y = {"google", 1, "apple", 2, 0}

z = x.symmetric_difference(y)
print(z) # True == 1 / False == 0
"""