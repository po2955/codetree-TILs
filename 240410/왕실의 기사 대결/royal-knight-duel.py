from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

L, N, Q = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(L)]
knight = [[0] * L for _ in range(L)]
first_HP = []
now_HP = []
flag = 0
for i in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    for q in range(r, r + h):
        for p in range(c, c + w):
            knight[q-1][p-1] = i
    first_HP.append(k)
    now_HP.append(k)
order = []
for turn in range(1, Q + 1):
    i, d = map(int, input().split())
    order.append((i, d))

def bfs():
    visited = [[0] * L for _ in range(L)]
    Q = deque()
    for i in range(L):
        for j in range(L):
            if knight[i][j] > 0 and visited[i][j] == 0:
                xy = [(i,j)]
                num.append(knight[i][j])
                visited[i][j] = 1
                Q.append((i, j))
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < L and 0 <= ny < L and visited[nx][ny] == 0 and knight[nx][ny] == knight[i][j]:
                            xy.append((nx ,ny))
                            visited[nx][ny] = 1
                            Q.append((nx, ny))
                check.append(xy)

def move_knight(kn, d):
    global check, num, move, move_num, flag, knight
    a = [kn]
    next_xy = []
    xy_num = []
    while a:
        now = a.pop()
        Q = deque()
        visited = [[0] * L for _ in range(L)]
        xy = []
        xxyy = []
        xy_num.append(now)
        for i in range(L):
            for j in range(L):
                if knight[i][j] == now and visited[i][j] == 0:
                    xy.append((i, j))
                    visited[i][j] = 1
                    Q.append((i, j))
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < L and 0 <= ny < L and knight[nx][ny] == now and visited[nx][ny] == 0:
                                xy.append((nx, ny))
                                visited[nx][ny] = 1
                                Q.append((nx, ny))
                    for q in range(len(xy)):
                        x, y = xy[q][0] + dx[d], xy[q][1] + dy[d]
                        if x < 0 or x >= L or y < 0 or y >= L:
                            flag = 1
                            return
                        elif 0 <= x < L and 0 <= y < L:
                            if chess[x][y] == 2:
                                flag = 1
                                return
                            else:
                                xxyy.append((x, y))
                                if knight[x][y] > 0 and knight[x][y] != now:
                                    if knight[x][y] not in a:
                                        a.append(knight[x][y])
                    next_xy.append(xxyy)
    test = [[0] * L for _ in range(L)]
    if not next_xy:
        flag = 1
        return
    for i in range(len(xy_num)):
        for k in range(len(next_xy[i])):
            x, y = next_xy[i][k][0], next_xy[i][k][1]
            test[x][y] = xy_num[i]
    for i in range(len(xy_num)):
        for j in range(len(num)):
            if xy_num[i] == num[j]:
                num[j] = 0
                break
    for i in range(len(num)):
        if num[i] > 0:
            for k in range(len(check[i])):
                x, y = check[i][k][0], check[i][k][1]
                test[x][y] = num[i]
    num = xy_num
    knight = test
def damage(i):
    global now_HP
    #num은 명령에 의해 밀려난 기사의 리스트다.
    num.remove(i)
    num.sort()
    for x in num:
        for i in range(L):
            for j in range(L):
                if knight[i][j] == x and chess[i][j] == 1 and now_HP[x-1] >= 0:
                    now_HP[x-1] -= 1
    for i in range(len(now_HP)):
        if now_HP[i] <= 0:
            now_HP[i] = 0
            for n in range(L):
                for m in range(L):
                    if knight[n][m] == i + 1:
                        knight[n][m] = 0


for turn in range(1, Q + 1):
    num = []
    check = []
    move = []
    move_num = []
    bfs()
    i, d = order[turn-1][0], order[turn-1][1]
    move_knight(i, d)
    if flag == 1:
        flag = 0
        continue
    damage(i)

answer = 0
for i in range(len(first_HP)):
    if now_HP[i] > 0:
        answer += first_HP[i] - now_HP[i]
print(answer)