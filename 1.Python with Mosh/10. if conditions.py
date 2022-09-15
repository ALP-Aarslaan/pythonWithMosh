is_cold = True
is_hot = False
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("its a cool day")
    print("wear warm cloths")
else:
    print("its a lovely day")

print("enjoy your day")

# exercise:

price = 10000000

has_good_credit = True
if has_good_credit:
    downPayment = price * 0.1
else:
    downPayment = price * 0.2
print(f"down payment is : ${downPayment}")