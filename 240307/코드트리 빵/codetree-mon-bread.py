from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_people = [[[] for _ in range(n)] for _ in range(n)]
for i in range(1, m+1):
    x, y = map(int, input().split())
    board[x-1][y-1] = 100 + i

cant_base = []
cant_store = []

def place_people_base():
    global minute
    for i in range(n):
        for j in range(n):
            if board[i][j] == 100 + minute:
                Q = deque()
                Q.append((i, j))
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] >= 0:
                            visited[nx][ny] = 1
                            Q.append((nx, ny))
                            if board[nx][ny] == 1:
                                board_people[nx][ny].append(minute)
                                cant_base.append((nx, ny))
                                return

def find_convinience_store(x, y, people):
    # people += 100
    Q = deque()
    Q.append((x, y))
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    board_trace = [[None] * n for _ in range(n)]
    while Q:
        temp = Q.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] >= 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                board_trace[nx][ny] = (temp[0], temp[1])
                Q.append((nx, ny))
                if board[nx][ny] == people + 100:
                    if visited[nx][ny] == 1:
                        cant_store.append((nx,ny))
                        return
                    xx, yy = board_trace[nx][ny]
                    while xx != x or yy != y:
                        xxx, yyy = xx, yy
                        xx, yy = board_trace[xx][yy]
                    board_people[xxx][yyy].append(people)

def move_people():
    for i in range(n):
        for j in range(n):
            if board_people[i][j]:
                while board_people[i][j]:
                    find_convinience_store(i, j, board_people[i][j].pop())

def cant_pass():
    if cant_base:
        for x, y in cant_base:
            board[x][y] = -1
        cant_base.clear()
    if cant_store:
        for x, y in cant_store:
            board[x][y] = -(100 + board[x][y])
        cant_store.clear()

def is_Finished():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] < -100:
                cnt += 1
    if cnt == m:
        return True
    else:
        return False

minute = 1
place_people_base()
minute = 2
round = 1
while 1:

    move_people()
    if minute <= m:
        place_people_base()
    cant_pass()    
    if is_Finished() == True:
        break

    minute += 1
    round += 1

    # for x in board:
    #     print(x, end =' ')
    #     print()
    # print('-------------')
    # for x in board_people:
    #     print(x, end =' ')
    #     print()
    # print()
print(minute)