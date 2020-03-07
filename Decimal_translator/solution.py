def decimal_translator(number, base):
    abc = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = str(number)
    if [x for x in number if x not in abc[:base]]:
        return
    return int(number, base)


if __name__ == '__main__':
    print(decimal_translator(101, 2))
