D, G = map(int, input().split())
p, c = [], []
for i in range(D):
    p_i, c_i = input().split()
    p.append(int(p_i))
    c.append(int(c_i))

score = 0
pb_num = 0
flag = False

for i in range(D):
    num = p[i]
    for j in range(p[i]):
        score += int(p[i])*100*(i+1)
        pb_num += 1
        num -= 1
        if score >= G:
            flag = True
            break
        if num == 0:
            score += c[i]
    if flag:
        break

print("p :" + str(p))
print("c :" + str(c))

print("score :" + str(score))
print("pb_num :" + str(pb_num))
