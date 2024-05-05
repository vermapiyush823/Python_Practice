# print("Hello world")
# age = 19
# print("I am", age, "years old")


# num1 = 10
# num2 = 15
# print(num1*"Q")

# print("num1"+"Q")


# Integer Division
# a = 10
# b = 3
# print(a//b)

# Float Division
# a = 10
# b = 3
# print(a/b)



# Taking input from user
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello", name, "you are", age, "years old")



# Conditional Statements
# age = int(input("Enter your age: "))
# if(age>18):
#     print("You are an adult")
# elif(age>12 and age<=18):
#     print("You are a teenager")
# else:
#     print("You are a child")


# Single Line ternary operator
# food = input("Enter your favourite food: ")
# eat = "yes" if food == "pizza" else "no"
# print(eat)


# Operators

# Arithmetic Operators
# a = 10
# b = 5
# sum = a+b
# minus = a-b 
# mul = a*b
# div = a/b
# mod = a%b
# pow = a**b
# print(sum, minus, mul, div, mod,pow)


# Relational Operators
# a = 50 
# b = 20
# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)

# Assignment Operators
# a = 10
# a+=1
# print(a)
# a*=2
# print(a)
# a/=2
# print(a)
# a-=2
# print(a)
# a%=2
# print(a)
# a//=2
# print(a)
# a**=2
# print(a)



# Type Conversion
# a = 2
# b = 2.3
# sum = a+b
# print(sum)

# Type Casting
# a = 2.0
# b = int(a)
# print(b)

# Strings
# str1 = "Hello"
# str2 = 'World'
# print(str2+"\n"+str1)
# print(len(str1))
# print(type(str1[0]))

# String Slicing
# str = "My name is Piyush Verma"
# print(str[0:7])
# print(str[11:])
# print(str[:10])
# print(str[0::2])
# print(str[::-1])
# print(str[:-1])

# String Methods
# str = "My name is Piyush Verma"
# print(str.endswith("Piyush"))
# print(str.startswith("My"))
# print(str.capitalize())
# print(str.replace("Piyush", "Rahul123"))
# print(str.find("Piyush"))
# print(str.count("Piyush"))


# Nested if else

# name = "Piyush Verma" 
# if(name.find("Piyush") != -1):
#     if(name.find("Verma") != -1):
#         print("Name is correct")
#     else:
#         print("Last name is incorrect")
# else:
#     print("First name is incorrect")



# a = int(input("Enter first no: "))
# b = int(input("Enter second no: "))
# c = int(input("Enter third no: "))
# if(a>b and a>c):
#     print(a,"is largest")
# elif(b>c):
#     print(b,"is largest")
# else: 
#     print(c,"is largest")

# num =  int(input("Enter a num: "))
# if(num%7==0):
#     print(num,"is multiple of 7")
# else:
#     print(num,"is not a multiple of 7")


# Lists in Python

# marks = [1,2,2,3]
# marks[2] = 1
# print(marks)

# List Methods
# list = []
# list.append(1)
# list.append(4)
# list.append(3)
# print(list)
# list.sort(reverse=True)
# list.insert(2,0)
# print(list)
# list.reverse()
# print(list)
# list.remove(1)
# list.pop(2)
# print(list)


# Tuples in Python
# tuple = (1,2,3,4)
# print(tuple) 
# print(tuple[1:3])

# list = []
# n = int(input("Enter the size: "))
# for i in range(0,n):
#     temp = input("Enter number: ")
#     list.append(temp)

# for i in range(0,n):
#     if(list[i]!=list[n-i-1]):
#         print("Not a palindrome")

# print("Palindrome")


# Dictionary in Python
# dict = {
#     "name" : "Piyush",
#     "cgpa" : "8.5",
#     "marks" : [12,13,22]
# }
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.get("name"))
# print(dict.items())

# dict = {
# "firstInfo" : {
#     "name":"Piyush",
#     "age":20,
#     "Gender":"Male"
# },
# "secondInfo" : {
#     "name":"Kashish",
#     "age":19,
#     "Gender":"Female"
# }
# }
# dict.get("firstInfo").update({"age":18});

# print(dict)


# Sets in python
# set = {1,2,4,3}
# set.add(10)
# print(set)

# Loops in Python

# While loop
# count = 1
# while count<=10:
#     print("cnt",count)
#     count+=1

# For loop
# arr = [1,2,3,4,5]

# for i in arr:
#     print(i)

# for i in range(1,5,1):
#     print(arr[i])

# Functions in Python
# def sum(a,b):
#     return a+b

# print(sum(1,2))


# Recursion in Python
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return n*fact(n-1)

# print(fact(5))



# File Input Output in Python
 
# f = open("demo.text")
# print(f.read())

# f = open("demo1.txt","a")
# f.write("Hello i am Piyush")


# Oops in Python
 
# class Student:
#     def __init__(self,name):
#         self.name = name
#         print("Hello I am",self.name)

#     def fun(self,name):
#         self.name = name
#         print("Fuck you",self.name)


# s1 = Student("Rajesh")
# s1.fun("Rajesh")


# class Student:
#     def __init__(self,name,marks): 
#         avg = marks[0] + marks[1]+ marks[2]
#         print(name,"marks average is :",avg//3)  

# s1 = Student("Piyush",[10,20,30])
# s2 = Student("Kashish",[10,50,60])
# s3 = Student("Tanmay",[10,10,10])

# Static Methods
# class Student:  
#     name = "Piyush" 
#     @staticmethod
#     def college():
#         print(Student.name,"you are in a good college")

# s1 = Student()
# s1.college()


# Abstraction in Python
# class Account:
#     def __init__(self,acc_no,balance):
#         self.acc_no = acc_no
#         self.balance = balance
#     def debit(self,amount):
#         self.balance -= amount
#     def credit(self,amount):
#         self.balance += amount
#     def bal(self):
#         print("Your account balance is :",self.balance)
    
# a1 = Account(121,10000)
# a1.bal()
# a1.debit(200)
# a1.bal()
# a1.credit(2000)
# a1.bal()



# del keyword in python
# class Student:
#     def name(self,name):
#         self.name = name
#         print(self.name)
    
# s1 = Student()
# s1.name("Piyush")
# del s1
# s1.name("Piyush")


# public, private in python
# class Bank:
#     def setter(self,acc_no,bal):
#         self.acc_no = acc_no
#         self.__bal = bal
#     def checkbalance(self):
#         print(self.__bal)
# b1 = Bank()
# b1.setter(121,10000)
# b1.__bal this will give error
# b1.checkbalance()


# Inheritance in Python

# class Car:
#     @staticmethod
#     def start():
#         print("Started...")
    

# class Toyota(Car):
#     def __init__(self):
#         print("It is a toyota car")


# t1 = Toyota()
# t1.start()


# super() method in python
# class Car:
#     @staticmethod
#     def start():
#         return 'having 4 tyres'

# class Toyota(Car):
#     def __init__(self):
#         print("It is a toyota car",super().start())


# t1 = Toyota()

