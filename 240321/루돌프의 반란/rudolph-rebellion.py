dx_R = [-1, -1, 0, 1, 1, 1, 0, -1]
dy_R = [0, 1, 1, 1, 0, -1, -1, -1]
dx_S = [-1, 0, 1, 0]
dy_S = [0, 1, 0, -1]
N, M, P, C, D = map(int, input().split())
# C : 루돌프에 의해 산타가 밀려날 때 얻을 점수와 밀려날 칸
# D : 산타에 의해 산타가 밀려날 때 얻을 점수와 밀려날 칸
board = [[[] for _ in range(N)] for _ in range(N)]
board_stun = [[0] * N for _ in range(N)]
point = [0]
#루돌프 x,y
x, y = map(int, input().split())
x-= 1
y -= 1
board[x][y].append(-1)
for santa in range(1, P + 1):
    a, x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y].append(a)
    point.append(0)

def communication_rudolph(x, y, d):
    santa = board[x][y].pop()
    nx = x + dx_R[d]
    ny = y + dy_R[d]
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny]:
            board[nx][ny].insert(0, santa)
            communication_rudolph(nx, ny, d)
        else:
            board[nx][ny].append(santa)

def crush_rudolph(d, R_x, R_y):
    point[board[R_x][R_y][-1]] += C
    S_nx = R_x + (dx_R[d] * C)
    S_ny = R_y + (dy_R[d] * C)
    santa = board[R_x][R_y].pop()

    if 0 <= S_nx < N and 0 <= S_ny < N:
        if board[S_nx][S_ny]:
            board[S_nx][S_ny].insert(0, santa)
            communication_rudolph(S_nx, S_ny, d)
            board_stun[S_nx][S_ny] = 2
        else:
            board[S_nx][S_ny].append(santa)
            board_stun[S_nx][S_ny]= 2

def move_rudolph():
    santa_xy = []
    signal = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                if board[i][j][0] == -1:
                    R_x, R_y = i, j
                    signal = 1
            if signal == 1:
                break
        if signal == 1:
                break
    for i in range(N):
        for j in range(N):            
            if board[i][j] and board[i][j][0] > 0:
                dis = (i - R_x) ** 2 + (j - R_y) ** 2
                santa_xy.append((i, j, dis))
    # print(santa_xy)
    if santa_xy:
        santa_xy = sorted(santa_xy, key = lambda x : (x[2], -x[0], -x[1]))
        santa = santa_xy[0]
    distance = 2359347539487
    for i in range(8):
        nx = R_x + dx_R[i]
        ny = R_y + dy_R[i]
        if 0 <= nx < N and 0 <= ny < N and (santa[0] - nx)**2 + (santa[1] - ny)**2 < distance:
            distance = (santa[0] - nx)**2 + (santa[1] - ny)**2
            R_nx, R_ny = nx, ny
            d = i
    R = board[R_x][R_y].pop()
    board[R_nx][R_ny].append(R)
    board[R_nx][R_ny].sort()
    if board[R_nx][R_ny][-1] > 0:
        crush_rudolph(d, R_nx, R_ny)
    return R_nx, R_ny

def communication_santa(x, y, d):
    santa = board[x][y].pop()
    nx = x + dx_S[d]
    ny = y + dy_S[d]
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny]:
            board[nx][ny].insert(0, santa)
        else:
            board[nx][ny].append(santa)

def crush_santa(d, S_x, S_y):
    point[board[S_x][S_y][-1]] += D
    santa = board[S_x][S_y].pop()
    d = (d + 2 + 4) % 4
    S_nx = S_x + (dx_S[d] * D)
    S_ny = S_y + (dy_S[d] * D)
    if 0 <= S_nx < N and 0 <= S_ny <N:
        if board[S_nx][S_ny]:
            board[S_nx][S_ny].insert(0, santa)
            communication_santa(S_nx, S_ny, d)
            board_stun[S_nx][S_ny] = 2
        else:
            board[S_nx][S_ny].append(santa)
            board_stun[S_nx][S_ny] = 2

def move_santa(t, R_x, R_y):
    for i in range(N):
        for j in range(N):
            if board[i][j] and board[i][j][-1] == t and board_stun[i][j] == 0:
                now = (i - R_x) ** 2 + (j - R_y) ** 2
                check = []
                for k in range(4):
                    nx = dx_S[k] + i
                    ny = dy_S[k] + j
                    next = (nx - R_x) ** 2 + (ny - R_y) ** 2
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] and board[nx][ny][0] > 0:
                            continue
                        if now > next:
                            check.append((next, nx , ny, k))
                if not check:
                    return
                check = sorted(check, key = lambda x : x[0])    
                S_x, S_y = check[0][1], check[0][2]
                d = check[0][3]
                santa = board[i][j].pop()
                if board[S_x][S_y]:
                    board[S_x][S_y].append(santa)
                    if board[S_x][S_y][0] == -1:
                        board[S_x][S_y].sort()
                        crush_santa(d, S_x, S_y)
                    # elif len(board[S_x][S_y]) > 1:
                    #     communication()
                else:
                    board[S_x][S_y].append(santa)
                return

def count_stun():
    for i in range(N):
        for j in range(N):
            if board_stun[i][j] > 0:
                board_stun[i][j] -= 1

def no_santa():
    for i in range(N):
        for j in range(N):
            if board[i][j] and board[i][j][-1] > 0:
                return False
    return True

def add_point():
    for i in range(N):
        for j in range(N):
            if board[i][j] and board[i][j][-1] > 0:
                point[board[i][j][-1]] += 1

for turn in range(M):
    R_x, R_y = move_rudolph()
    
    for t in range(1, P + 1):
        move_santa(t, R_x, R_y)
    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print(turn + 1, point)
    # print()    
    count_stun()
    if no_santa() == True:
        break

    add_point()
    
for i in range(1, len(point)):
    print(point[i], end =' ')