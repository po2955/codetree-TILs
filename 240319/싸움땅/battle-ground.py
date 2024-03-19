dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m, k = map(int, input().split())
board_gun = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    gun = list(map(int, input().split()))
    for j in range(n):
        board_gun[i][j].append(gun[j])
board_player = [[[] for _ in range(n)]for _ in range(n)]
answer = [0]
for _ in range(m):
    answer.append(0)

for i in range(1, m+1):
    x, y, d, s = map(int, input().split())
    x -= 1
    y -= 1
    board_player[x][y].append([i,d,s,0])

def fight_player(x, y):
    player_2 = board_player[x][y].pop()
    player_1 = board_player[x][y].pop()
    power_1 = player_1[2] + player_1[3]
    power_2 = player_2[2] + player_2[3]
    if power_1 == power_2:
        power_1 = player_1[2]
        power_2 = player_2[2]
    point = abs((player_1[2] + player_1[3]) - (player_2[2] + player_2[3]))
    
    if power_1 > power_2:
        board_player[x][y].append(player_1)
        answer[player_1[0]] += point
        loser_gun = player_2[3]
        player_2[3] = 0
        board_gun[x][y].append(loser_gun)
        d = player_2[1]
        for i in range(4):
            nx = x + dx[(d + i + 4) % 4]
            ny = y + dy[(d + i + 4) % 4]
            if 0 <= nx < n and 0 <= ny < n and not board_player[nx][ny]:
                player_2[1] = (d + i + 4) % 4
                board_player[nx][ny].append(player_2)
                if board_gun[nx][ny]:
                    board_gun[nx][ny].sort()
                    new_gun = board_gun[nx][ny].pop()
                    board_player[nx][ny][0][3] = new_gun
                break
        board_gun[x][y].sort()
        if board_player[x][y][0][3] < board_gun[x][y][-1]:
            place = board_player[x][y][0].pop()
            new_gun = board_gun[x][y].pop()
            board_player[x][y][0].append(new_gun)
            board_gun[x][y].append(place)

    elif power_1 < power_2:
        board_player[x][y].append(player_2)
        answer[player_2[0]] += point
        loser_gun = player_1[3]
        player_1[3] = 0 
        board_gun[x][y].append(loser_gun)
        d = player_1[1]
        for i in range(4):
            nx = x + dx[(d + i + 4) % 4]
            ny = y + dy[(d + i + 4) % 4]
            if 0 <= nx < n and 0 <= ny < n and not board_player[nx][ny]:
                player_1[1] = (d + i + 4) % 4
                board_player[nx][ny].append(player_1)
                if board_gun[nx][ny]:
                    board_gun[nx][ny].sort()
                    new_gun = board_gun[nx][ny].pop()
                    board_player[nx][ny][0][3] = new_gun
                break
        board_gun[x][y].sort()
        if board_player[x][y][0][3] < board_gun[x][y][-1]:
            place = board_player[x][y][0].pop()
            new_gun = board_gun[x][y].pop()
            board_player[x][y][0].append(new_gun)
            board_gun[x][y].append(place)

def move_player(num):
    for i in range(n):
        for j in range(n):
            if board_player[i][j]:
                if board_player[i][j][0][0] == num:
                    d = board_player[i][j][0][1]
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and not board_player[nx][ny]:
                        if board_gun[nx][ny]:
                            board_gun[nx][ny].sort()
                            if board_player[i][j][0][3] < board_gun[nx][ny][-1]:
                                place = board_player[i][j][0].pop()
                                new_gun = board_gun[nx][ny].pop()
                                board_player[i][j][0].append(new_gun)
                                board_gun[nx][ny].append(place)
                        player = board_player[i][j].pop()
                        board_player[nx][ny].append(player)

                    elif 0 <= nx < n and 0 <= ny < n and board_player[nx][ny]:
                        player = board_player[i][j].pop()
                        board_player[nx][ny].append(player)
                        fight_player(nx, ny)

                    elif 0 > nx or nx >= n or 0 > ny or ny >= n:
                        nx = i + dx[(d + 2 + 4) % 4]
                        ny = j + dy[(d + 2 + 4) % 4]

                        if 0 <= nx < n and 0 <= ny < n and not board_player[nx][ny]:
                            if board_gun[nx][ny]:
                                board_gun[nx][ny].sort()
                                if board_player[i][j][0][3] < board_gun[nx][ny][-1]:
                                    place = board_player[i][j][0].pop()
                                    new_gun = board_gun[nx][ny].pop()
                                    board_player[i][j][0].append(new_gun)
                                    board_gun[nx][ny].append(place)
                            player = board_player[i][j].pop()
                            player[1] = (d + 2 + 4) % 4
                            board_player[nx][ny].append(player)

                        elif 0 <= nx < n and 0 <= ny < n and board_player[nx][ny]:
                            player = board_player[i][j].pop()
                            player[1] = (d + 2 + 4) % 4
                            board_player[nx][ny].append(player)
                            fight_player(nx, ny)
                    return

for turn in range(k):
    for i in range(1, m+1):
        move_player(i)
        # if turn == 0:
        #     for x in board_player:
        #         print(x ,end = ' ')
        #         print()
        #     print()
for x in range(1, len(answer)):
    print(answer[x], end = ' ')