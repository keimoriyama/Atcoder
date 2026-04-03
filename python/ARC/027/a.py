h, m = map(int, input().split())
if m != 0:
    h += 1

hour = 18 - h
minute = 60 - m

if m != 0:
    print(hour * 60 + minute)
else:
    print(hour * 60)
