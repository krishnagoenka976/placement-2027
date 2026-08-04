def greet(name):
    print("Hello",name)
    print("Welcome to Python")

greet("Krishna")

def add(a,b):
    print("sum is ",a+b)

add(4,5)

def square(n):
    return n*n

print(square(4))

def largest(a,b):
    if a>b:
        print(a)
    else:
        print(b)
        
largest(4,5)

def table(num):
    for i in range(1,11):
        print(num,"X",i,"=",num*i)

table(5)

def evenOdd(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")

evenOdd(4)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

print(factorial(5))

def calculator(a,b,op):
    if(op=='+'):
        return a+b
    elif(op=='-'):
        return a-b
    elif(op=='*'):
        return a*b
    elif(op=='/'):
        return a/b
    else:
        return "Invalid operator"

print(calculator(4,5,'*'))