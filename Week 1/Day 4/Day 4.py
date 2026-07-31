# Program 1
for i in range(5):
    print("Hello")

# Program 2
for i in range(1,11):
    print(i)

# Program 3
for i in range(10,0,-1):
    print(i)

# Program 4
num = int(input("Enter a number: "))
for i in range(1,11):
    print(num,"X",i,"=",num*i)

# Program 5
for i in range(1,21):
    if i%2==0:
        print(i)

# Program 6
for i in range(1,21):
    if i%2!=0:
        print(i)

# Program 7
num = int(input("Enter a number: "))
match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")

# Challenge Program
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()