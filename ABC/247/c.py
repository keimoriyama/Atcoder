def gen_s(N):
    if N == 1:
        return "1"
    else:
        return gen_s(N - 1) + " " + str(N) + " " + gen_s(N - 1)


N = int(input())
print(gen_s(N))