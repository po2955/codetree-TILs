dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n = int(input())
students = [[] * 5 for _ in range(n*n)]
board = [[0] * n for _ in range(n)]
for i in range(n * n):
    n0, n1, n2, n3, n4 = map(int, input().split())
    students[i] = [n0, n1, n2, n3, n4]

def move_student(student):
    test = []
    check = student[1:]
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue
            cnt_like = 0
            cnt_blank = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 0:
                        cnt_blank += 1
                    elif board[nx][ny] != 0 and board[nx][ny] in check:
                        cnt_like += 1
            test.append((cnt_like, cnt_blank, i, j))
    if not test:
        return
    test = sorted(test, key = lambda x : (-x[0], -x[1], x[2], x[3]))
    x, y = test[0][2], test[0][3]
    board[x][y] = student[0]

for turn in range(n*n):
    for i in range(len(students)):
        move_student(students[i])

point = 0
for i in range(n):
    for j in range(n):
        for k in range(len(students)):
            if board[i][j] == students[k][0]:
                check = students[k][1:]
                cnt = 0
                for q in range(4):
                    nx = i + dx[q]
                    ny = j + dy[q]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in check:
                        cnt += 1
                if cnt == 0:
                    continue
                elif cnt == 1:
                    point += 1
                elif cnt == 2:
                    point += 10
                elif cnt == 3:
                    point += 100
                elif cnt == 4:
                    point += 1000
print(point)