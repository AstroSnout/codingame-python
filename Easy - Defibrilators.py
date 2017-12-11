import math


def distance(lon_a, lat_a, lon_b, lat_b):
    lon_a = math.radians(lon_a)
    lat_a = math.radians(lat_a)
    lon_b = math.radians(lon_b)
    lat_b = math.radians(lat_b)
    x = (lon_b - lon_a) * math.cos((lat_a + lat_b) / 2)
    y = lat_b - lat_a
    return math.sqrt(x ** 2 + y ** 2) * 6371


dists = []


class Defib:
    def __init__(self, ID, name, address, lon, lat):
        self.ID = ID
        self.name = name
        self.address = address
        self.lon = lon
        self.lat = lat


lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())
defibs = []
for i in range(n):
    ID, name, address, _, lon_a, lat_a = input().split(';')
    defibs.append(Defib(int(ID), name, address, float(lon_a.replace(',', '.')), float(lat_a.replace(',', '.'))))

for d in defibs:
    dists.append(distance(d.lon, d.lat, lon, lat))

ID_p = dists.index(min(dists))

print(defibs[ID_p].name)
# Can be done with less code, but meh
