from solution import *


def solve(number):
    result = []
    n, angle = 1, 3
    while angle <= number:
        while create_polygon_number(n, angle) <= number:
            if create_polygon_number(n, angle) == number:
                result.append((n, angle))
            n += 1
        n = 1
        angle += 1
    if not result:
        result.append((None, None))
    return result


if __name__ == "__main__":
    print(*solve(int(input())), sep='\n')
