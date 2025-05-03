
arr = [list(map(int,input().split())) for _ in range(4)]
for row in arr:
    s = 0
    for x in row:
        s += x
    print(s)