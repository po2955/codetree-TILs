from collections import deque
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def is_Finished():
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 1:
                cnt = 1
                Q = deque()
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                Q.append((i, j))
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            if board[nx][ny] == board[i][j] or board[nx][ny] == 0:
                                cnt += 1
                                visited[nx][ny] = 1
                                Q.append((nx, ny))
                if cnt >= 2:
                    return False
    return True

def remove_bomb(x, y):
    global point
    for i in range(n):
        for j in range(n):
            if board[i][j] == board[x][y]:
                cnt = 1
                Q = deque()
                visited = [[0] * n for _ in range(n)]
                Q.append((x, y))
                visited[x][y] = 1
                change = [(x, y)]
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            if board[nx][ny] == board[x][y] or board[nx][ny] == 0:
                                visited[nx][ny] = 1
                                Q.append((nx, ny))
                                change.append((nx, ny))
                                cnt += 1
                point += cnt * cnt
                for x, y in change:
                    board[x][y] = -2
                # for x in board:
                #     print(x, end = ' ')
                #     print()
                return

def find_maximum_bomb():
    check = []
    visited_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 1 and visited_board[i][j] == 0:
                visited_board[i][j] = 1
                cnt_bomb = 1
                cnt_red = 0
                check_dot = []
                check_dot.append((i, j))
                Q = deque()
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                Q.append((i, j))
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            if board[nx][ny] == board[i][j] or board[nx][ny] == 0:
                                visited_board[nx][ny] = 1
                                visited[nx][ny] = 1
                                Q.append((nx, ny))
                                cnt_bomb += 1
                                if board[nx][ny] == 0:
                                    cnt_red += 1
                                else:
                                    check_dot.append((nx, ny))
                if cnt_bomb >= 2:
                    check_dot = sorted(check_dot, key = lambda x : (-x[0], x[1]))
                    x, y = check_dot[0][0], check_dot[0][1]
                    check.append((cnt_bomb, cnt_red, x, y))
                else:
                    continue
    if not check:
        return
    
    check = sorted(check, key = lambda x : (-x[0], x[1], -x[2], x[3]))
    x, y = check[0][2], check[0][3]
    remove_bomb(x, y)

def gravity():
    for i in range(n-1, -1, -1):
        for j in range(n-2, -1, -1):
            if board[j][i] >= 0:
                a = board[j][i]
                for k in range(j+1, n):
                    if board[k][i] == -2:
                        board[k][i] = a
                        board[k-1][i] = -2
                    else:
                        break

def rotate_board():
    global board
    test = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            test[n-1-j][i] = board[i][j]
    board = test

point = 0
round = 0
while 1:
    
    if is_Finished() == True:
        break
    find_maximum_bomb()

    gravity()

    rotate_board()
    
    gravity()
    
print(point)