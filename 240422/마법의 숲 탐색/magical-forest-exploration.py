dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
R, C, K = map(int, input().split())
board = [[0] * C for _ in range(R+2)]
board_robot = [[0] * C for _ in range(R+2)]
answer = 0

def drop(i, j, d, t):
    if i == R + 1:
        i -= 1
        board[i][j] = t
        board_robot[i][j] = 1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            board[nx][ny] = t
            if nx == i + dx[d] and ny == j + dy[d]:
                board[nx][ny] = -t
        return
    while 1:
        if board[i+1][j] == 0 and board[i][j+1] == 0 and board[i][j-1] == 0:
            if i + 1 == R + 1:
                # i -= 1
                board[i][j] = t
                board_robot[i][j] = 1
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    board[nx][ny] = t
                    if nx == i + dx[d] and ny == j + dy[d]:
                        board[nx][ny] = -t
                return
        else:
            if 0 <= j-2 and board[i-1][j-2] == 0 and board[i-2][j-1] == 0 and board[i][j-1] == 0 and board[i+1][j-1] == 0 and board[i][j-2] == 0:
                d = (d - 1 + 4) % 4
                i += 1
                j -= 1
                drop(i, j, d, t)
                return
            elif j+2 < C and board[i][j+1] == 0 and board[i-1][j+2] == 0 and board[i-2][j+1] == 0 and board[i+1][j+1] == 0 and board[i][j+2] == 0:
                d = (d + 1 + 4) % 4
                i += 1
                j += 1
                drop(i, j, d, t)
                return
            else:
                i -= 1
                board[i][j] = t
                board_robot[i][j] = 1
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    board[nx][ny] = t
                    if nx == i + dx[d] and ny == j + dy[d]:
                        board[nx][ny] = - t
                return
        i += 1

def check_out():
    for i in range(2):
        for j in range(C):
            if board[i][j] > 0:
                return True
    return False

def clear():
    global board
    board = [[0] * C for _ in range(R+2)]

def count_point():
    global answer, check, visited
    check = []
    for i in range(R+2):
        for j in range(C):
            if board_robot[i][j] == 1:
                visited[i][j] = 1
                board_robot[i][j] = 0
                check.append(i)
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if board[nx][ny] < 0 and visited[nx][ny] == 0:
                        for q in range(4):
                            nnx = nx + dx[q]
                            nny = ny + dy[q]
                            if 0 <= nnx < R+2 and 0 <= nny < C and board[i][j] != board[nnx][nny] and board[nnx][nny] != 0 and visited[nnx][nny] == 0:
                                for p in range(4):
                                    nnnx = nnx + dx[p]
                                    nnny = nny + dy[p]
                                    if 0 <= nnnx < R+2 and 0 <= nny < C and abs(board[nnx][nny]) == abs(board[nnnx][nnny]) and visited[nnnx][nnny] == 0:
                                        board_robot[nnnx][nnny] = 1
                                        count_point()
                                        return
                            if 0 <= nnx < R+2 and 0 <= nny < C:
                                visited[nnx][nny] = 1
                    visited[nx][ny] = 1
for turn in range(1, K + 1):
    j, d = map(int, input().split())
    drop(2, j-1, d, turn)
    visited = [[0] * C for _ in range(R + 2)]
    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print()
    if check_out() == True:
        clear()
        continue
    check = []
    count_point()
    if check:
        answer += max(check)
    # print(answer)

print(answer)