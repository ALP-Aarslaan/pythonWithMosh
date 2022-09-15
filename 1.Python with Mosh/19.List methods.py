numbers = [1, 2, 3, 4, 5, 6, 7, 8,8, 9, 10]
numbers.append(11)
print(numbers)
numbers.insert(0,22)
print(numbers)
numbers.remove(22)
print(numbers)
numbers.pop() # it removes last item of the list
print(numbers)
print(numbers.index(10))
print(77 in numbers)
print(numbers.count(8))
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
print(numbers2)
numbers.remove(8)
print(numbers)
print(numbers)
numbers.clear()
print(numbers)

number = [2,1,3,5,6,3,1,2]
unique = []
for num in number:
    if num not in unique:
        unique.append(num)
        unique.sort()
print(unique)
