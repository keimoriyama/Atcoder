import math


def calc_distance(a, b):
    x, y = 0, 0
    dis = 0
    x = abs(int(a[0]) - int(b[0])) * abs(int(a[0]) - int(b[0]))
    y = abs(int(a[1]) - int(b[1])) * abs(int(a[1]) - int(b[1]))
    dis = math.sqrt(x+y)
    return dis


N = int(input())

num_list = []
for i in range(N):
    a = input()
    # for j in range(2):
    num_list.append(a.split(' '))

max_distance = 0
distance = 0

for i in range(N):
    for j in range(N):
        if i != j:
            distance = calc_distance(num_list[i], num_list[j])
            if max_distance < distance:
                max_distance = distance


print(max_distance)
