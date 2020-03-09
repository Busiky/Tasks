def create_polygon_number(n, q):
    return n + (q - 2) * n * (n - 1) // 2


def check_polygon_number(number):
    angle = 3
    n = 1
    while True:
        if create_polygon_number(n, angle) == number:
            return n, angle
        if angle > number:
            return None, None
        if create_polygon_number(n, angle) < number:
            n += 1
        elif create_polygon_number(n, angle) > number:
            n = 1
            angle += 1


if __name__ == "__main__":
    # result = [create_polygon_number(n, q) for n in range(1, 100) for q in range(3, 100)]
    print(create_polygon_number(int(input()), int(input())))
    # print(check_polygon_number(int(input())))
    # print(result)
