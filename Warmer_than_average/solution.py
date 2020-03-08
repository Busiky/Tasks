def warmer_day(temperatures):
    average = sum([sum(t) for t in temperatures]) / sum([len(t) for t in temperatures])
    for i in range(len(temperatures)):
        for j in range(len(temperatures[0])):
            if temperatures[i][j] > average:
                return i * len(temperatures[0]) + j + 1


if __name__ == '__main__':
    temperature = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0, 0], [1, 1]]
    print(warmer_day(temperature))




