from collections import deque
from copy import deepcopy
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx_p = [-1, 0, 1, 0]
dy_p = [0, -1, 0, 1]
m, t = map(int, input().split())
r, c = map(int, input().split())
board_egg = [[[] for _ in range(4)] for _ in range(4)]
board = [[[] for _ in range(4)] for _ in range(4)]
board[r-1][c-1].append(-4)
for _ in range(m):
    r, c, d = map(int, input().split())
    board[r-1][c-1].append(d)

def copy_monster():
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                for x in board[i][j]:
                    if 0 < x <= 8:
                        board_egg[i][j].append(x)

def move_monster():
    global board
    test = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                # if -3 in board[i][j] or -2 in board[i][j] or -1 in board[i][j]:
                for k in range(len(board[i][j])):
                    if board[i][j][k] < 0:
                        test[i][j].append(board[i][j][k])
            # else:
                    else:
                        signal = 0
                        d = board[i][j][k]
                        if 0 < board[i][j][k]:
                            nx = i + dx[d]
                            ny = j + dy[d]
                            if 0 <= nx < 4 and 0 <= ny < 4 and -4 not in board[nx][ny] and -3 not in board[nx][ny] and -2 not in board[nx][ny] and -1 not in board[nx][ny]:
                                test[nx][ny].append(d)
                                signal = 1
                            else:
                                for k in range(d+1, d+9):
                                    nd = ((k + 9) + 9) % 9
                                    if nd == 0:
                                        continue
                                    nx = i + dx[nd]
                                    ny = j + dy[nd]
                                    if 0 <= nx < 4 and 0 <= ny < 4 and -4 not in board[nx][ny] and -3 not in board[nx][ny] and -2 not in board[nx][ny] and -1 not in board[nx][ny]:
                                        test[nx][ny].append(nd)
                                        signal = 1
                                        break
                        if signal == 0:
                            test[i][j].append(d)
    board = test

def move_packman():
    for i in range(4):
        for j in range(4):
            if -4 in board[i][j]:
                board[i][j].sort(reverse=True)
                pack = board[i][j].pop()
                maximum = -123123
                cnt = 0
                for k in range(4):
                    nx = i + dx_p[k]
                    ny = j + dy_p[k]
                    a = 0
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if board[nx][ny]:
                            for x in board[nx][ny]:
                                if x > 0:
                                    cnt += 1
                                    a += 1
                        for q in range(4):
                            nxx = nx + dx_p[q]
                            nyy = ny + dy_p[q]
                            b = 0
                            if 0 <= nxx < 4 and 0 <= nyy < 4:
                                if board[nxx][nyy]:
                                    for x in board[nxx][nyy]:
                                        if x > 0:
                                            cnt += 1
                                            b += 1
                                for p in range(4):
                                    nxxx = nxx + dx_p[p]
                                    nyyy = nyy + dy_p[p]
                                    c = 0
                                    if 0 <= nxxx < 4 and 0 <= nyyy < 4:
                                        if board[nxxx][nyyy]:
                                            for x in board[nxxx][nyyy]:
                                                if x > 0:
                                                    cnt += 1
                                                    c += 1
                                        if maximum < cnt:
                                            test =[(nx, ny), (nxx, nyy), (nxxx, nyyy)]
                                            if test[0] != test[1] and test[0] != test[2] and test[1] != test[2]:   
                                                maximum = cnt
                                                check = [(nx, ny), (nxx, nyy), (nxxx, nyyy)]
                                                # print(check)
                                    cnt -= c
                            cnt -= b
                    cnt -= a
    for x, y in check:
        if board[x][y]:
            for i in range(len(board[x][y])):
                if board[x][y][i] > 0:
                    board[x][y][i] = -3
    x, y = check[2][0], check[2][1]
    board[x][y].append(pack)
def remove_dead():
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                for k in range(len(board[i][j])):
                    if -3 <= board[i][j][k] <= -1:
                        board[i][j][k] += 1
                while 0 in board[i][j]:
                    board[i][j].remove(0)

def complete_copy():
    for i in range(4):
        for j in range(4):
            if board_egg[i][j]:
                while board_egg[i][j]:
                    monster = board_egg[i][j].pop()
                    board[i][j].append(monster)
for turn in range(t):
    copy_monster()
    
    move_monster()
    # if turn == 1:
    #     for x in board:
    #         print(x, end = ' ')
    #         print()
    #     print()
    move_packman()
    
    remove_dead()
    
    complete_copy()
    
answer = 0
for i in range(4):
    for j in range(4):
        if board[i][j]:
            for x in board[i][j]:
                if x > 0:
                    answer += 1
print(answer)