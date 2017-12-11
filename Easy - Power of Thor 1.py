lx, ly, x, y = [int(i) for i in input().split()]
while True:
    input()
    p=''
    p += 'S' if y < ly else 'N' if y != ly else ''
    p += 'E' if x < lx else 'W' if x != lx else ''
    y += 1 if y < ly else -1 if y != ly else 0
    x += 1 if x < lx else -1 if x != lx else 0
    print(p)
