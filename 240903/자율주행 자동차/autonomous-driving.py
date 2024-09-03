from copy import deepcopy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n ,m = map(int, input().split())
x, y, d = map(int, input().split())
cnt = 1
board = [list(map(int, input().split())) for _ in range(n)]
visited = deepcopy(board)
board[x][y] = 2
visited[x][y] = -1
flag = 0
def check_left():
    check_d = deepcopy(d)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                check_d = (check_d - 1 + 4) % 4
                nx = x + dx[check_d]
                ny = y + dy[check_d]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                    return True
                else:
                    return False

def move_car():
    global x, y, d, cnt
    d = (d - 1 + 4) % 4
    nx = x + dx[d]
    ny = y + dy[d]
    board[nx][ny] = 2
    board[x][y] = -1
    cnt += 1
    x, y = nx, ny

def check_back():
    check_d = deepcopy(d)
    check_d = (check_d + 2 + 4) % 4
    nx = x + dx[check_d]
    ny = y + dy[check_d]
    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1:
        return True
    else:
        return False

def move_back():
    global x, y
    check_d = deepcopy(d)
    check_d = (check_d + 2 + 4) % 4
    nx = x + dx[check_d]
    ny = y + dy[check_d]
    board[x][y] = -1
    board[nx][ny] = 2
    x, y = nx, ny

while 1:
    if flag == 4:
        if check_back() == True:
            move_back()
            flag = 0
        elif check_back() == False:
            break
    if check_left() == True:
        flag = 0
        move_car()
    elif check_left() == False:
        flag += 1
        d = (d - 1 + 4) % 4

print(cnt)