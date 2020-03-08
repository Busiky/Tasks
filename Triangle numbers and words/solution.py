import string


def triangle(item):
    abc = string.ascii_uppercase
    if item.isdigit():
        number = int(item)
    else:
        number = sum([abc.index(letter) + 1 for letter in item.upper()])
    count = 0
    triangle_number = 0
    while triangle_number < number:
        count += 1
        triangle_number = count * (count + 1) // 2
    if triangle_number == number:
        return count
    return False


if __name__ == '__main__':
    print(triangle(input()))
