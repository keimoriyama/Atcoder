K = int(input())

num = []
while K > 0:
    num.append(K % 2)
    K = K // 2

for n in reversed(num):
    if n == 1:
        print("2", end="")
    else:
        print("0", end="")
