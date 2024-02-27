dx = [-1, 1, 0 , 0]
dy = [0, 0, 1, -1]
n, m, k = map(int, input().split())
board = [[[] for _ in range(m)] for _ in range(n)]
board_d = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y, s, d, b = map(int, input().split())
    #속도, 방향, 크기
    board[x-1][y-1].append([s, d-1, b])
answer = 0
# for x in board:
#     print(x, end = ' ')
#     print()
def move_mold():
    global board
    test_board = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                s = board[i][j][0][0]
                d = board[i][j][0][1]
                b = board[i][j][0][2]
                nx = i
                ny = j
                for k in range(s):
                    nx += dx[d]
                    if nx < 0 or nx >= n:
                        if d == 0:
                            d = 1
                            nx += dx[d] * 2
                        elif d == 1:
                            d = 0
                            nx += dx[d] * 2
                    ny += dy[d]
                    if ny < 0 or ny >= m:
                        if d == 2:
                            d = 3
                            ny += dy[d] * 2
                        elif d == 3:
                            d = 2
                            ny += dy[d] * 2
                test_board[nx][ny].append([s,d,b])
    for i in range(n):
        for j in range(m):
            if test_board[i][j]:
                test_board[i][j].sort(key = lambda x : (-x[2]))
                a = test_board[i][j][0]
                test_board[i][j].clear()
                test_board[i][j].append(a)
    board = test_board

for j in range(m):
    signal = 0
    for i in range(n):
        if board[i][j]:
            answer += board[i][j][0][2]
            board[i][j].clear()
            move_mold()
            signal = 1
        if signal == 1:
            break
print(answer)