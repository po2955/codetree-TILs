from collections import deque
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move_rule = deque()
for _ in range(m):
    d, p = map(int, input().split())
    move_rule.append((d-1, p))
board_tonic = [[0] * n for _ in range(n)]
board_tonic[n-1][0] = 1
board_tonic[n-2][0] = 1
board_tonic[n-1][1] = 1
board_tonic[n-2][1] = 1
first_tonic = []

def move_tonic():
    global board_tonic, first_tonic
    first_tonic.clear()
    test = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board_tonic[i][j] == 1:
                nx = (i + (dx[now_d] * now_p) + n) % n
                ny = (j + (dy[now_d] * now_p) + n) % n
                first_tonic.append((nx, ny))
                test[nx][ny] = 1
    board_tonic = test

def grow_tree():
    grow = [[0] * n for _ in range(n)]
    check = []
    for i in range(n):
        for j in range(n):
            if board_tonic[i][j] == 1:
                board[i][j] += 1
                board_tonic[i][j] = 0
                check.append((i, j))
  
    for x, y in check:
        for k in range(1, 8, 2):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] >= 1:
                grow[x][y] += 1

    for i in range(n):
        for j in range(n):
            if grow[i][j] > 0:
                board[i][j] += grow[i][j]

def cut_tree():
    global first_tonic
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in first_tonic:
                board_tonic[i][j] = 1
                board[i][j] -= 2

for turn in range(m):
    now_d, now_p = move_rule.popleft()
    move_tonic()
    grow_tree()
    cut_tree()

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]
print(answer)