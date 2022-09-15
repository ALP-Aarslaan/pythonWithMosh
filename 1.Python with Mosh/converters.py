def kg_to_lbs(weight):
    return weight * 2.205


def lbs_to_kg(weight):
    return weight / 2.205


def find_max(numbers):
    maximum = numbers[0]
    for x in numbers:
        if x >= maximum:
            maximum = x

    return maximum
