has_high_income = False
has_good_credit = True
if has_good_credit and has_high_income:
    print("eligible for loan")


if has_good_credit or has_high_income:
    print("eligible for loan")
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("eligible for loan")