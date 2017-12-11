values = []
worst = -1

n = int(input())
for i in input().split():
    values.append( int(i) )

for i in range( len(values) ):
    if worst < values[i]:
        for j in range ( i+1, len(values) ):
            val = values[i] - values[j]
            if val > worst:
                worst = val

print(0 if worst is -1 else -worst)
