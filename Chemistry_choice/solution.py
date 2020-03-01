def solve(text):
    return '\n'.join([x.capitalize() for x in text.split() if x[-2:] == 'um' and len(x) <= 8])


if __name__ == '__main__':
    print(solve(input()))
