from copy import deepcopy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dx_s = [-1, 0, 1, 0]
dy_s = [0, 1, 0, -1]
# dx_s_r = [1, 0, -1, 0]
# dy_s_r = [0, 1, 0, -1]
signal = 0
n, m, h, k = map(int, input().split())
board = [[[]for _ in range(n)] for _ in range(n)]
board_sullae = [[-1] * n for _ in range(n)]
board_tree = [[0] * n for _ in range(n)]
board[n//2][n//2].append(-1)
board_sullae[n//2][n//2] = 0
point = 0
move_go = []
move_reverse = [n-1]
l = 0
for i in range((n*2 - 2) // 2):
    l += 1
    move_go.append(l)
    move_go.append(l)
move_go.append(l)
for i in range((n*2 -2) // 2):
    move_reverse.append(l)
    move_reverse.append(l)
    l -= 1

for _ in range(m):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y].append(d)
for _ in range(h):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board_tree[x][y] = 1

def find_sullae():
    for i in range(n):
        for j in range(n):
            if board[i][j] and board[i][j][0] == -1:
                return i, j

def move_runner(s_x, s_y):
    global board
    test = [[[] for _ in range(n)]for _ in range(n)]
    test[s_x][s_y].append(-1)
    for i in range(n):
        for j in range(n):
            if board[i][j] and abs(i - s_x) + abs(j - s_y) > 3:
                while board[i][j]:
                    test[i][j].append(board[i][j].pop())
            elif board[i][j] and abs(i - s_x) + abs(j - s_y) <= 3:
                board[i][j].sort()
                dont_move = []
                while board[i][j]:
                    runner = board[i][j].pop()
                    if runner == -1:
                        board[i][j].append(-1)
                        break
                    nx = i + dx[runner]
                    ny = j + dy[runner]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] and board[nx][ny][0] == -1:
                            dont_move.append(runner)
                        else:
                            test[nx][ny].append(runner)
                    elif 0 > nx or nx >= n or 0 > ny or ny >= n:
                        runner = (runner + 2 + 4) % 4
                        nx = i + dx[runner]
                        ny = j + dy[runner]
                        if board[nx][ny] and board[nx][ny][0] == -1:
                            dont_move.append(runner)
                        else:
                            test[nx][ny].append(runner)
                if dont_move:
                    while dont_move:
                        runner = dont_move.pop()
                        test[i][j].append(runner)
    board = test
sullae_i = 0
move_cnt = 0
def move_sullae(s_x, s_y, turn):
    global signal, dx_s, dy_s, sullae_i, move_cnt, point, n
    catch = 0
    board[s_x][s_y].sort(reverse=True)
    sullae = board[s_x][s_y].pop()
    s_d = board_sullae[s_x][s_y]
    board_sullae[s_x][s_y] = -1
    if signal == 0:
        nx = s_x + dx_s[s_d]
        ny = s_y + dy_s[s_d]
        move_cnt += 1
        if move_cnt == move_go[sullae_i]:
            if nx != 0 or ny != 0:
                move_cnt = 0
                sullae_i += 1
                s_d = (s_d + 1 + 4) % 4
            elif nx == 0 and ny == 0:
                move_cnt = 0
                sullae_i = 0
                signal = 1
                s_d = 0
                dx_s = [1, 0, -1, 0]
                dy_s = [0, 1, 0, -1]
        board[nx][ny].append(sullae)
        board_sullae[nx][ny] = s_d
        board[nx][ny].sort()
        for i in range(3):
            nnx = nx + (dx_s[s_d] * i)
            nny = ny + (dy_s[s_d] * i)
            if 0 <= nnx < n and 0 <= nny < n and board[nnx][nny] and board[nnx][nny][-1] != -1:
                while board[nnx][nny]:
                    if board_tree[nnx][nny] == 1:
                        break
                    runner = board[nnx][nny].pop()
                    if runner == -1:
                        board[nnx][nny].append(-1)
                        break
                    catch += 1
    elif signal == 1:
        nx = s_x + dx_s[s_d]
        ny = s_y + dy_s[s_d]
        move_cnt += 1
        if move_cnt == move_reverse[sullae_i]:
            if nx != n // 2 or ny != n // 2:
                sullae_i += 1
                move_cnt = 0
                s_d = (s_d + 1 + 4) % 4
            elif nx == n // 2 and ny == n // 2:
                sullae_i = 0
                move_cnt = 0
                s_d = 0
                dx_s = [-1, 0, 1, 0]
                dy_s = [0, 1, 0, -1]
                signal = 0
        board[nx][ny].append(sullae)
        board[nx][ny].sort()
        board_sullae[nx][ny] = s_d
        for i in range(3):
            nnx = nx + (dx_s[s_d] * i)
            nny = ny + (dy_s[s_d] * i)
            if 0 <= nnx < n and 0 <= nny < n and board[nnx][nny] and board[nnx][nny][-1] != -1:
                while board[nnx][nny]:
                    if board_tree[nnx][nny] == 1:
                        break
                    runner = board[nnx][nny].pop()
                    if runner == -1:
                        board[nnx][nny].append(-1)
                        break
                    catch += 1
    point += (turn * catch)
for turn in range(1, k + 1):
    # for x in board:
    #     print(x, end =' ')
    #     print()
    # print()
    s_x, s_y = find_sullae()
    move_runner(s_x, s_y)
    # for x in board:
    #     print(x, end =' ')
    #     print()
    # print()
    move_sullae(s_x, s_y, turn)


print(point)