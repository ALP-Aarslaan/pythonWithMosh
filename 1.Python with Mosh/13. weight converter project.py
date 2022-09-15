weight = float(input("enter your weight : "))
print("select the unit of your weight which you entered previously--->")
unit = input("enter L for (lbs) or K for (kg) :")
unit = unit.upper()
print("which unit you want to convert to : ")
desired_unit = input("enter L for (lbs) or K for (kg) :")
desired_unit = desired_unit.upper()
if unit == 'L' and desired_unit == 'K':
    weight = weight * 0.453592
elif unit == 'L' and desired_unit == 'L':
    weight = weight
elif unit == 'K' and desired_unit == 'K':
    weight = weight
else:
    weight = weight * 2.20462
print("Your weight is : ", weight)
