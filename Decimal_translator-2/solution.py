def decimal_translator_2(number, base):
    abc = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = str(number)
    if [x for x in number if x not in abc[:base]]:
        return
    return int(number, base)


if __name__ == '__main__':
    number, base = input().split()
    print(decimal_translator_2(number, int(base)))
