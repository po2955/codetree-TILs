from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
bomb_cnt = 0
def is_Finished():
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == board[i][j] or board[nx][ny] == 0:
                            return False
    return True

def choice_package():
    global bomb_cnt
    visited = [[0] * n for _ in range(n)]
    list_package = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 1:
                Q = deque()
                Q.append((i, j))
                visited[i][j] = 1
                cnt = 1
                cnt_red = 0
                list_row_col = [(i,j)]
                red_xy = [] #visited에서 빨간색 좌표는 다시 0으로 초기화
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            if board[nx][ny] == board[i][j] or board[nx][ny] == 0:
                                Q.append((nx, ny))
                                visited[nx][ny] = 1
                                cnt += 1
                                if board[nx][ny] != 0:
                                    list_row_col.append((nx, ny))
                                if board[nx][ny] == 0:
                                    cnt_red += 1
                                    red_xy.append((nx, ny))
                if red_xy:
                    for x, y in red_xy:
                        visited[x][y] = 0
                if cnt >= 2:
                    list_row_col = sorted(list_row_col, key = lambda x: (-x[0], x[1]))
                    x, y = list_row_col[0][0], list_row_col[0][1]
                    list_package.append((cnt, cnt_red, x, y))
    x, y = -1, -1
    if list_package:
        list_package = sorted(list_package, key = lambda x : (-x[0], x[1], -x[2], x[3]))
        x, y = list_package[0][2], list_package[0][3]
        bomb_cnt = list_package[0][0]
    return x, y

def remove_bomb(x, y):
    global board
    Q = deque()
    Q.append((x, y))
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    while Q:
        temp = Q.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] == 0 or board[nx][ny] == board[x][y]:
                    board[nx][ny] = -2
                    Q.append((nx, ny))
                    visited[nx][ny] = 1
    board[x][y] = -2

def gravity():
    global board
    for i in range(n-2, -1, -1):
        for j in range(n-1, -1, -1):
            if board[i][j] >= 0 and board[i+1][j] == -2:
                q = i + 1
                color = board[i][j]
                while 1:
                    board[q - 1][j] = -2
                    q += 1

                    if q == n or board[q][j] != -2:
                        board[q-1][j] = color
                        break

def rotate_270():
    global board
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[n-1-j][i] = board[i][j]
    board = a

answer = 0
while 1:
    if is_Finished() == True:
        break
    x, y = choice_package()
    if x != -1 or y != -1:
        remove_bomb(x ,y)
    gravity()
    rotate_270()
    gravity()
    answer += bomb_cnt ** 2
    bomb_cnt = 0
print(answer)