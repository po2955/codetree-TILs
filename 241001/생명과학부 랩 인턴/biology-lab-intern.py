dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
cnt = 0
n, m, k = map(int, input().split())
board_b = [[0] * m for _ in range(n)]
board_d = [[0] * m for _ in range(n)]
board_s = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y, s, d, b = map(int, input().split())
    x -= 1
    y -= 1
    board_b[x][y], board_s[x][y], board_d[x][y] = b, s, d

def find_mold(j):
    global cnt
    for i in range(n):
        if board_b[i][j] > 0:
            cnt += board_b[i][j]
            board_b[i][j] = 0
            board_s[i][j] = 0
            board_d[i][j] = 0
            return

def move_mold():
    global board_s, board_d, board_b
    test_board_b = [[0] * m for _ in range(n)]
    test_board_d = [[0] * m for _ in range(n)]
    test_board_s = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board_b[i][j]:
                s, b, d = board_s[i][j], board_b[i][j], board_d[i][j]
                nx, ny = i, j
                for q in range(s):
                    nx = nx + dx[d]
                    ny = ny + dy[d]
                    if 0 > nx or n <= nx or ny < 0 or ny >= m:
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        elif d == 4:
                            d = 3
                        nx = nx + (dx[d] * 2)
                        ny = ny + (dy[d] * 2)
                if test_board_b[nx][ny] == 0:
                    test_board_b[nx][ny] = b
                    test_board_s[nx][ny] = s
                    test_board_d[nx][ny] = d
                else:
                    if test_board_b[nx][ny] > b:
                        continue
                    else:
                        test_board_b[nx][ny] = b
                        test_board_s[nx][ny] = s
                        test_board_d[nx][ny] = d
    board_b = test_board_b
    board_s = test_board_s
    board_d = test_board_d

for turn in range(m):
    find_mold(turn)
    move_mold()
print(cnt)