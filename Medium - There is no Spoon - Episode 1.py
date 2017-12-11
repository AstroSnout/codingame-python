def find_neighbour(lista, index_y, index_x):
    # If none present, print out (index_x index_y -1 -1 -1 -1)
    current = [index_x, index_y]
    right = bottom = [-1, -1]

    row = lista[index_y]

    # Looking for the right one
    for i in range(index_x + 1, len(row)):
        if row[i] == '0':
            right = [i, index_y]
            break

    # Looking for the bottom one
    for j in range(index_y + 1, len(lista)):
        if lista[j][index_x] == '0':
            bottom = [index_x, j]
            break

    return ' '.join(str(x) for x in current + right + bottom)


input()
data = [input() for _ in range(int(input()))]  # gets all of the data

# Checks for a '0'
# When it finds one, it calls find_neighbour() which returns a printable string
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '0':
            print(find_neighbour(data, i, j))
