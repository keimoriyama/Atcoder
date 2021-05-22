n = int(input())
a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())

def bi_search(target):
    right = len(a) - 1
    left = 0
    while(right >= left):
        mid = int((right+left)/2)
        if(a[mid] == target):
            return True
        else:
            if(a[mid] > target):
                right = mid - 1
            else:
                left = mid + 1

    return False

bin = []
for i in a:
    bin[i]+= 1

a.sort()


ans = 0
for i in range(n):
    if bi_search(b[c[i]-1]):
        ans += bin[b[c[i] - 1]]
print(ans)
