from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m, c = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        board[i][j].append(arr[j])
x, y = map(int, input().split())
x -= 1
y -= 1
board[x][y].append(-1)
sign = 0
for i in range(11, m + 11):
    x_s, y_s, x_e, y_e = map(int, input().split())
    x_s-=1
    y_s-=1
    x_e-=1
    y_e-=1
    board[x_s][y_s].append(i)
    board[x_e][y_e].append(-i)

def is_Finished():
    if c <= 0:
        return True
    return False

def is_Finished_two():
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for x in board[i][j]:
                    if x > 10:
                        return False
    return True

def find_car():
    for i in range(n):
        for j in range(n):
            if board[i][j] and -1 in board[i][j]:
                return i, j

def move_passenger(x_p, y_p, use):
    global c, sign
    for i in range(len(board[x_p][y_p])):
        if board[x_p][y_p][i] > 10:
            passenger = board[x_p][y_p][i]
            board[x_p][y_p][i] = 0
            break
    visited = [[-1] * n for _ in range(n)]
    visited[x_p][y_p] = 0
    Q = deque()
    Q.append((x_p, y_p))
    while Q:
        temp = Q.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and 1 not in board[nx][ny]:
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                Q.append((nx, ny))
                if -1 * passenger in board[nx][ny]:
                    if c - visited[nx][ny] < 0:
                        sign = 1
                        return
                    c -= visited[nx][ny]
                    c += visited[nx][ny] * 2
                    for i in range(len(board[nx][ny])):
                        if board[nx][ny][i] == -1 * passenger:
                            board[nx][ny][i] = 0
                            break
                    board[nx][ny].append(-1)
                    return

def find_passenger(car_x, car_y):
    global c, sign
    for i in range(len(board[car_x][car_y])):
        if board[car_x][car_y][i] > 10:
            move_passenger(car_x, car_y, 0)
            return
    visited = [[-1] * n for _ in range(n)]
    visited[car_x][car_y] = 0
    Q = deque()
    Q.append((car_x, car_y))
    check = []
    while Q:
        temp = Q.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and 1 not in board[nx][ny]:
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                Q.append((nx, ny))
                for j in range(len(board[nx][ny])):
                    if board[nx][ny][j] > 10:
                        check.append((visited[nx][ny], nx, ny))
    if check:
        check = sorted(check, key = lambda x : (x[0], x[1], x[2]))
        x_p, y_p = check[0][1], check[0][2]
        use_battery = visited[x_p][y_p]
        if c - use_battery <= 0:
            sign = 1
            return
        else:
            c -= use_battery
        move_passenger(x_p, y_p, use_battery)
    else:
        sign = 1

while 1:
    if is_Finished() == True or is_Finished_two() == True or sign == 1:
        break
    car_x, car_y = find_car()
    for i in range(len(board[car_x][car_y])):
        if board[car_x][car_y][i] == -1:
            board[car_x][car_y][i] = 0
            break
    find_passenger(car_x, car_y)

if sign == 1:
    print(-1)
else:
    print(c)