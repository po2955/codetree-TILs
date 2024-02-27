from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

wind = []
for i in range(n):
    if board[i][0] == -1:
        wind.append(i)
wind_first = wind[0]
wind_second = wind[1]


def spread_dust():
    global board
    test_board = [[0] * m for _ in range(n)]
    test_board[wind[0]][0], test_board[wind[1]][0] = -1, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != -1:
                        cnt += 1
                        test_board[nx][ny] += board[i][j] // 5
                test_board[i][j] += board[i][j] - ((board[i][j] // 5) * cnt)
    board = test_board

def clean_wind():
    global board
    test_board = deepcopy(board)

    test_board[wind_first][1] = 0
    for i in range(2, m):
        test_board[wind_first][i] = board[wind_first][i-1]

    for i in range(wind_first-1, -1, -1):
        test_board[i][m-1] = board[i + 1][m-1]
    
    for i in range(m-2, -1, -1):
        test_board[0][i] = board[0][i+1]
    
    for i in range(1, wind_first):
        test_board[i][0] = board[i-1][0]
    
    test_board[wind_second][1] = 0
    for i in range(2, m):
        test_board[wind_second][i] = board[wind_second][i-1]

    for i in range(wind_second + 1, n):
        test_board[i][m-1] = board[i-1][m-1]

    for i in range(m-2, -1, -1):
        test_board[n-1][i] = board[n-1][i+1]
    
    for i in range(n-2, wind_second, -1):
        test_board[i][0] = board[i+1][0]

    board = test_board

    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print()
for turn in range(t):
    spread_dust()
    clean_wind()

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] > 0:
            answer += board[i][j]
print(answer)