def calculate_discount(price, is_member):
    if is_member:
        disc = price * 0.1
        disc_price = price - disc
        return disc_price
    else:
        return 0


def calculate_diff(numbers):
    if len(numbers) == 0:
        return 0

    min_number = numbers[0]
    max_number = numbers[0]

    for number in numbers:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number

    diff = max_number - min_number
    return diff


