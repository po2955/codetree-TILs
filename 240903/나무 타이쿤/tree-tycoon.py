dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_tonic = [[0] * n for _ in range(n)]
for i in range(n-2, n):
    for j in range(0, 2):
        board_tonic[i][j] = 1
rule = []
for _ in range(m):
    d, p = map(int, input().split())
    d -= 1
    rule.append((d, p))

def move_tonic_grow(d, p):
    global board_tonic, board
    test_tonic = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board_tonic[i][j] == 1:
                nx = (i + (dx[d] * p) + n) % n
                ny = (j + (dy[d] * p) + n) % n
                test_tonic[nx][ny] = 1
                board[nx][ny] += 1
                list_tonic.append((nx, ny))
    board_tonic = test_tonic

def grow_tree_cross():
    global board
    if list_tonic:
        for x, y in list_tonic:
            for i in range(1, 8, 2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] >= 1:
                    board[x][y] += 1

def cut_tree():
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i,j) not in list_tonic:
                board[i][j] -= 2
                new_tonic.append((i,j))

for turn in range(m):
    d, p = rule[turn]
    list_tonic = []
    new_tonic = []
    move_tonic_grow(d, p)
    grow_tree_cross()
    cut_tree()
    if list_tonic:
        for x, y in list_tonic:
            board_tonic[x][y] = 0
    if new_tonic:
        for x, y in new_tonic:
            board_tonic[x][y] = 1

answer = 0
for i in range(n):
    for j in range(n):
            answer += board[i][j]
print(answer)