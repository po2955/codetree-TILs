dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
board_m = [[[] for _ in range(n)] for _ in range(n)]
board_s = [[[] for _ in range(n)] for _ in range(n)]
board_d = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, m, s, d  = map(int, input().split())
    board_m[x-1][y-1].append(m)
    board_s[x-1][y-1].append(s)
    board_d[x-1][y-1].append(d)

def move_atom():
    global board_d, board_m, board_s
    test_m = [[[] for _ in range(n)] for _ in range(n)]
    test_s = [[[] for _ in range(n)] for _ in range(n)]
    test_d = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board_d[i][j]:
                for k in range(len(board_d[i][j])):
                    m, s, d = board_m[i][j][k], board_s[i][j][k], board_d[i][j][k]
                    nx = i
                    ny = j
                    for _ in range(board_s[i][j][k]):
                        nx = (nx + dx[board_d[i][j][k]] + n) % n
                        ny = (ny + dy[board_d[i][j][k]] + n) % n
                    test_m[nx][ny].append(m)
                    test_s[nx][ny].append(s)
                    test_d[nx][ny].append(d)

    board_m = test_m
    board_s = test_s
    board_d = test_d

def compose_atom():
    for i in range(n):
        for j in range(n):
            if len(board_m[i][j]) > 1:
                m = sum(board_m[i][j]) // 5
                if m == 0:
                    board_m[i][j].clear()
                    board_s[i][j].clear()
                    board_d[i][j].clear()
                    continue
                s = sum(board_s[i][j]) // len(board_s[i][j])
                board_m[i][j].clear()
                board_s[i][j].clear()
                for _ in range(4):
                    board_m[i][j].append(m)
                    board_s[i][j].append(s)
                signal = 0
                test = board_d[i][j][0] % 2
                for k in range(1, len(board_d[i][j])):
                    if test != (board_d[i][j][k] % 2):
                        signal = 1
                if signal == 0:
                    board_d[i][j].clear()
                    for q in range(0, 7, 2):
                        board_d[i][j].append(q)
                else:
                    board_d[i][j].clear()
                    for q in range(1, 8, 2):
                        board_d[i][j].append(q)

for turn in range(k):
    move_atom()
    compose_atom()

answer = 0 

for i in range(n):
    for j in range(n):
        if board_m[i][j]:
            answer += sum(board_m[i][j])
print(answer)