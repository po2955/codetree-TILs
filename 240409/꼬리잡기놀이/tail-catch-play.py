from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_people = [[0] * n for _ in range(n)]
point = 0
round = 0

for i in range(n):
    for j in range(n):
        if board[i][j] != 4:
            board_people[i][j] = board[i][j]
            if 1 <= board[i][j] <= 3:
                board[i][j] = 4

def move_team():
    global board_people
    test = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board_people[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and board_people[nx][ny] == 0:
                        Q = deque()
                        Q.append((nx, ny))
                        visited = [[0] * n for _ in range(n)]
                        visited[nx][ny] = 1
                        go = [(nx, ny)]
                        signal = 0
                        while Q:
                            temp = Q.popleft()
                            for q in range(4):
                                nnx = temp[0] + dx[q]
                                nny = temp[1] + dy[q]
                                if 0 <= nnx < n and 0 <= nny < n and visited[nnx][nny] == 0 and board[nnx][nny] == 4 and board_people[nnx][nny] >= 1:
                                    if board_people[nnx][nny] == 3:
                                        signal = 1
                                        break
                                    go.append((nnx, nny))
                                    Q.append((nnx, nny))
                                    visited[nnx][nny] = 1
                            if signal == 1:
                                break
                        break
                Q = deque()
                Q.append((i, j))
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                people = [board_people[i][j]]
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4 and board_people[nx][ny] >= 1:
                            visited[nx][ny] = 1
                            Q.append((nx, ny))
                            people.append(board_people[nx][ny])
                for k in range(len(people)):
                    x, y = go[k][0], go[k][1]
                    test[x][y] = people[k]
    board_people = test

def throw_ball(turn):
    global round, point
    if turn != 0 and turn % n == 0:
        round = (round + 1 + 4) % 4
    visited = [[0] * n for _ in range(n)]
    change = []
    if round == 0:
        turn %= 7
        for j in range(n):
            #공 잡았으면 몇 번짼지, 그룹화 시켜서 그 뒤에 같은 그룹 사람이 맞아도 카운트 안하게.
            if board_people[turn][j] >= 1:
                if board_people[turn][j] == 1 or board_people[turn][j] == 3:
                    change.append((turn, j))
                if board_people[turn][j] == 1:
                    point += 1
                Q = deque()
                Q.append((turn, j))
                visited[turn][j] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board_people[nx][ny] == 1:
                                point += visited[nx][ny] ** 2
                            if board_people[nx][ny] == 3 or board_people[nx][ny] == 1:
                                change.append((nx ,ny))
                            Q.append((nx, ny))
    elif round == 1:
        turn %= 7
        for i in range(n-1, -1, -1):
            #공 잡았으면 몇 번짼지, 그룹화 시켜서 그 뒤에 같은 그룹 사람이 맞아도 카운트 안하게.
            if board_people[i][turn] >= 1:
                if board_people[i][turn] == 1 or board_people[i][turn] == 3:
                    change.append((i, turn))
                if board_people[i][turn] == 1:
                    point += 1
                Q = deque()
                Q.append((i, turn))
                visited[i][turn] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board_people[nx][ny] == 1:
                                point += visited[nx][ny] ** 2
                            if board_people[nx][ny] == 3 or board_people[nx][ny] == 1:
                                change.append((nx ,ny))
                            Q.append((nx, ny))
    elif round == 2:
        turn = abs((turn % 7) - 6)
        for j in range(n-1, -1, -1):
            #공 잡았으면 몇 번짼지, 그룹화 시켜서 그 뒤에 같은 그룹 사람이 맞아도 카운트 안하게.
            if board_people[turn][j] >= 1:
                if board_people[turn][j] == 1 or board_people[turn][j] == 3:
                    change.append((turn, j))
                if board_people[turn][j] == 1:
                    point += 1
                Q = deque()
                Q.append((turn, j))
                visited[turn][j] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board_people[nx][ny] == 1:
                                point += visited[nx][ny] ** 2
                            if board_people[nx][ny] == 3 or board_people[nx][ny] == 1:
                                change.append((nx ,ny))
                            Q.append((nx, ny))
    elif round == 3:
        turn = abs((turn % 7) - 6)
        for i in range(n-1, -1, -1):
            #공 잡았으면 몇 번짼지, 그룹화 시켜서 그 뒤에 같은 그룹 사람이 맞아도 카운트 안하게.
            if board_people[i][turn] >= 1:
                if board_people[i][turn] == 1 or board_people[i][turn] == 3:
                    change.append((i, turn))
                if board_people[i][turn] == 1:
                    point += 1
                Q = deque()
                Q.append((i, turn))
                visited[i][turn] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board_people[nx][ny] == 1:
                                point += visited[nx][ny] ** 2
                            if board_people[nx][ny] == 3 or board_people[nx][ny] == 1:
                                change.append((nx ,ny))
                            Q.append((nx, ny))
    if change:
        for x, y in change:
            if board_people[x][y] == 1:
                board_people[x][y] = 3
            elif board_people[x][y] == 3:
                board_people[x][y] = 1


for turn in range(k):
    group = []
    move_team()
    throw_ball(turn)
print(point)