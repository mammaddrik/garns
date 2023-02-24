#::::: Solve :::::
def solve(bo):
    "Sudoku solving function."
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

#::::: Valid :::::
def valid(bo, num, pos):
    "Answer validity function for Sudoku"
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    x = pos[1] // 3
    y = pos[0] // 3
    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

#::::: Find Empty :::::
def find_empty(bo):
    "Function to find empty value."
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None