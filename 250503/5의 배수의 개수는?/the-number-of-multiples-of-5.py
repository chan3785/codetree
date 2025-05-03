matrix = [list(map(int,input().split())) for _ in range(4)]

cnt = 0
for row in matrix:
    for x in row:
        if (x % 5 == 0):
            cnt += 1

print(cnt)