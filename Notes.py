'''
printing and taking input
'''
print("Devendra")
input("Whats your name")
print(len(input("whats your name")))

print("2 + 3 = ", int(3/2))


#String

myString = "My Name is Devendra"
print(myString.upper())
print(myString.lower())
print(myString.split())

#slicing and indexing
print(myString[7])
print(myString[:6:])
print(myString[4::10])
print(len(myString))
print(myString[1:17:2])


print('my name is {0}'.format('name'))
print('the {2} {0} {1}'.format('fox','brown','quick'))
print('the {q} {b} {f}'.format(f='fox', q='quick', b='brown'))

result = 100/777
print(result)
print("The result is {}".format(result))
print('The result is {:1.3f}'.format(result))

#-----------------------------------------
#List

#  object retrieve by location
# it an ordered sequence and can be indexed or slicing

mylist = [1,2,3]
print(mylist)

print(mylist[2])

mylist.append(4)
print(mylist)

mylist1 = [1,2,3,4,5]
mylist2 = [6,7,8]
mylist = mylist2 + mylist1
print(mylist)

print(len(mylist))

mylist.pop()
print(mylist)

#pop to exact location

mylist.pop(2)
print(mylist)

mylist.sort()
sortedList = mylist
print(sortedList)

#Dictonary

#it a key value pair
# it is unordered and we can't sort a dictonary

mydict = {'key1': 'value1', 'key2': 'value2'}
print(mydict['key1'])


d= {'k1': 123, 'k2': [1,2,3], 'k3': {'insidekey': 100}}
print(d['k2'])
print(d.keys())
print(d.values())

#----------------------------
#Tuples
# Tuples are similar to list but immutable
#(1,2,3)

myTuple = (1,2,3)
print(myTuple)
print(type(myTuple))
myTuple = ('apple','banana','grapes')
print(myTuple.count('banana'))

myTupleIndex = ('apple', 'apple', 'banana', 'banana', 'grapes')
print(myTupleIndex.index('apple'))
print(myTupleIndex.index('banana'))

#------------------
#Sets
#Sets are unordered collection of unique elements


mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)

mylist = [1,1,1,2,3,2,3,2,3]
print(set(mylist))

'''
--------------------------------------
IF elif Else
'''
a,b,c = 7,8,9
if a>b & a > c:
    print('a')
elif b > a & b > c:
    print('b')
else:
    print('c')

'''
-------------------------------------
For loop
'''
array = [1,2,3,4,5,6,7,8,9,10]
for jelly in array:
    print(jelly,end = '\t')
print('\n')
myDict = {'fruit': 'apple', 'k1': [1,2,3,4], 'k3': {'k4': 'banana'}}
for key,value in myDict.items():
    print(key,value, end='\t')
print('\n')
mylist = [(1,2),(3,4),(5,6),(7,8)]
for jelly in mylist:
    print(jelly)

'''
----------------------------
while loop
'''

x=0
while x<5:
    print('x is less than 5')
    x+=1
else:
    print('not less than 5')

'''
----------------------------
break - come out of the current loop
continue - goes back to the current loop
pass - do nothing
'''

myString = "Sammy"
for letter in myString:
    if letter == 'a':
        pass
print("end of script") #if we will not write pass it will show error stating the loop is not complete, not it will print end of script

'''
----------------------------------------
continue
------------------------------------
'''
myString = "Sammy"
for letter in myString:
    if letter == 'a':
        continue
    print(letter)

'''
----------------------------------------
break
------------------------------------
'''
myString = "Sammy"
for letter in myString:
    if letter == 'a':
        break
    print(letter)

'''
-------------
-----------
Methods
----------
'''
def say_hello():
    print("Hello")

say_hello()

def say_name(name):
    print(f'Hello {name}')

say_name('John')

#or

def say_name(name = "john"):
    print(f'hello {name}')

say_name()

def add(num1,num2):
    return num1 + num2

result = add(2,3)
print(result)


def even_chk(num):
    result = num % 3 == 0
    return result

print(even_chk(17))


def chk_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
print(chk_even_list([1,2,3,4,5]))
print(chk_even_list([1,7,3]))































