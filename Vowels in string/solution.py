def vowels_in_string(line):
    rus_vowels = 'аяоёуюэеыи'
    en_vowels = 'aeuioy'
    return [letter for letter in line if letter in rus_vowels + en_vowels + rus_vowels.upper() + en_vowels.upper()]


if __name__ == '__main__':
    print(vowels_in_string(input()))
