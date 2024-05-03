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

dict = {
"firstInfo" : {
    "name":"Piyush",
    "age":20,
    "Gender":"Male"
},
"secondInfo" : {
    "name":"Kashish",
    "age":19,
    "Gender":"Female"
}
}
dict.get("firstInfo").update({"age":18});

print(dict)