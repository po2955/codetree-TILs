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
                people = [board_people[i][j]]
                Q = deque()
                Q.append((i, j))
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                signal = 0
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4 and board_people[nx][ny] >= 1:
                            if board[nx][ny] == 2:
                                visited[nx][ny] = 1
                                Q.append((nx, ny))
                                people.append(board_people[nx][ny])
                            if board_people[nx][ny] == 3:
                                board_people[nx][ny] = -1
                                three = (nx, ny)
                Q = deque()
                Q.append((i, j))
                visited = [[0] * n for _ in range(n)]
                signal = 0
                go = []
                # for x in board_people:
                #     print(x, end = ' ')
                #     print()
                # print()
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and visited[nx][ny] == 0 and board_people[nx][ny] >= -1:
                            if board_people[nx][ny] <= 0:
                                test[nx][ny] = board_people[temp[0]][temp[1]]
                                board_people[temp[0]][temp[1]] = 0
                                visited[nx][ny] = 1
                                go.append((nx, ny))
                            if board_people[nx][ny] == 2:
                                Q.append((nx, ny))
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and board_people[nx][ny] == -1:
                            if temp[0] != i and temp[1] != j:
                                continue
                x, y = go[-1]
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx <n and 0 <= ny < n and board[nx][ny] == 4 and test[nx][ny] == 0:
                        test[nx][ny] = 3
                        break
    board_people = test

