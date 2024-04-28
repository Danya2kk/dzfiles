import re


def sum_of_nums(filename):
    sum = 0
    with open('text.txt', 'r') as file:
        for line in file:
            numbers = re.findall(r'\d+', line)
            for number in numbers:
                sum += int(number)

    return sum

print(f"Сумма всех последовательностей чисел = {sum_of_nums('text.txt')}")