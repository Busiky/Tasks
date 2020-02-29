def solve(text):
    log, count, i = {}, 0, 0
    line = text[i]
    while line:
        line = line.split()
        subject, mark = ' '.join(line[:-1]), int(line[-1])
        log[subject] = log.get(subject, [])
        log[subject].append(mark)
        i += 1
        line = text[i]
    sub = text[-1]
    if sub not in log:
        return 'Нет предмета'
    if len(log[sub]) > 2:
        average = sum(log[sub]) / len(log[sub])
        while average <= 4.5:
            log[sub].append(5)
            count += 1
            average = sum(log[sub]) / len(log[sub])
        return count
    while len(log[sub]) < 3:
        log[sub].append(5)
        count += 1
    average = sum(log[sub]) / len(log[sub])
    while average <= 4.5:
        log[sub].append(5)
        count += 1
        average = sum(log[sub]) / len(log[sub])
    return count


if __name__ == '__main__':
    data = []
    string = input()
    while string:
        data.append(string)
        string = input()
    data.append('')
    data.append(input())
    print(solve(data))
