for x in range(4):
    for y in range(4):
        print(f"{x}, {y}")
numbers = [6, 2, 6, 2, 2]
i = 0
for n in numbers:
    print("*"*n)
for items in numbers:
    output = " "
    for count in range(items):
        output = output + "X"
    print(output)