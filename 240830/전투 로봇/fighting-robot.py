from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n = int(input())
board= [[[0] for _ in range(n)]for _ in range(n)]
time = 0
robot_level = 2
catch_cnt = 0
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        if board[i][j][0] == 0:
            board[i][j].pop()
        board[i][j].append(a[j])

def is_Finished():
    global robot_level
    for i in range(n):
        for j in range(n):
            if board[i][j][-1] == 9:
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                Q = deque()
                Q.append((i, j))
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny][-1] <= robot_level and visited[nx][ny] == 0:
                            if 0 < board[nx][ny][-1] < robot_level:
                                return False
                            Q.append((nx, ny))
                            visited[nx][ny] = 1
    return True

def move_robot():
    global time, robot_level, catch_cnt
    for i in range(n):
        for j in range(n):
            if board[i][j][-1] == 9:
                visited = [[-1] * n for _ in range(n)]
                visited[i][j] = 0
                Q = deque()
                Q.append((i,j))
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny][-1] <= robot_level and visited[nx][ny] == -1:
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            Q.append((nx, ny))
                            if 0 < board[nx][ny][-1] < robot_level:
                                catch_cnt += 1
                                board[i][j][-1] = 0
                                board[nx][ny][-1] = 9
                                time += visited[nx][ny]
                                return
                return


while 1:
    if is_Finished() == True:
        print(time)
        break
    move_robot()
    if catch_cnt == robot_level:
        robot_level += 1
        catch_cnt = 0