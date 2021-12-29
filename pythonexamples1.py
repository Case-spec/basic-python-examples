#list are mutable
lst=[1,4, "python", 2, 7, 9]
print(lst)
lst[1]="Hello"
print(lst)
lst.append("Simplilearn")
print(len(lst))
print(lst)
#nested list
nested= [1,4,[3,7,5]]
print (nested)
nested.extend([[7,4, 9]])
print(nested)
#tuples
tpl=(2,5,4)
print(tpl)
#tuples are immutable
#accessing values
print(tpl[1])
a, b, c= tpl
print(a, b, b)
a, *lst= tpl
print(a, lst)
#sets
s={1, 4 ,5 ,7}
print(s)
#arithmetic operators
a,b=10, 5
print('a+b', a+b)
print('a-b', a-b)
print('a*b', a*b)
print('a/b', a/b)
print('a%b', a%b)
print('a**b', b**2)
count=0
count +=2
print(count)
#above works for all basic arithmetic operators
#relational operators
a,b = 10, 5
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
#bitwise operator
a, b= 10, 5
print(bin(a),bin(b))
print(a & b)
#membership operators
lst=[1,3,2,4,6]
x=2
print(x in lst)
print(x not in lst)
#identity operators
x=10
y=10
print(x ==y)
#non basic operators examples
import math
print(math.pi)
x=9.5
y=3
print(math.pow(x, y))
#inline input
name=input("Enter your name\n")
print("Hi", name)
age=input("Enter your age\n")
print(age)
print("%s is %d years old"%(name, int(age)))

#if, while, for, break, continue
a= int(input("Enter a number"))
if a%2!=0:
   print (a, "this is an odd number")
else:
    print(a, "is an even number")
a= int(input("Enter a number"))
b= int(input("Enter a number"))
c= int(input("Enter a number"))
if a>b and a>c:
    print(a, 'is the greatest number')
elif b>a and b>c:
    print(b, 'is the greatest number')
else:
    print(c, 'is the greatest number')
age= int(input("Enter your age"))
if age>= 60:
    print("You are eligible for senior citizen discount")
else:
    print("You are not eligible for any discount")
word= "Python"
i=0
while i<=5:
    print(i, word)
    i+=1
word= "Python"
for w in range(0,3):
    print(w, word)
n=49
for i in range(2, n//2+1):
    if  n%i==0:
        print(n, "is not a prime number")
        break
    
#arrays and numpy
from array import*
ar=array('i', [1,2,3,4,5])
print(type(ar))


#functions
def fun():
    print("Simplilearn")
fun()
def add(a,b):
    s=a+b
    d=a-b
    return s, d
n1, n2=add(4,5)
print (n1, n2)

#functions  --recursive
def rec(n):
    if n==1:
        print (n)
        return
    print (n)
    return rec(n-1)
rec(3)
def fact(n):
   f=1
   for i in range (1, n+1):
    f *=i
    return f
fact(3)

#lambda filter, map
l=lambda a,b :a+b
print (l(10,20))
lst=['a', 'b', 'e', 'f', 'o', 'a']
l= list(filter(lambda x:x in ['a', 'e', 'i', 'o', 'u'],lst))
print(1)
#map0
result=map(lambda x:chrord(x)+1, lst)
print(list(result))
#reduce
#concentate all elements of the list
from functools import reduce
result= reduce(lambda  x,y:x+y,lst)
print (result)

#OOP- Object Oriented Programming
class car:
    cartype= "manual"  #global feature
    def _init_(self, year, speed):
        self.year=year #instance feature
        self.speed=speed
        @staticmethod
        def welcome():
            print("Welcome to the car showroom")
            @classmethod
            def type(cls):
                print("These cars are", cls.carType)
                def getSpeed(self):
                    print("Maximum speed is", self.speed)
    
BMW= car(2018, 155)
Ford= car(2016, 140)
car.type()
Ford.getSpeed()
            
                    
                       
