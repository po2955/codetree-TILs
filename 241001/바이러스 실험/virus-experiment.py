dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n, m, k = map(int, input().split())
board_medi = [[5] * n for _ in range(n)]
board_add = [list(map(int, input().split())) for _ in range(n)]
board = [[[] for _ in range(n)]for _ in range(n)]
for _ in range(m):
    r, c, age = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c].append(age)

def eat_medi():
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                board[i][j].sort()
                for q in range(len(board[i][j])):
                    if board[i][j][q] > 0:
                        board_medi[i][j] -= board[i][j][q]
                        if board_medi[i][j] < 0:
                            board_medi[i][j] += board[i][j][q]
                            for p in range(q, len(board[i][j])):
                                board[i][j][p] *= -1

                        else:
                            board[i][j][q] += 1

def change_medi():
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for q in range(len(board[i][j])):
                    if board[i][j][q] < 0:
                        board_medi[i][j] += (board[i][j][q] * -1) // 2
                while 1:
                    if not board[i][j] or board[i][j][-1] > 0:
                        break
                    board[i][j].pop()

def spread_virus():
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for q in range(len(board[i][j])):
                    if board[i][j][q] % 5 == 0:
                        for q in range(8):
                            nx = i + dx[q]
                            ny = j + dy[q]
                            if 0 <= nx < n and 0 <= ny < n:
                                board[nx][ny].append(1)

def add_medi():
    for i in range(n):
        for j in range(n):
            board_medi[i][j] += board_add[i][j]

for turn in range(k):
    eat_medi()
    change_medi()
    spread_virus()
    add_medi()

answer = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            answer += len(board[i][j])
print(answer)