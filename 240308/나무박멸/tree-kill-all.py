from copy import deepcopy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            board[i][j] = 1000

def grow_tree():
    test = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if 0 <board[i][j] < 1000:
                for q in range(0, 7, 2):
                    nx = i + dx[q]
                    ny = j + dy[q]
                    if 0 <= nx < n and 0 <= ny < n and 1000 > board[nx][ny] > 0:
                        test[i][j] += 1
    for i in range(n):
        for j in range(n):
            if test[i][j]:
                board[i][j] += test[i][j]
                
def spread_tree():
    global board
    test = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if 1000 > board[i][j] > 0:
                cnt = 0
                spread = []
                for q in range(0, 7, 2):
                    nx = i + dx[q]
                    ny = j + dy[q]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        cnt += 1
                        spread.append((nx, ny))
                if cnt != 0:
                    tree = board[i][j] // cnt
                    for x, y in spread:
                        test[x][y] += tree
    board = test

def tree_killer():
    global answer
    maximum = -12312763417486
    max_xy = ()
    for i in range(n):
        for j in range(n):
            if 1000 > board[i][j] > 0:
                cnt = board[i][j]
                for q in range(1, 8, 2):
                    nx = i
                    ny = j
                    for _ in range(k):
                        nx = nx + dx[q]
                        ny = ny + dy[q]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] == 0 or board[nx][ny] == 1000:
                                break
                            elif 1000 > board[nx][ny] > 0:
                                cnt += board[nx][ny]
                if maximum < cnt:
                    maximum = cnt
                    max_xy = (i, j)
    
    if max_xy:
        x, y = max_xy
        answer += board[x][y]
        board[x][y] = -c
        for q in range(1, 8, 2):
            nx = x
            ny = y
            for _ in range(k):
                nx = nx + dx[q]
                ny = ny + dy[q]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 1000:
                        break
                    elif board[nx][ny] == 0:
                        board[nx][ny] = -c
                        break
                    else:
                        if 1000 > board[nx][ny] > 0:
                            answer += board[nx][ny]
                        board[nx][ny] = -c
def reduce_killer():
    for i in range(n):
        for j in range(n):
            if -10 <= board[i][j] <= -1:
                board[i][j] += 1
answer = 0
for turn in range(m):
    
    grow_tree()
    spread_tree()
    reduce_killer()
    tree_killer()
    
print(answer)