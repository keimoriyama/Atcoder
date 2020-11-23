num = int(input()) #ここで標準入力
i = 0

while True:
    ans = 1000*i - num
    i+=1
    if ans >= 0:
        break

print(ans)
