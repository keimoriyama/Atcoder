card = list(map(int, input().split()))
card.sort()
print(card[-1] + card[-2])
