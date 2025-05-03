n = int(input())

# Please write your code here.

matrix = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        cnt += 1
        matrix[i][j] = cnt
        if cnt >= 9:
            cnt = 0

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()