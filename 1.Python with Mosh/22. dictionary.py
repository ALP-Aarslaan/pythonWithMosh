customers = {
    "name": "Mohammad Jonayed Sarkar",
    "age": 23,
    "is_valid": True
}
print(customers)
print(customers["age"])
print(customers.get("birthdate"))

print(customers.get("name"))

print(customers.get("birthdate", "11th March, 1998"))
print(customers)
customers["name"] = "Mohammad"
print(customers)

customers["birthdate"] = "11th March, 1998"
print(customers)

phone = input("phone : ")
digits_to_word = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = " "
for characters in phone:
    output = output + digits_to_word.get(characters, "!")+" "

print(output)
