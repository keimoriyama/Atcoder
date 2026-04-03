a, b, c, d, e, f, x = map(int, input().split())
time = 0
t_s, t_a = divmod(x, (a + c))  #, x % (a + c)
a_s, a_a = divmod(x, (d + f))  #, x % (d + e)
#print(t_s, t_a, a_s, a_a)
t_d = t_s * a * b
a_d = a_s * d * e
if t_a <= a:
    t_d += b * t_a
else:
    t_d += b * a
if a_a <= a:
    a_d += e * a_a
else:
    a_d += e * a
if t_s == 0:
    if x < a:
        t_d = x * b
    else:
        t_d = a * b
if a_s == 0:
    if x < d:
        a_d = x * e
    else:
        a_d = d * e

#print(a_d, t_d)
if a_d == t_d:
    print("Draw")
elif a_d < t_d:
    print("Takahashi")
else:
    print("Aoki")