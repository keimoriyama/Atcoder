s = input()
num = [str(i) for i in range(10)]
for n in num:
    #print(n)
    if n not in s:
        print(n)