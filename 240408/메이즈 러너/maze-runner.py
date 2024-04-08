from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        board[i][j].append(a[j])
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y][0] = 10
x, y = map(int, input().split())
board[x-1][y-1][0] = -1
move_cnt = 0

def find_exit():
    for i in range(N):
        for j in range(N):
            if board[i][j] and board[i][j][0] == -1:
                return i, j

def move_challenger(e_x, e_y):
    global move_cnt, board
    test = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            board[i][j].sort()
            if board[i][j] and board[i][j][-1] == 10:
                signal = 0
                distance = abs(i-e_x) + abs(j - e_y)
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] and board[nx][ny][0] == -1:
                        signal = 1
                        while board[i][j]:
                            a = board[i][j].pop()
                            if a == 0:
                                test[i][j].append(a)
                                break
                            move_cnt += 1
                        break
                    elif 0 <= nx < N and 0 <= ny < N and board[nx][ny] and 1 <= board[nx][ny][0] <= 9:
                        continue
                    elif 0 <= nx < N and 0 <= ny < N:
                        if distance > abs(nx-e_x) + abs(ny-e_y):
                            signal = 1
                            while board[i][j]:
                                challenger = board[i][j].pop()
                                if challenger == 0:
                                    test[i][j].append(0)
                                    break
                                test[nx][ny].append(challenger)
                                move_cnt += 1
                            break
                if signal == 0:
                    test[i][j] = board[i][j]
            else:
                if board[i][j]:
                    for x in board[i][j]:
                        test[i][j].append(x)

    board = test
def rotate(x, y, mindist):
    test = [[[] for _ in range(mindist)] for _ in range(mindist)]
    for i in range(x, x + mindist):
        for j in range(y, y + mindist):
            test[j-y][mindist-1-(i-x)] = board[i][j]

    for i in range(x, x + mindist):
        for j in range(y, y + mindist):
            board[i][j] = test[i-x][j-y]
            if board[i][j] and 1 <= board[i][j][0] <= 9:
                board[i][j][0] -= 1

def rotate_maze(e_x, e_y):
    #1 정사각형의 크기 구하기
    mindist = 23587345
    for i in range(N):
        for j in range(N):
            board[i][j].sort()
            if board[i][j] and board[i][j][-1] == 10:
                mindist = min(mindist, max(abs(e_x - i) + 1, abs(e_y - j) + 1))
    #2 구한 정사각형 크기에 맞고, 조건에 맞는 왼쪽 최상단 좌표를 구하자
    for i in range(N):
        for j in range(N):
            flag_1 = 0
            flag_2 = 0
            for x in range(i, i + mindist):
                for y in range(j, j + mindist):
                    if x < N and y < N:
                        if board[x][y] and board[x][y][-1] == 10:
                            flag_1 = 1
                        if board[x][y] and board[x][y][-1] == -1:
                            flag_2 = 1
            if flag_1 == 1 and flag_2 == 1:
                rotate(i, j, mindist)
                return

def is_Finished():
    for i in range(N):
        for j in range(N):
            board[i][j].sort()
            if board[i][j] and board[i][j][-1] == 10:
                return False
    return True

for turn in range(1, K + 1):
    e_x, e_y = find_exit()
    move_challenger(e_x, e_y)
    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print()
    rotate_maze(e_x, e_y)
    if is_Finished() == True:
        break
exit = []
for i in range(N):
    for j in range(N):
        if board[i][j] and board[i][j][0] == -1:
            exit.append(i)
            exit.append(j)
print(move_cnt)
print(exit[0] + 1, exit[1] + 1)