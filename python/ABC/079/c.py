N = input()
num_list = list(N)
op = ["+", "-"]
flag = False
for i in range(len(op)):
    for j in range(len(op)):
        for k in range(len(op)):
            eq = num_list[0] + op[i] + num_list[1] + \
                op[j] + num_list[2] + op[k] + num_list[3]
            ans = eval(eq)
            if ans == 7:
                flag = True
                break
        if flag == True:
            break
    if flag == True:
        break
print(eq + "=" + str(ans))
