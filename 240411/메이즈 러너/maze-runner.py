from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
move_cnt = 0
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        board[i][j].append(a[j])
for _ in range(M):
    x, y = map(int, input().split())
    board[x-1][y-1].append(10)
x, y = map(int, input().split())
board[x-1][y-1].append(-1)

def is_Finished():
    for i in range(N):
        for j in range(N):
            if board[i][j] and board[i][j][-1] == 10:
                return False
    return True

def find_exit():
    for i in range(N):
        for j in range(N):
            if board[i][j] and -1 in board[i][j]:
                return i, j

def move_player(ex ,ey):
    global board, move_cnt
    move = []
    test = [[[] for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] and board[i][j][-1] < 10:
                test[i][j] = board[i][j]
            elif board[i][j] and board[i][j][-1] == 10:
                flag = 0
                distance = abs(i-ex) + abs(j-ey)
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] and 1 <= board[nx][ny][-1] <= 9:
                            continue
                        elif nx == ex and ny == ey:
                            # move_cnt += 1
                            if board[i][j][0] == 0:
                                for q in range(len(board[i][j]) - 1):
                                    move_cnt += 1
                            elif board[i][j][0] == 10:
                                for q in range(len(board[i][j])):
                                    move_cnt += 1
                            flag = 1
                            break
                        else:
                            if abs(nx-ex) + abs(ny-ey) < distance:
                                # move_cnt += 1
                                if board[i][j][0] == 0:
                                    l = len(board[i][j])-1
                                else:
                                    l = len(board[i][j])
                                for _ in range(l):
                                    move.append((nx, ny))
                                    move_cnt += 1
                                flag = 1
                                break
                if flag == 0:
                    if board[i][j][0] == 0:
                        l = len(board[i][j]) - 1
                    else:
                        l = len(board[i][j])
                    for _ in range(l):
                        move.append((i, j))
    if move:
        for x, y in move:
            test[x][y].append(10)
            test[x][y].sort()
    board = test

def real_rotate(x, y, l):
    ret = [[[] for _ in range(l)] for _ in range(l)]
    for i in range(x, x + l):
        for j in range(y, y + l):
            ret[j-y][l-(i-x)-1] = board[i][j]
    for i in range(x, x + l):
        for j in range(y, y + l):
            if ret[i-x][j-y] and 1 <= ret[i-x][j-y][-1] <= 9:
                ret[i-x][j-y][-1] -= 1
            board[i][j] = ret[i-x][j-y]
            board[i][j].sort()

def rotate(ex, ey):
    mindist = 234093458
    for i in range(N):
        for j in range(N):
            if 10 in board[i][j]:
                mindist = min(mindist, max(abs(i - ex), abs(j - ey)))
    mindist += 1
    for i in range(N):
        for j in range(N):
            flag1 = 0
            flag2 = 0
            if i + mindist <= N and j + mindist <= N:
                for p in range(i, i + mindist):
                    for q in range(j, j + mindist):
                        if 10 in board[p][q]:
                            flag1 = 1
                        if -1 in board[p][q]:
                            flag2 = 1
                if flag1 == 1 and flag2 == 1:
                    real_rotate(i, j, mindist)
                    return
for turn in range(K):
    if is_Finished() == True:
        break
    ex, ey = find_exit()
    move_player(ex, ey)
    rotate(ex, ey)

for i in range(N):
    for j in range(N):
        if board[i][j] and board[i][j][0] == -1:
            print(move_cnt)
            print(i + 1, j + 1)