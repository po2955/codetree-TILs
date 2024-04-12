from collections import deque
from copy import deepcopy
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
time = 0
board = [list(map(int, input().split())) for _ in range(n)]
board_people = [[[] for _ in range(n)] for _ in range(n)]
for i in range(1, m + 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = i * 10

def is_Finished():
    for i in range(n):
        for j in range(n):
            if board_people[i][j]:
                return False
    return True

def find_base(t):
    for i in range(n):
        for j in range(n):
            if board[i][j] == t * 10:
                Q = deque()
                Q.append((i, j))
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] >= 0:
                            if board[nx][ny] == 1:
                                board[nx][ny] = -1
                                board_people[nx][ny].append(time)
                                return
                            Q.append((nx, ny))
                            visited[nx][ny] = 1

def move_people():
    global board, board_people
    test_people = [[[] for _ in range(n)] for _ in range(n)]
    test = deepcopy(board)
    cant = []
    for i in range(n):
        for j in range(n):
            if board_people[i][j]:
                while board_people[i][j]:
                    people = board_people[i][j].pop()
                    signal = 0
                    Q = deque()
                    Q.append((i,j))
                    visited = [[0] * n for _ in range(n)]
                    visited[i][j] = 1
                    check = [[None] * n for _ in range(n)]
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] >= 0:
                                check[nx][ny] = (temp[0], temp[1])
                                if board[nx][ny] == people * 10:
                                    if temp[0] == i and temp[1] == j:
                                        signal = 1
                                        cant.append((nx, ny))
                                        break
                                    x, y = check[nx][ny]
                                    while 1:
                                        xx, yy = x, y
                                        x, y = check[xx][yy]
                                        if x == i and y == j:
                                            test_people[xx][yy].append(people)
                                            signal = 1
                                            break

                                    if signal == 1:
                                        break
                                Q.append((nx, ny))
                                visited[nx][ny] = 1
                        if signal == 1:
                            break
    if cant:
        for x, y in cant:
            test[x][y] = -1
    board = test
    board_people = test_people

a = 0
while 1:
    time += 1
    move_people()
    if time <= m:
        find_base(time)
    if is_Finished() == True:
        break
    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print()
    # for x in board_people:
    #     print(x, end = ' ')
    #     print()
    # print()
    a += 1
print(time)