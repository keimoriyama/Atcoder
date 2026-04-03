x, y, z = map(int, input().split())

if (x > 0 and y > 0 and x > y) or (x < 0 and y < 0 and y > x):
    if (y > 0 and z > 0 and z < y) or (y < 0 and z < 0 and y < z):
        if (x > 0 and z > 0) or (x < 0 and z < 0):
            print(abs(x))
        else:
            print(abs(x) + 2 * abs(z))
    elif (y < 0 and z > 0) or (y > 0 and z < 0):
        print(abs(x) + 2 * abs(z))
    else:
        print(-1)
else:
    print(abs(x))
