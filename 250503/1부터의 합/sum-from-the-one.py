n = int(input())
s = 0
for i in range(100):
    s += i
    if (s >= n):
        print(i)
        break
        