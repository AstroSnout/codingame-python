import sys


class Dwarf:
    def __init__(self, my_pos):
        self.pos = my_pos
        self.adj = []
        self.mentor = False

    def __eq__(self, other):
        return self.pos == other

    def add_adj(self, neighbour):
        self.adj.append(neighbour)

    def is_mentor(self):
        self.mentor = True


def look_longest(dwarf, p):
    val = []
    if dwarf.adj != []:  # List
        for index in dwarf.adj:  # Int
            val.append(look_longest(dwarves[dwarves.index(index)], p))
        return (max(val) + 1)
    else:
        return p + 1


dwarves = []
adjs = []
for i in range(int(input())):
    pos, adj = [int(j) for j in input().split()]
    d = Dwarf(pos)
    d_adj = Dwarf(adj)
    if d not in dwarves:
        dwarves.append(d)
        d.add_adj(adj)
        adjs.append(adj)
    else:
        dind = dwarves.index(d)
        dwarves[dind].add_adj(adj)
        adjs.append(adj)

    if d_adj not in dwarves:
        dwarves.append(d_adj)

mentors = []
for d in dwarves:
    if d.pos not in adjs:
        d.is_mentor()
        mentors.append(d)
    print('Position is {} and connections are {}'.format(d.pos, d.adj), file=sys.stderr)
p = 0
c = []
for m in mentors:
    c.append(look_longest(m, p))
    print('Mentor(s):', m.pos, file=sys.stderr)

print(max(c))