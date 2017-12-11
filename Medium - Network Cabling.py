# Tried to write short code
# Ended up being unreadable instead :(


def taxi_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


n = int(input())
bld = sorted([[int(j) for j in input().split()] for i in range(n)], key=lambda x: x[1])
bld_x = sorted(bld, key=lambda x: x[0])
median = bld[n//2][1] if n%2==1 else (bld[n//2][1] + bld[n//2-1][1])//2
dists = sum([taxi_dist([mini[0], median], mini) for mini in bld]) + taxi_dist([bld_x[0][0], median], [bld_x[n-1][0], median])

print(dists)
