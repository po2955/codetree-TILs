from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
point = 0

def find_group():
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                groups_num.append(board[i][j])
                visited[i][j] = 1
                Q = deque()
                Q.append((i, j))
                xy = []
                xy.append((i,j))
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == board[i][j]:
                            Q.append((nx, ny))
                            visited[nx][ny] = 1
                            xy.append((nx , ny))
                groups.append(xy)

def count_point():
    global point
    for first in range(len(groups_num)):
        first_num = groups_num[first]
        first_cnt = len(groups[first])
        for second in range(first+1, len(groups_num)):
            touch = 0
            secnd_num = groups_num[second]
            second_cnt = len(groups[second])
            for x, y in groups[first]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) in groups[second]:
                        touch += 1
            point += (first_cnt + second_cnt) * first_num * secnd_num * touch

def rotate():
    row = []
    feature = []
    for i in range(len(board)):
        row.append(board[i][n//2])
    for i in range(len(board[0])):
        feature.append(board[n//2][i])
    board[n//2] = row
    for i in range(len(feature) -1, -1, -1):
        board[len(feature)-1-i][n//2] = feature[i]

    ret = [[0] * (n//2) for _ in range(n//2)]
    for i in range(0, n//2):
        for j in range(0, n//2):
            ret[j][len(ret) - i -1] = board[i][j]
    for i in range(len(ret)):
        for j in range(len(ret)):
            board[i][j] = ret[i][j]


    ret = [[0] * (n // 2) for _ in range(n // 2)]
    for i in range(0, n // 2):
        for j in range(n//2 + 1, n):
            ret[j-(n//2 + 1)][len(ret) - i - 1] = board[i][j]
            
    for i in range(0, n // 2):
        for j in range(n // 2 + 1, n):
            board[i][j] = ret[i][j - (n//2 + 1)]


    ret = [[0] * (n // 2) for _ in range(n // 2)]
    for i in range(n//2 + 1, n):
        for j in range(0, n // 2):
            ret[j][len(ret) - (i -(n//2+1)) - 1] = board[i][j]

    for i in range(n // 2 + 1, n):
        for j in range(0, n // 2):
            board[i][j] = ret[i - (n//2 + 1)][j]

    ret = [[0] * (n // 2) for _ in range(n // 2)]
    for i in range(n//2 + 1, n):
        for j in range(n//2 + 1, n):
            ret[j-(n//2 + 1)][len(ret) - (i-(n//2 + 1)) - 1] = board[i][j]

    for i in range(n // 2 + 1, n):
        for j in range(n // 2 + 1, n):
            board[i][j] = ret[i - (n//2 + 1)][j - (n//2 + 1)]

for turn in range(4):
    groups = []
    groups_num = []
    find_group()
    count_point()
    rotate()
print(point)