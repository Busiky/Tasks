def solve():
    line = input()
    result = []
    count = 0
    for i in range(1, len(line) - 1):
        if line[i] == line[i - 1] and line[i] != '%':
            count += 1
        elif line[i] == '%' and line[i - 1] != '%' and line[i + 1] == '%':
            result.append([line[i - 1], 1])
            count = 0
        else:
            if count:
                result.append([line[i - 1], count])
                count = 0
    if line[-3] == line[-2] and count or line[-2] == line[-1] and not count:
        result.append([line[-2], 1])
    return ''.join(x[0] for x in result)


if __name__ == '__main__':
    print(solve(input()))
