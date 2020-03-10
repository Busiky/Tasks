from pprint import pprint


def hex_to_binary(num):
    decimal = int(num, 16)
    binary = []
    while decimal:
        binary.append(decimal % 2)
        decimal //= 2
    binary += [0] * (8 - len(binary))
    return ''.join(map(str, binary[::-1]))


def from_bit_to_pic(string):
    result = [[hex_to_binary(string[i * 2: (i + 1) * 2])] for i in range(len(string) // 2)]
    return result


if __name__ == '__main__':
    line = '02C22418243C183E6424182400'
    pprint(from_bit_to_pic(line))
    print('\n'.join(''.join(map(str, item)) for item in from_bit_to_pic(line)))
