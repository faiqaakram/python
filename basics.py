<<<<<<< HEAD
#using print function
print("Hello,user!")
print("I am faiqa","my age is 23")
print(23)
print(23+35)

#Variable
name="Faiqa"
age=19
networth="$0"
price=23.33

#Printing above variables
print(name)
print(age)
print(networth)
print(price)
print("my name is:",name)

#Print type of variables
print(type(name))
print(type(age))
print(type(price))
print(type(networth))

#Data types
#1. INTEGER
PRICE=100
PROFIT=0
LOSS=-2
print(type(PRICE))
print(type(PROFIT))
print(type(LOSS))

#2. String
name1='faiqa'
name2="manaal"
name3='''aleena'''
print(type(name1))
print(type(name2))
print(type(name3))

#3. Float
price=3.99
print(type(price))

#4. Boolean
old=False
print(type(old))
young=True
print(type(young))

#5. None
a = None
print(type(None))

#Printing sum
a=2000
b=3500
sum=a+b
print(sum)

#printing difference
diff=a-b
print(diff)

#Comments
#1. Single line comment
#print("hello")

#2. Multi line comment
"""This is a multiline comment"""

#Input in python
name=input("name: ")           #string input
age=int(input("age: "))         #int input
price=float(input("price: "))    #float input
print("my name is",name,"and i am",age,"years old")

#Conditional statements
Light = input("Light: ")
if(Light =="red"):
    print("stop")
elif(Light=="yellow"):
    print("look")
elif(Light=="green"):
    print("go")
else:
    print("Light is broken")  

marks= input("marks: ") 
if(marks >= 90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>= 70 and marks< 80):
    print("C") 
else:
    print("D") 


#Single line if/ Ternary operator
food=input("food: ") 
eat="yes"  if food=="cake" else "no"
print(eat)

food=input("food: ") 
print("sweet")  if food=="cake" or food=="jalebi" else print("not sweet")

#Clever if/Ternary operator
age=int(input("age: "))
vote= ("yes", "no") [age<=18]

sal=float(input("salary: "))
tax=sal*(0.1, 0.2) [sal>=50000]
print(tax)

principalamount= float(input("p: "))
rate=float(input("r: "))
time=float(input("t: "))
simpleinterest=principalamount*rate*time/100
print(simpleinterest)

#Operators
#1. Arithmetic operator
a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)     #gives reminder
print(a**b)    #a^b

#Relational/Comparison operators
a=50
b=60
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)

#Assignment operators
num= 10
num=num+10
num+=10
num-=10
num/=10
num%=10
num**=10
print("num:", num)

#Logical operators
print(not False)  #not operator
print(not True)

a=50
b=30
print(not(a>b))

val1=True          #And operator
val2=False
print("and operator:", val1 and val2)

val1=True          #Or operator
val2=False
print("and operator:", val1 or val2)

#Type conversion
#1. Automatic conversion
a=2
b=4.25
sum=a+b

#2. Type casting or manual conversion

a=float("2")
b=4.35
print(a+b)

a=3.14
a=str(a)

print(type(a))

#Input in python
name=input("enter your name: ")
print("Welcome", name)

val=int(input("enter some value: "))
print(type(val), val)

name=input("enter name: ")
age= int(input("enter age: "))
marks= float(input("enter marks"))

first= int(input("enter first: "))
second =int(input("enter second: "))

print("sum=", first+second)

side= int(input("enter square side: "))
print("area=", side*side)   #orside**2

a=float(input("enter first: "))
b=float(input("enter second: "))

print("avg=", (a+b/2))



























=======
>>>>>>> b31414e5e8a23c15102ef5787aa9b0c90a805cdc

