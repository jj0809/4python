# from
# https://www.w3schools.com/python/python_dictionaries.asp

# dictionary 는 데이터 값을 키: 값의 쌍으로 저장할 때 주로 사용됨
"""
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020
}
print(thisdict) #year 가 2020으로 출력됨
print(len(thisdict)) # 3



thisdict = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1967,
    "colors" : ["red", "white", "black"]
}
print(type(thisdict)) # class<'dict'>


"""

thisdict = dict(name="joe", age= 35, country="kr")
# print(thisdict) # { } 형태로 출력됨
# thisdict["age"] = 24
# thisdict.update({"age": 25})
# thisdict.pop("age")
# thisdict.popitem() # 맨 마지막게 pop 됨
# del thisdict["age"]
# del thisdict # 전체 삭제
# thisdict.clear() # {} 출력

# print(thisdict)
"""
for x in thisdict:
   print(x) # keys
   print(thisdict[x]) # values
# for x in thisdict.keys():
#     print(x)
# for x in thisdict.values():
#     print(x)
for x, y in thisdict.items():
    print(x, y) # key value 출력

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

# @@@@@@@@@@@@@ if else @@@@@@@@@@@@@

a = 200
b = 33
c = 500
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("둘 중 하나 true일 때")
if not a > b:
  print("a is NOT greater than b")

x = 40
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



if b > a:
  pass


# @@@@@@@@@@@ while @@@@@@@@@

i = 1
while i < 5:
    print(i)
    i += 1 # i++ 불가

"""

a = True
b = True
c = True
if a and b == False:
    print("101")
elif a == False and b == False:
    print("102")
elif c == False:
    print("103")
else:
    print("done")