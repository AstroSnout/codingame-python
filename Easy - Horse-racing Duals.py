horses = sorted([ int(input()) for _ in range(int(input()))])
best = abs(horses[0] - horses[1])

for i in range (2, len(horses)):
    curr = abs(horses[i-1] - horses[i])
    if curr < best:
        best = curr

print(best)
