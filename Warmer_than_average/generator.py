#!/usr/bin/python3

from os import mkdir
from os.path import isdir
from shutil import rmtree
import random as rd
from solution import warmer_day

TEST_COUNT = 50
TEST_PATH = 'tests'
ANSWER_PATH = 'tests'
SAMPLES_PATH = 'tests'

SAMPLES = [[[1, 1, 2, -3], [0, 5, 11, -10], [14, -2, 4]],
           [[0, 0, -2, -3], [0, -5, -1, -1], [1, 15]]]


def main():
    if isdir(TEST_PATH):
        rmtree(TEST_PATH)
    mkdir(TEST_PATH)
    if ANSWER_PATH != TEST_PATH:
        if isdir(ANSWER_PATH):
            rmtree(ANSWER_PATH)
        mkdir(ANSWER_PATH)
    if SAMPLES_PATH != TEST_PATH:
        if isdir(SAMPLES_PATH):
            rmtree(SAMPLES_PATH)
        mkdir(SAMPLES_PATH)
    make_samples()
    for test_number in range(TEST_COUNT):
        make_test(test_number)


def make_samples():
    for index, sample in enumerate(SAMPLES):
        test_file_name = f'./{SAMPLES_PATH}/sample{index + 1:02}'
        answer_file_name = f'./{ANSWER_PATH}/sample{index + 1:02}.a'

        with open(test_file_name, 'w', encoding='utf8', newline="\n") as test_stream:
            line = f'temperature = {sample}\n' \
                   f'print(warmer_day(temperature))'
            print(line, file=test_stream)

        with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
            print(make_output_data(sample), sep='\n', file=answer_stream)

        print(f'Sample {index + 1} [OK]')


def make_test(test_number):
    test_file_name = f'./{TEST_PATH}/{test_number + 1:02}'
    answer_file_name = f'./{ANSWER_PATH}/{test_number + 1:02}.a'

    input_data = make_input_data()
    output_data = make_output_data(input_data)

    with open(test_file_name, 'w', encoding='utf8', newline="\n") as test_stream:
        line = f'temperature = {input_data}\n' \
               f'print(warmer_day(temperature))'
        print(line, file=test_stream)

    with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
        print(output_data, sep='\n', file=answer_stream)

    print(f'Test {test_number + 1} [OK]')


def make_input_data():
    data = [[rd.choice(range(-20, 35)) for _ in range(7)] for _ in range(4)]
    data.append([rd.choice(range(-20, 35)) for _ in range(rd.randint(0, 3))])
    return data


def make_output_data(input_data):
    return warmer_day(input_data)


if __name__ == '__main__':
    main()
