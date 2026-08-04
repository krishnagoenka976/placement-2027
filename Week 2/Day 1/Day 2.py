fruits = ["apple","mango","banana","cherry","orange"]
print(fruits[0])
print(fruits[-1])

l = []
for i in range(5):
    num = int(input("Enter number: "))
    l.append(num)

print(l)

numbers = [20,15,18,53,81,30]
largest = numbers[0]
for i in range(len(numbers)):
    if largest<numbers[i]:
        largest = numbers[i]
print(largest)
        
smallest = numbers[0]
for i in range(len(numbers)):
    if smallest>numbers[i]:
        smallest = numbers[i]
print(smallest)

ls = [1,2,3,4,5]
ls.append(7)
print(ls)
ls.insert(2,9)
print(ls)
ls.remove(9)
print(ls)
ls.pop()
print(ls)