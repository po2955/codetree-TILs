from copy import deepcopy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dxc = [-1, -1, 1, 1]
dyc = [-1, 1, 1, -1]

n, m, k, c = map(int, input().split())
answer = 0
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            board[i][j] = -11

def grow_tree():
    global board
    test_board = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                        test_board[i][j] += 1
    board = test_board

def spread_tree():
    global board
    test_board = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                cnt = 0
                check_blank = []
                for q in range(4):
                    nx = i + dx[q]
                    ny = j + dy[q]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        cnt += 1
                        check_blank.append((nx, ny))
                if cnt >= 1:
                    for x, y in check_blank:
                        test_board[x][y] += board[i][j] // cnt
    board = test_board

def choice_killer():
    global answer
    check = []
    for i in range(n):
        for j in range(n):
            if -10 <= board[i][j] <= 0:
                check.append((0, i, j))
                continue
            elif board[i][j] > 0:
                cnt = board[i][j]
                for q in range(4):
                    for p in range(1, k + 1):
                        nx = i + (dxc[q] * p)
                        ny = j + (dyc[q] * p)
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] <= 0:
                                break
                            elif board[nx][ny] > 0:
                                cnt += board[nx][ny]
                check.append((cnt, i, j))
    if check:
        check = sorted(check, key = lambda x : (-x[0], x[1], x[2]))
        answer += check[0][0]
        return check[0][1], check[0][2]
    return -1, -1

def spread_killer(x, y):
    global k
    board[x][y] = -c
    for q in range(4):
        for p in range(1, k+1):
            nx = x + (dxc[q] * p)
            ny = y + (dyc[q] * p)
            if 0 <= nx < n and 0 <= ny < n:
                if -10 <= board[nx][ny] <= 0:
                    board[nx][ny] = -c
                    break
                elif board[nx][ny] == -11:
                    break
                else:
                    board[nx][ny] = -c

def count_killer():
    for i in range(n):
        for j in range(n):
            if -11 < board[i][j] < 0:
                board[i][j] += 1

for turn in range(1, m + 1):
    grow_tree()
    spread_tree()
    kill_x, kill_y = choice_killer()
    count_killer()
    if kill_x != -1:
        spread_killer(kill_x, kill_y)
print(answer)