def throw_ball(turn):
    global round, point
    if turn != 0 and turn % n == 0:
        round = (round + 1 + 4) % 4
    visited = [[0] * n for _ in range(n)]
    change = []
    if round == 0:
        turn %= n
        for j in range(n):
            #공 잡았으면 몇 번짼지, 그룹화 시켜서 그 뒤에 같은 그룹 사람이 맞아도 카운트 안하게.
            if board_people[turn][j] >= 1 and visited[turn][j] == 0:
                # if board_people[turn][j] == 1 or board_people[turn][j] == 3:
                #     change.append((turn, j))
                if board_people[turn][j] == 1:
                    change.append((turn, j))
                    point += 1
                    visited[turn][j] = 1
                    Q = deque()
                    Q.append((turn, j))
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                Q.append((nx, ny))
                                if board_people[nx][ny] == 3:
                                    change.append((nx ,ny))
                    continue
                elif board_people[turn][j] == 3:
                    change.append((turn, j))
                    visited[turn][j] = 1
                    Q = deque()
                    Q.append((turn, j))
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and visited[nx][ny] == 0:
                                if board_people[nx][ny] == 1 and temp[0] == turn and temp[1] == j:
                                    continue
                                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                                Q.append((nx, ny))
                                if board_people[nx][ny] == 1:
                                    change.append((nx, ny))
                                    point += visited[nx][ny] ** 2
                    continue
                Q = deque()
                Q.append((turn, j))
                visited[turn][j] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4 and board_people[nx][ny] >= 1:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board_people[nx][ny] == 1:
                                point += visited[nx][ny] ** 2
                            if board_people[nx][ny] == 3 or board_people[nx][ny] == 1:
                                change.append((nx ,ny))
                                if board_people[nx][ny] == 3:
                                    continue
                            Q.append((nx, ny))
    elif round == 1:
        turn %= n
        for i in range(n-1, -1, -1):
            #공 잡았으면 몇 번짼지, 그룹화 시켜서 그 뒤에 같은 그룹 사람이 맞아도 카운트 안하게.
            if board_people[i][turn] >= 1 and visited[i][turn] == 0:
                if board_people[i][turn] == 1:
                    change.append((i, turn))
                    point += 1
                    Q= deque()
                    Q.append((i, turn))
                    visited[i][turn] = 1
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and visited[nx][ny] == 0:
                                Q.append((nx, ny))
                                visited[nx][ny] = 1
                                if board_people[nx][ny] == 3:
                                    change.append((nx, ny))
                    continue

                elif board_people[i][turn] == 3:
                    visited[i][turn] = 1
                    Q = deque()
                    Q.append((i, turn))
                    change.append((nx, ny))
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4:
                                if board_people[nx][ny] == 1 and temp[0] == i and temp[1] == turn:
                                    continue
                                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                                Q.append((nx, ny))
                                if board[nx][ny] == 1:
                                    change.append((nx, ny))
                                    point += visited[nx][ny] ** 2
                    continue

                Q = deque()
                Q.append((i, turn))
                visited[i][turn] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board_people[nx][ny] <= 2 and board[nx][ny] == 4:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board_people[nx][ny] == 1:
                                point += visited[nx][ny] ** 2
                            if board_people[nx][ny] == 3 or board_people[nx][ny] == 1:
                                change.append((nx ,ny))
                            Q.append((nx, ny))

    elif round == 2:
        turn = abs((turn % n) - (n-1))
        for j in range(n-1, -1, -1):
            # 공 잡았으면 몇 번짼지, 그룹화 시켜서 그 뒤에 같은 그룹 사람이 맞아도 카운트 안하게.
            if board_people[turn][j] >= 1 and visited[turn][j] == 0:
                # if board_people[turn][j] == 1 or board_people[turn][j] == 3:
                #     change.append((turn, j))
                if board_people[turn][j] == 1:
                    change.append((turn, j))
                    point += 1
                    visited[turn][j] = 1
                    Q = deque()
                    Q.append((turn, j))
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                Q.append((nx, ny))
                                if board_people[nx][ny] == 3:
                                    change.append((nx, ny))
                    continue
                elif board_people[turn][j] == 3:
                    change.append((turn, j))
                    visited[turn][j] = 1
                    Q = deque()
                    Q.append((turn, j))
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and visited[nx][ny] == 0:
                                if board_people[nx][ny] == 1 and temp[0] == turn and temp[1] == j:
                                    continue
                                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                                Q.append((nx, ny))
                                if board_people[nx][ny] == 1:
                                    change.append((nx, ny))
                                    point += visited[nx][ny] ** 2
                    continue
                Q = deque()
                Q.append((turn, j))
                visited[turn][j] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4 and \
                                board_people[nx][ny] >= 1:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board_people[nx][ny] == 1:
                                point += visited[nx][ny] ** 2
                            if board_people[nx][ny] == 3 or board_people[nx][ny] == 1:
                                change.append((nx, ny))
                                if board_people[nx][ny] == 3:
                                    continue
                            Q.append((nx, ny))
    elif round == 3:
        turn = abs((turn % n) - (n-1))
        for i in range(n-1, -1, -1):
            # 공 잡았으면 몇 번짼지, 그룹화 시켜서 그 뒤에 같은 그룹 사람이 맞아도 카운트 안하게.
            if board_people[i][turn] >= 1 and visited[i][turn] == 0:
                if board_people[i][turn] == 1:
                    change.append((i, turn))
                    point += 1
                    Q = deque()
                    Q.append((i, turn))
                    visited[i][turn] = 1
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 4 and visited[nx][ny] == 0:
                                Q.append((nx, ny))
                                visited[nx][ny] = 1
                                if board_people[nx][ny] == 3:
                                    change.append((nx, ny))
                    continue

                elif board_people[i][turn] == 3:
                    visited[i][turn] = 1
                    Q = deque()
                    Q.append((i, turn))
                    change.append((nx, ny))
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 4:
                                if board_people[nx][ny] == 1 and temp[0] == i and temp[1] == turn:
                                    continue
                                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                                Q.append((nx, ny))
                                if board[nx][ny] == 1:
                                    change.append((nx, ny))
                                    point += visited[nx][ny] ** 2
                    continue

                Q = deque()
                Q.append((i, turn))
                visited[i][turn] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board_people[nx][ny] <= 2 and \
                                board[nx][ny] == 4:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board_people[nx][ny] == 1:
                                point += visited[nx][ny] ** 2
                            if board_people[nx][ny] == 3 or board_people[nx][ny] == 1:
                                change.append((nx, ny))
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
    # for x in board_people:
    #     print(x, end =' ')
    #     print()
    # print()
    throw_ball(turn)

print(point)