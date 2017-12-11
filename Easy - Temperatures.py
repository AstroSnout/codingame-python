n = int(input())  # the number of temperatures to analyse
temps = input().rsplit(' ')  # the n temperatures expressed as integers ranging from -273 to 5526
close = 5526
for i in range (n):
    temp = int(temps[i])
    if abs(temp) < abs(close):
        close = temp
    elif abs(temp) == abs(close):
        if temp > close:
            close = temp

print(0 if n is 0 else close)
