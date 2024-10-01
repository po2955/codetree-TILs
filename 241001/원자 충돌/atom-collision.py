dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, m, s, d = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y].append((m, s, d))

def move_atom():
    global board
    test_board = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for q in range(len(board[i][j])):
                    m = board[i][j][q][0]
                    s = board[i][j][q][1]
                    d = board[i][j][q][2]
                    nx = (i + (dx[d] * s)) % n
                    ny = (j + (dy[d] * s)) % n
                    test_board[nx][ny].append((m, s, d))
    board = test_board

def over_two_atom():
    for i in range(n):
        for j in range(n):
            if board[i][j] and len(board[i][j]) > 1:
                l = len(board[i][j])
                m, s, d = 0, 0, 0
                sign = 0
                for q in range(len(board[i][j])):
                    m += board[i][j][q][0]
                    s += board[i][j][q][1]
                    if board[i][j][0][2] % 2 != board[i][j][q][2] % 2:
                        sign = 1
                board[i][j].clear()
                m //= 5
                if m == 0:
                    continue
                s //= l
                if sign == 0:
                    for p in range(0, 7, 2):
                        board[i][j].append((m,s,p))
                else:
                    for p in range(1, 8, 2):
                        board[i][j].append((m,s,p))

for turn in range(k):
    move_atom()
    over_two_atom()

answer = 0

for i in range(n):
    for j in range(n):
        if board[i][j]:
            for q in range(len(board[i][j])):
                answer += board[i][j][q][0]
print(answer)