log, count, i = {}, 0, 0
line = input()
while line:
    line = line.split()
    subject, mark = ' '.join(line[:-1]), int(line[-1])
    log[subject] = log.get(subject, [])
    log[subject].append(mark)
    i += 1
    line = input()
sub = input()
if sub not in log:
    print('Нет предмета')
elif len(log[sub]) > 2:
    average = sum(log[sub]) / len(log[sub])
    while average <= 4.5:
        log[sub].append(5)
        count += 1
        average = sum(log[sub]) / len(log[sub])
    print(count)
else:
    while len(log[sub]) < 3:
        log[sub].append(5)
        count += 1
    average = sum(log[sub]) / len(log[sub])
    while average <= 4.5:
        log[sub].append(5)
        count += 1
        average = sum(log[sub]) / len(log[sub])
    print(count)
