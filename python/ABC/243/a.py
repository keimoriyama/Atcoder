V,A,B,C = map(int, input().split())

while True:
    if V >= A:
        V -= A
    else:
        print("F")
        break
    if V >= B:
        V -= B
    else:
        print("M")
        break
    if V >= C:
        V -= C
    else:
        print("T")
        break
