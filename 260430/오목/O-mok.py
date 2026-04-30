board = [list(map(int, input().split())) for _ in range(19)]
flag = False
#오른쪽
for i in range(19):
    cnt_b, cnt_w = 0, 0
    for j in range(19):
        if board[i][j] == 0:
            cnt_b = 0
            cnt_w = 0
        if board[i][j] == 1:
            cnt_b += 1
            cnt_w = 0
        if board[i][j] == 2:
            cnt_b = 0
            cnt_w += 1
        if cnt_b == 5:
            print(1)
            exit(print(i+1, j-1))
        if cnt_w == 5:
            print(2)
            exit(print(i+1, j-1))
#아래
for i in range(19):
    cnt_b, cnt_w = 0, 0
    for j in range(19):
        if board[j][i] == 0:
            cnt_b = 0
            cnt_w = 0
        if board[j][i] == 1:
            cnt_b += 1
            cnt_w = 0
        if board[j][i] == 2:
            cnt_b = 0
            cnt_w += 1
        if cnt_b == 5:
            print(1)
            exit(print(j-1, i+1))
        if cnt_w == 5:
            print(2)
            exit(print(j-1, i+1))

# 대각선 오른쪽
for i in range(19):
    cnt_b, cnt_w = 0, 0
    for j in range(19):
        x, y = i + j, j
        if x >= 19 or y >= 19:
            continue
        if board[y][x] == 0:
            cnt_b = 0
            cnt_w = 0
        if board[y][x] == 1:
            cnt_b += 1
            cnt_w = 0
        if board[y][x] == 2:
            cnt_b = 0
            cnt_w += 1
        if cnt_b == 5:
            print(1)
            exit(print(x-1, y-1))
        if cnt_w == 5:
            print(2)
            exit(print(x-1, y-1))
for i in range(19):
    cnt_b, cnt_w = 0, 0
    for j in range(19):
        x, y = i + j, j
        if x >= 19 or y >= 19:
            continue
        if board[x][y] == 0:
            cnt_b = 0
            cnt_w = 0
        if board[x][y] == 1:
            cnt_b += 1
            cnt_w = 0
        if board[x][y] == 2:
            cnt_b = 0
            cnt_w += 1
        if cnt_b == 5:
            print(1)
            exit(print(x-1, y-1))
        if cnt_w == 5:
            print(2)
            exit(print(x-1, y-1))

#대각선 왼쪽
for i in range(19):
    cnt_b, cnt_w = 0, 0
    for j in range(19):
        x, y = i-j , j
        if x >= 19 or y >= 19 or x<0 or y<0:
            continue
        if board[y][x] == 0:
            cnt_b = 0
            cnt_w = 0
        if board[y][x] == 1:
            cnt_b += 1
            cnt_w = 0
        if board[y][x] == 2:
            cnt_b = 0
            cnt_w += 1
        if cnt_b == 5:
            print(1)
            exit(print(y-1, x+3))
        if cnt_w == 5:
            print(2)
            exit(print(y-1, x+3))
for i in range(19):
    cnt_b, cnt_w = 0, 0
    for j in range(19):
        x, y = i-j , j
        if x >= 19 or y >= 19:
            continue
        if board[x][y] == 0:
            cnt_b = 0
            cnt_w = 0
        if board[x][y] == 1:
            cnt_b += 1
            cnt_w = 0
        if board[x][y] == 2:
            cnt_b = 0
            cnt_w += 1
        if cnt_b == 5:
            print(1)
            exit(print(y+3, x-1))
        if cnt_w == 5:
            print(2)
            exit(print(y+3, x-1))
if not flag:
    print(0)