S1 = input()
S2 = input()
S3 = input()
SS = set((S1, S2, S3))
SSS = set(("ABC", "ARC", "AGC", "AHC"))

diff = list(SSS - SS)
print(diff[0])
