from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
cant = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        board[i][j].append(arr[j])
time = 1

for store in range(-11, -11 - m, -1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y].append(store)
    board[x][y].sort()

def go_base(time):
    global cant_base
    store = (time * -1) - 10
    people = time + 10
    check = []
    for i in range(n):
        for j in range(n):
            if board[i][j] and board[i][j][0] == store:
                Q = deque()
                Q.append((i, j))
                visited = [[-1] * n for _ in range(n)]
                visited[i][j] = 0
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and -1 not in board[nx][ny]:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            Q.append((nx, ny))
                            if 1 in board[nx][ny]:
                                check.append((visited[nx][ny], nx, ny))
    if check:
        check = sorted(check, key = lambda x : (x[0], x[1], x[2]))
        x, y = check[0][1], check[0][2]
        board[x][y].append(people)
        board[x][y].sort()
        cant_base.append((x, y))

def move(x, y, store):
    global cant
    people = store * -1
    Q = deque()
    Q.append((x, y))
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    check = []
    while Q:
        temp = Q.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < n and people in board[nx][ny]:
                for i in range(len(board[nx][ny])):
                    if board[nx][ny][i] == people:
                        board[nx][ny][i] = 0
                        break
                board[temp[0]][temp[1]].append(people)
                board[temp[0]][temp[1]].sort()
                if temp[0] == x and temp[1] == y:
                    cant.append((x, y))
                return
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and -1 not in board[nx][ny]:
                visited[nx][ny] = visited[temp[0]][temp[1]]
                Q.append((nx, ny))
                if people in board[nx][ny]:
                    for i in range(len(board[nx][ny])):
                        if board[nx][ny][i] == people:
                            board[nx][ny][i] = 0
                            break
                    board[temp[0]][temp[1]].append(people)
                    check.append((visited[temp[0]][temp[1]], temp[0], temp[1]))
    if check:
        check = sorted(key = lambda x : ((x[0], x[1], x[2])))
        a, b = check[0][1], check[0][2]
        board[a][b].append(people)

def move_people():
    for i in range(n):
        for j in range(n):
            if board[i][j] and board[i][j][0] < -10:
                move(i, j, board[i][j][0])

def is_Finished():
    for i in range(n):
        for j in range(n):
            if board[i][j] and board[i][j][0] < -10:
                return False
    return True
while 1:
    cant_base = []
    move_people()
    if cant:
        for x, y in cant:
            cnt = 0
            for i in range(len(board[x][y])):
                if board[x][y][i] > 10:
                    cnt += 1
            if cnt <= 1:
                board[x][y].clear()
            board[x][y].append(-1)
            cant = []
    if time <= m:
        go_base(time)
    if cant_base:
        for x, y in cant_base:
            board[x][y].append(-1)
            board[x][y].sort()
    if is_Finished() == True:
        break
    time += 1

print(time)