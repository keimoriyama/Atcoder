n, k = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

max_value = max(a)
found = False
for b in b:
    if a[b-1] == max_value:
        print("Yes")
        found = True
        break
if not found:
    print("No")
