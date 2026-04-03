Y = int(input())
diff = Y % 4
if diff == 0:
    print(Y + 2)
elif diff == 1:
    print(Y+1)
elif diff == 2:
    print(Y)
elif diff == 3:
    print(Y + 3)