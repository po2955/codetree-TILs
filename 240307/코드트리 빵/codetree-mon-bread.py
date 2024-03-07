from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_people = [[[] for _ in range(n)] for _ in range(n)]
for i in range(1, m+1):
    x, y = map(int, input().split())
    board[x-1][y-1] = 100 + i
cant_pass = []
def place_people():
    for i in range(n):
        for j in range(n):
            if board_people[i][j]:
                return True
    return False

def base_people():
    for i in range(n):
        for j in range(n):
            if board[i][j] == minute + 100:
                Q = deque()
                visited = [[0] * n for _ in range(n)]
                Q.append((i, j))
                visited[i][j] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] >= 0:
                            visited[nx][ny] = 1
                            Q.append((nx ,ny))
                            if board[nx][ny] == 1:
                                # board[nx][ny] = -1
                                board_people[nx][ny].append(minute)
                                cant_pass.append((nx, ny))
                                return

def clear(move):
    for i in range(n):
        for j in range(n):
            if board_people[i][j]:
                board_people[i][j].clear()

    if move:
        for x, y, people in move:
            board_people[x][y].append(people)

def move_people():
    move = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 100:
                if board[i][j] - 100 >= minute:
                    continue
                people = board[i][j] - 100
                board_trace = [[None] * n for _ in range(n)]
                Q = deque()
                visited = [[-1] * n for _ in range(n)]
                Q.append((i,j))
                visited[i][j] = 0
                signal = 0
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                            if board[nx][ny] < 0 and people not in board_people[nx][ny]:
                                continue
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            Q.append((nx, ny))
                            board_trace[nx][ny] = (temp[0], temp[1])
                            
                            if people in board_people[nx][ny]:
                                if visited[nx][ny] == 1:
                                    xx, yy = board_trace[nx][ny]
                                    cant_pass.append((xx, yy))
                                    signal = 1
                                else:
                                    xx, yy = board_trace[nx][ny]
                                    move.append((xx, yy, people))
                                    signal = 1
                        if signal == 1:
                            break
                    if signal == 1:
                        break
    clear(move)
    

def ban():
    if cant_pass:
        for x, y in cant_pass:
            board[x][y] = -(board[x][y])
        cant_pass.clear()

def is_Finished():
    for i in range(n):
        for j in range(n):
            if board_people[i][j]:
                return False
    return True

minute = 1
base_people()
ban()
minute = 2
while 1:
    move_people()
    ban()
    if minute <= m:
        base_people()
    ban()
    if is_Finished() == True:
        break
    minute += 1

print(minute)