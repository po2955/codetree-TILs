from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
bomb_x = [-1, -1, 0, 1, 1, 1, 0, -1]
bomb_y = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
last_attack = [[0] * M for _ in range(N)]
is_attack = [[0] * M for _ in range(N)]

def select_attacker(turn):
    check = []
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                check.append((board[i][j], last_attack[i][j], i + j, j, i))
    check = sorted(check, key = lambda x : (x[0], -x[1], -x[2], -x[3]))
    attacker = check[0]
    x ,y = attacker[4], attacker[3]
    last_attack[x][y] = turn
    board[x][y] += N + M
    return x, y

def select_defenser():
    check = []
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                check.append((board[i][j], last_attack[i][j], i + j, j, i))
    check = sorted(check, key = lambda x : (-x[0], x[1], x[2], x[3]))
    defenser = check[0]
    x, y = defenser[4], defenser[3]
    return x, y

def laser_attack(check):
    damage = board[attack_x][attack_y]
    board[defense_x][defense_y] -= damage
    if board[defense_x][defense_y] <= 0:
        board[defense_x][defense_y] = 0
    x, y = check[defense_x][defense_y]
    while 1:
        if x == attack_x and y == attack_y:
            break
        board[x][y] -= damage // 2
        if board[x][y] <= 0:
            board[x][y] = 0
        is_attack[x][y] = 1
        x, y = check[x][y]

def bomb_attack():
    damage = board[attack_x][attack_y]
    board[defense_x][defense_y] -= damage
    if board[defense_x][defense_y] <= 0:
        board[defense_x][defense_y] = 0
    for i in range(8):
        nx = (defense_x + bomb_x[i] + N) % N
        ny = (defense_y + bomb_y[i] + M) % M
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] > 0:
            if nx == attack_x and ny == attack_y:
                continue
            board[nx][ny] -= damage // 2
            if board[nx][ny] <= 0:
                board[nx][ny] = 0
            is_attack[nx][ny] = 1

def attack(attx, atty, defx, defy):
    visited = [[-1] * M for _ in range(N)]
    visited[attx][atty] = 0
    Q = deque()
    Q.append((attx, atty))
    check = [[None] * M for _ in range(N)]
    while Q:
        temp = Q.popleft()
        for i in range(4):
            nx = (temp[0] + dx[i] + N) % N
            ny = (temp[1] + dy[i] + M) % M
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and board[nx][ny] > 0:
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                Q.append((nx, ny))
                check[nx][ny] = (temp[0], temp[1])
                if nx == defx and ny == defy:
                    laser_attack(check)
                    return
    bomb_attack()

def repair():
    for i in range(N):
        for j in range(M):
            if is_attack[i][j] == 0 and board[i][j] > 0:
                board[i][j] += 1
            elif is_attack[i][j] == 1:
                is_attack[i][j] = 0

for turn in range(1, K + 1):
    attack_x, attack_y = select_attacker(turn)
    defense_x, defense_y = select_defenser()
    is_attack[attack_x][attack_y], is_attack[defense_x][defense_y] = 1, 1
    attack(attack_x, attack_y, defense_x, defense_y)
    repair()

maximum = -12312313123
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            maximum = max(maximum, board[i][j])
print(maximum)