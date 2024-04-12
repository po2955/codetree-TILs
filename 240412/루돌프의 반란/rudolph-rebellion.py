dx_r = [-1, -1, 0, 1, 1, 1, 0, -1]
dy_r = [0, 1, 1, 1, 0, -1, -1, -1]
dx_s = [-1, 0, 1, 0]
dy_s = [0, 1, 0, -1]
N, M, P, C ,D = map(int, input().split())
board = [[0] * N for _ in range(N)]
x, y = map(int, input().split())
x -= 1
y -= 1
board[x][y] = -1
santa_live = [0]
santa_stun = [0]
santa_point = [0]
for i in range(1, P + 1):
    santa, x, y = map(int, input().split())
    board[x-1][y-1] = santa
    santa_live.append(1)
    santa_point.append(0)
    santa_stun.append(0)

def find_rudolph():
    for i in range(N):
        for j in range(N):
            if board[i][j] == -1:
                return i, j

def communication_santa(Santa, Sx, Sy, d):
    global santa_live
    nx = Sx + dx_s[d]
    ny = Sy + dy_s[d]
    S = board[Sx][Sy]
    # print(Santa, nx, ny)
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 0:
            board[nx][ny] = S
        elif board[nx][ny] != 0:
            communication(board[nx][ny], nx, ny, d)
            board[nx][ny] = S
    else:
        santa_live[S] = 0
        # board[nx][ny] = Santa

def communication(Santa, Sx, Sy, d):
    global santa_live
    nx = Sx + dx_r[d]
    ny = Sy + dy_r[d]
    S = board[Sx][Sy]
    # print(Santa, nx, ny)
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 0:
            board[nx][ny] = Santa
        elif board[nx][ny] != 0:
            communication(board[nx][ny], nx, ny, d)
            board[nx][ny] = Santa
    else:
        santa_live[S] = 0
        # board[nx][ny] = Santa

def crush_rudolph(Santa, Rx, Ry, d):
    global santa_point, santa_live,santa_stun
    santa_point[Santa] += C
    santa_stun[Santa] = 2
    nx = Rx + (dx_r[d] * C)
    ny = Ry + (dy_r[d] * C)
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 0:
            board[nx][ny] = Santa
        elif board[nx][ny] != 0:
            communication(board[nx][ny],nx, ny, d)
            board[nx][ny] = Santa
    else:
        santa_live[Santa] = 0

def move_rudolph(r_x, r_y):
    santa = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and santa_live[board[i][j]] != 0:
                distance = (r_x-i)**2 + (r_y-j)**2
                santa.append((distance, i, j))
    if santa:
        santa = sorted(santa, key = lambda x: (x[0], -x[1], -x[2]))
    santa_x, santa_y = santa[0][1], santa[0][2]
    distance = 324234234
    for i in range(8):
        nx = r_x + dx_r[i]
        ny = r_y + dy_r[i]
        if 0 <= nx < N and 0 <= ny < N:
            if distance > (nx - santa_x)**2 + (ny - santa_y)**2:
                distance = (nx - santa_x)**2 + (ny - santa_y)**2
                Rx, Ry = nx, ny
                d = i
    board[r_x][r_y] = 0
    if board[Rx][Ry] == 0:
        board[Rx][Ry] = -1
    else:
        S = board[Rx][Ry]
        crush_rudolph(S,Rx,Ry,d)
        board[Rx][Ry] = -1

def crush_santa(S, Sx, Sy, d):
    global santa_live, santa_stun, santa_point
    santa_point[S] += D
    santa_stun[S] = 2
    d = (d + 2 + 4) % 4
    nx = Sx + (dx_s[d] * D)
    ny = Sy + (dy_s[d] * D)
    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 0:
            board[nx][ny] = S
        else:
            communication_santa(board[nx][ny],nx,ny,d)
            board[nx][ny] = S
    else:
        santa_live[S] = 0

def move_santa(S, r_x, r_y):
    for i in range(N):
        for j in range(N):
            if board[i][j] == S:
                board[i][j] = 0
                distance = (r_x - i)**2 + (r_y - j) ** 2
                check = []
                for k in range(4):
                    nx = i + dx_s[k]
                    ny = j + dy_s[k]
                    if 0 <= nx < N and 0 <= ny < N and distance > (r_x-nx) **2 + (r_y-ny)**2 and board[nx][ny] <= 0:
                        distance = (r_x - nx)**2 + (r_y - ny)**2
                        check.append((distance, nx , ny, k))
                if not check:
                    board[i][j] = S
                    return
                check = sorted(check, key = lambda x : (x[0], x[1], -x[2]))
                Nx, Ny, d = check[0][1], check[0][2], check[0][3]
                if board[Nx][Ny] == 0:
                    board[Nx][Ny] = S
                    return
                else:
                    crush_santa(S, Nx, Ny, d)
                    return

for turn in range(1, M + 1):
    r_x, r_y = find_rudolph()
    move_rudolph(r_x, r_y)
    r_x, r_y = find_rudolph()
    for santa in range(1, P + 1):
        if santa_live[santa] == 0 or santa_stun[santa] != 0:
            continue
        move_santa(santa, r_x, r_y)
    flag = 0
    for i in range(1, len(santa_stun)):
        if santa_stun[i] > 0:
            santa_stun[i] -= 1
        if santa_live[i] == 1:
            santa_point[i] += 1
    flag = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                flag = 1
    if flag == 0:
        break

for i in range(1, len(santa_point)):
    print(santa_point[i], end = ' ')