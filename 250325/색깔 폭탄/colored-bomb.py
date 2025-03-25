from collections import deque
import sys
import copy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
point = 0

def is_Finished():
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == board[i][j] or board[nx][ny] == 0:
                            return False
    return True

def delete_bomb(x, y):
    global point, board
    test_board = copy.deepcopy(board)
    Q = deque()
    Q.append((x, y))
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    test_board[x][y] = -2
    cnt = 1
    while Q:
        temp = Q.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] == board[x][y] or board[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = 1
                    test_board[nx][ny] = -2
                    cnt += 1
    board = test_board
    point += cnt * cnt

def find_package():
    visited = [[0] * n for _ in range(n)]
    check_package = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                Q = deque()
                Q.append((i, j))
                bomb_cnt = 1
                visited[i][j] = 1
                package = [(i, j)]
                visited_red = []
                red = 0
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            if board[nx][ny] == board[i][j] or board[nx][ny] == 0:
                                Q.append((nx, ny))
                                visited[nx][ny] = 1
                                bomb_cnt += 1
                                package.append((nx, ny))
                                if board[nx][ny] == 0:
                                    red += 1
                                    package.pop()
                                    visited_red.append((nx, ny))
                if visited_red:
                    for x, y in visited_red:
                        visited[x][y] = 0
                if bomb_cnt >= 2:
                    package.sort(key = lambda x : ((-x[0], x[1])))
                    a, b = package[0][0], package[0][1]
                    check_package.append((bomb_cnt, red, a, b))            
    if check_package:
        check_package.sort(key = lambda x : (-x[0], x[1], -x[2], x[3]))
        delete_bomb(check_package[0][2], check_package[0][3])

def rotate_270():
    global board
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[n-1-j][i] = board[i][j]
    board = arr

def gravity():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] >= 0:
                nx = i + 1
                while 1:
                    if  nx >= n or board[nx][j] == -1 or board[nx][j] >= 0:
                        nx -= 1
                        break
                    nx += 1
                if nx != i:
                    board[nx][j] = board[i][j]
                    board[i][j] = -2       
while 1:
    if is_Finished() == True:
        break
    find_package()
    gravity()
    rotate_270()
    gravity()
print(point)