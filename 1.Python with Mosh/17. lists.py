names = ["Mohammad","Jonayed","Sarkar"]
print(names)
print(names[:2])

print(names[2:])
print(names[:])
names[0] = " Jon"
print(names)

numbers = [1,2,3,4,5,6,7,8,9,10]
maxNumber = numbers[0]
for x in numbers:
    if x >= maxNumber:
        maxNumber = x
print(f"Maximum number is : {maxNumber}")