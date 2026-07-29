# Program 1
name = input("Enter your name: ")
print(name.upper())
print(name.lower())

# Program 2
name = input("Enter your name: ")
print(len(name))
print(name.count(" "))

# Program 3
str = "I love Python"
print(str.replace("Python", "Java"))

# Program 4
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

# Program 5
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Program 6
a = int(input("Enter the first number: "))
b = int(input('Enter the second number: '))
if a>b:
    print("Largest number = ", a)
else:
    print("Largest number = ", b)

# Program 7
num = int(input("Enter a number: "))
if num == 0:
    print("The number is zero")
elif num > 0:
    print("The number is positive")
else:
    print("The number is negative")

# Challenge Program 
marks = int(input("Enter your marks: "))
if(marks>90):
    print("Grade = A")
elif(marks>80):
    print("Grade = B")
elif(marks>70):
    print("Grade = C")
elif(marks>60):
    print("Grade = D")
else:
    print("Grade = F")