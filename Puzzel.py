g = 0

def print_board(elements):
    for row in elements:
        for cell in row:
            if cell == -1:
                print("_", end=" ")
            else:
                print(cell, end=" ")
        print()
    print()


def heuristic(start, goal):
    global g
    h = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] != goal[i][j] and start[i][j] != -1:
                h += 1
    return h + g


def moveleft(start, position):
    start[position[0]][position[1]], start[position[0]][position[1] - 1] = start[position[0]][position[1] - 1], start[position[0]][position[1]]


def moveright(start, position):
    start[position[0]][position[1]], start[position[0]][position[1] + 1] = start[position[0]][position[1] + 1], start[position[0]][position[1]]


def moveup(start, position):
    start[position[0]][position[1]], start[position[0] - 1][position[1]] = start[position[0] - 1][position[1]], start[position[0]][position[1]]


def movedown(start, position):
    start[position[0]][position[1]], start[position[0] + 1][position[1]] = start[position[0] + 1][position[1]], start[position[0]][position[1]]


def movetile(start, goal):
    emptyat = find_empty(start)
    row, col = emptyat[0], emptyat[1]
    t1, t2, t3, t4 = [row[:] for row in start], [row[:] for row in start], [row[:] for row in start], [row[:] for row in start]
    f1, f2, f3, f4 = 100, 100, 100, 100

    if col - 1 >= 0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2, f3, f4)

    if f1 == min_heuristic:
        moveleft(start, emptyat)
    elif f2 == min_heuristic:
        moveright(start, emptyat)
    elif f3 == min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)


def find_empty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:
                return (i, j)


def solveEight(start, goal):
    global g
    g += 1
    movetile(start, goal)
    print_board(start)
    f = heuristic(start, goal)
    if f == g:
        print("Solved in {} moves".format(f))
        return

    solveEight(start, goal)


def main():
    start = []
    goal = []
    print("Enter the start state:(Enter -1 for empty):")
    for _ in range(3):
        row = list(map(int, input().split()))
        start.append(row)

    print("Enter the goal state:(Enter -1 for empty):")
    for _ in range(3):
        row = list(map(int, input().split()))
        goal.append(row)

    print_board(start)
    solveEight(start, goal)


if __name__ == '__main__':
    main()
