from collections import deque
from copy import deepcopy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
numbers = list(map(int, input().split()))
numbers = deque(numbers)

def check_point(test_board, x, y, angle):
    global check
    visited = [[0] * 5 for _ in range(5)]
    point = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                visited[i][j] = 1
                Q = deque()
                Q.append((i, j))
                cnt = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0 and test_board[nx][ny] == test_board[i][j]:
                            Q.append((nx, ny))
                            visited[nx][ny] = 1
                            cnt += 1
                if cnt >= 3:
                    point += cnt
    check.append((point, angle, y, x))

def rotate_90(x, y):
    test_board = deepcopy(board)
    ret = [[0] * 3 for _ in range(3)]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            ret[j-y][3-1-(i-x)] = board[i][j]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            test_board[i][j] = ret[i-x][j-y]
    check_point(test_board, x+1, y+1, 90)

def rotate_180(x, y):
    test_board = deepcopy(board)
    ret = [[0] * 3 for _ in range(3)]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            ret[3-1-(i-x)][3-1-(j-y)] = board[i][j]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            test_board[i][j] = ret[i-x][j-y]
    check_point(test_board, x + 1, y + 1, 180)

def rotate_270(x, y):
    test_board = deepcopy(board)
    ret = [[0] * 3 for _ in range(3)]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            ret[3-1-(j-y)][i-x] = board[i][j]
    for i in range(x, y):
        for j in range(x, y):
            test_board[i][j] = ret[i - x][j - y]
    check_point(test_board, x + 1, y + 1, 270)

def real_rotate_90(x, y):
    global board
    test_board = deepcopy(board)
    ret = [[0] * 3 for _ in range(3)]
    for i in range(x, x + 3):
        for j in range(y, y + 3) :
            ret[j - y][3 - 1 - (i - x)] = board[i][j]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            test_board[i][j] = ret[i - x][j - y]
    board = test_board

def real_rotate_180(x, y):
    global board
    test_board = deepcopy(board)
    ret = [[0] * 3 for _ in range(3)]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            ret[3-1-(i-x)][3-1-(j-y)] = board[i][j]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            test_board[i][j] = ret[i-x][j-y]
    board = test_board

def real_rotate_270(x, y):
    global board
    test_board = deepcopy(board)
    ret = [[0] * 3 for _ in range(3)]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            ret[3-1-(j-y)][i-x] = board[i][j]
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            test_board[i][j] = ret[i - x][j - y]
    board = test_board

def count_point():
    global answer, new_xy
    visited = [[0] * 5 for _ in range(5)]
    point = 0
    blank_xy = []
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                visited[i][j] = 1
                Q = deque()
                Q.append((i, j))
                blank = [(i, j)]
                cnt = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0 and board[nx][ny] == board[i][j]:
                            Q.append((nx, ny))
                            visited[nx][ny] = 1
                            cnt += 1
                            blank.append((nx, ny))
                if cnt >= 3:
                    blank_xy.append(blank)
                    point += cnt
    answer += point
    if blank_xy:
        for i in range(len(blank_xy)):
            for j in range(len(blank_xy[i])):
                x, y = blank_xy[i][j][0], blank_xy[i][j][1]
                board[x][y] = 0
                new_xy.append((x, y))

def fill_num():
    global new_xy, numbers, board
    if new_xy:
        new_xy = sorted(new_xy, key = lambda x: (x[1], -x[0]))
    new_xy = deque(new_xy)
    while new_xy:
        x, y = new_xy.popleft()
        num = numbers.popleft()
        board[x][y] = num

def is_Finished():
    visited = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                Q = deque()
                Q.append((i, j))
                visited[i][j] = 1
                cnt = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0 and board[nx][ny] == board[i][j]:
                            cnt += 1
                            Q.append((nx, ny))
                            visited[nx][ny] = 1
                if cnt >= 3:
                    return False
    return True

for turn in range(1, K + 1):
    check = []
    answer = 0
    new_xy = []
    for i in range(0, 3):
        for j in range(0, 3):
            rotate_90(i, j)
            rotate_180(i, j)
            rotate_270(i, j)
    if check:
        check = sorted(check, key = lambda x : (-x[0], x[1], x[2], x[3]))
    else:
        break
    x, y, angle = check[0][3], check[0][2], check[0][1]
    if angle == 90:
        real_rotate_90(x - 1, y - 1)
        while 1:
            count_point()
            fill_num()
            if is_Finished() == True:
                break
    elif angle == 180:
        real_rotate_180(x-1, y-1)
        while 1:
            count_point()
            fill_num()
            if is_Finished() == True:
                break
    else:
        real_rotate_270(x-1, y-1)
        while 1:
            count_point()
            fill_num()
            if is_Finished() == True:
                break
    if answer != 0:
        print(answer, end = ' ')