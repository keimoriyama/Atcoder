K = int(input())
H = 21 + K // 60
M = K % 60

print("{}:{:02}".format(H, M))
