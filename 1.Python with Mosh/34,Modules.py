import converters
from converters import kg_to_lbs
from  converters import lbs_to_kg

print(converters.lbs_to_kg(172))
print(converters.kg_to_lbs(78.00453514739229))

print(kg_to_lbs(78))
print(lbs_to_kg(78))

n = int(input("enter how many numbers you want : "))
numbers = []

for i in range(n):
    numbers.append(input())

max = converters.find_max(numbers)

print(max)
