from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m, c = map(int, input().split())
battery = c
use_battery = 0
signal = 0
board =[[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    push = list(map(int, input().split()))
    for j in range(n):
        board[i][j].append(push[j])
x, y = map(int, input().split())
board[x-1][y-1].append(-1)
for i in range(1, m + 1):
    xs, ys, xe, ye = map(int, input().split())
    board[xs-1][ys-1].append(i * 1000)
    board[xs-1][ys-1].sort()
    board[xe-1][ye-1].append(-1 * i * 1000)
    board[xe-1][ye-1].sort()
def find_car():
    for i in range(n):
        for j in range(n):
            if -1 in board[i][j]:
                for k in range(len(board[i][j])):
                    if board[i][j][k] == -1:
                        board[i][j][k] = 0
                        break
                board[i][j].sort()
                return i, j

def arrive(ex, ey):
    global battery, use_battery
    board[ex][ey].append(-1)
    board[ex][ey].sort()
    battery += (2 * use_battery)
    use_battery = 0

def move_passenger(px, py, passenger):
    global use_battery, battery, signal
    Q = deque()
    Q.append((px, py))
    visited = [[-1] * n for _ in range(n)]
    visited[px][py] = 0
    while Q:
        temp = Q.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and board[nx][ny][0] != 1:
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                Q.append((nx, ny))
                if board[nx][ny] and (-1 * passenger) in board[nx][ny]:
                    for k in range(len(board[nx][ny])):
                        if (-1 * passenger) == board[nx][ny][k]:
                            board[nx][ny][k] = 0
                            break
                    use_battery += visited[nx][ny]
                    battery -= visited[nx][ny]
                    if battery < 0:
                        signal = 1
                        return
                    arrive(nx, ny)
                    return
    signal = 1
    return

def find_passenger(car_x, car_y):
    global use_battery, signal, battery
    if board[car_x][car_y] and board[car_x][car_y][-1] >= 1000:
        passenger = board[car_x][car_y][-1]
        board[car_x][car_y][-1] = 0
        move_passenger(car_x, car_y, passenger)
        return
    Q = deque()
    Q.append((car_x, car_y))
    visited = [[-1] * n for _ in range(n)]
    visited[car_x][car_y] = 0
    check = []
    while Q:
        temp = Q.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and board[nx][ny][0] != 1:
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                Q.append((nx, ny))
                if board[nx][ny][-1] >= 1000:
                    check.append((nx, ny, visited[nx][ny]))
    if not check:
        signal = 1
        return
    check = sorted(check, key = lambda x :(x[2], x[0], x[1]))
    nx, ny, use = check[0][0], check[0][1], check[0][2]
    passenger = board[nx][ny][-1]
    board[nx][ny][-1] = 0
    # use_battery += use
    battery -= use
    if battery < 0:
        signal = 1
        return
    move_passenger(nx, ny, passenger)
    return

def is_Finished2():
    for i in range(n):
        for j in range(n):
            if board[i][j][0] <= -1000 or board[i][j][0] >= 1000 or board[i][j][-1] <= -1000 or board[i][j][-1] >= 1000:
                return False
    return True

while 1:
    if is_Finished2() == True:
        print(battery)
        break
    car_x, car_y = find_car()
    find_passenger(car_x, car_y)
    if signal == 1:
        print(-1)
        break