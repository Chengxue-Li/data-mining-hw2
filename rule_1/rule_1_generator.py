import csv
import sys
import random
def rule(x):
    if x[0] < 0.5 and x[1] < 0.5:
        return 1
    elif x[0] > 0.5 and x[1] > 0.5:
        return 1
    else:
        return 0
number = int(sys.argv[1])
noise = float(sys.argv[2])
data_title = [['temperature', 'humidity', 'late']]
data = []
noise_number = int(number * noise)
correct_number = number - noise_number
for i in range(0, correct_number):
    x = [random.random(), random.random()]
    y = str(rule(x))
    x.append(y)
    data.append(x)
for i in range(0, noise_number):
    x = [random.random(), random.random()]
    y = str(int(random.random() * 2))
    x.append(y)
    data.append(x)
random.shuffle(data)
data_title.extend(data)
with open('number_' + str(number) + '_noise_' + sys.argv[2] + '.csv','w') as f:
    f_1 = csv.writer(f)
    f_1.writerows(data_title)
