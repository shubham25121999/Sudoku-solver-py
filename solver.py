
# solver.py
def solve(gr):
    find = find_empty(gr)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(gr, i, (row, col)):
            gr[row][col] = i

            if solve(gr):
                return True

            gr[row][col] = 0

    return False


def valid(gr, num, pos):
    # Checking row
    for i in range(len(gr[0])):
        if gr[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking column
    for i in range(len(gr)):
        if gr[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking 3x3 subgrid
    gr_x = pos[1] // 3
    gr_y = pos[0] // 3

    for i in range(gr_y*3, gr_y*3 + 3):
        for j in range(gr_x * 3, gr_x*3 + 3):
            if gr[i][j] == num and (i,j) != pos:
                return False

    return True


def print_grid(gr):
    for i in range(len(gr)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(gr[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            print(gr[i][j], end = ' ')
        print()


def find_empty(gr):
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            if gr[i][j] == 0:
                return (i, j)  # row, col

    return None