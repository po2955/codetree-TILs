from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def find_group():
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == 0:
                Q = deque()
                groups_num.append(board[i][j])
                xy = [(i,j)]
                Q.append((i, j))
                visited[i][j] = 1
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == board[i][j]:
                            Q.append((nx, ny))
                            visited[nx][ny] = 1
                            xy.append((nx, ny))
                groups.append(xy)

def count_point():
    global point
    for fir in range(len(groups_num)):
        first = groups_num[fir]
        first_cnt = len(groups[fir])
        for sec in range(fir + 1, len(groups_num)):
            second = groups_num[sec]
            second_cnt = len(groups[sec])
            touch = 0
            for x, y in groups[fir]:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) in groups[sec]:
                        touch += 1
            point += (first_cnt + second_cnt) * first * second * touch

def rotate():
    a = board[n//2]
    b = []
    for i in range(n):
        b.append(board[i][n//2])
    board[n//2] = b
    for i in range(n-1, -1, -1):
        board[i][n//2] = a[(n-1)-i]

    ret = [[0] * (n//2) for _ in range(n//2)]
    for i in range(0, n//2):
        for j in range(0, n//2):
            ret[j][n//2-1-i] = board[i][j]
    for i in range(0, n // 2):
        for j in range(0, n//2):
            board[i][j] = ret[i][j]

    # ret = [[0] * n for _ in range(n)]
    for i in range(n//2 + 1, n):
        for j in range(0, n//2):
            ret[j][n//2-1-(i - (n//2 + 1))] = board[i][j]
    for i in range(n//2 + 1, n):
        for j in range(0, n//2):
            board[i][j] = ret[i-(n//2+1)][j]

    # ret = [[0] * n for _ in range(n)]
    for i in range(n//2):
        for j in range(n//2 + 1, n):
            ret[j-(n//2 + 1)][n//2-1-i] = board[i][j]
    for i in range(n//2):
        for j in range(n//2 + 1, n):
            board[i][j] = ret[i][j-(n//2 + 1)]

    # ret = [[0] * n for _ in range(n)]
    for i in range(n//2 + 1, n):
        for j in range(n//2 + 1, n):
            ret[j-(n//2 + 1)][n//2-1-(i-(n//2 + 1))] = board[i][j]
    for i in range(n//2 + 1, n):
        for j in range(n//2 +1, n):
            board[i][j] = ret[i-(n//2 + 1)][j-(n//2 + 1)]

point = 0
for turn in range(4):
    groups = []
    groups_num = []
    find_group()
    count_point()
    rotate()

# for x in board:
#     print(x, end = ' ')
#     print()
print(point)