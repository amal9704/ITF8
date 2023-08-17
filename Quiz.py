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

    min_num = numbers[0]
    max_num = numbers[0]

    for num in numbers:
        if num < min_num:
            min_number = num
        if num > max_num:
            max_num = num

    diff = max_num - min_num
    return diff


