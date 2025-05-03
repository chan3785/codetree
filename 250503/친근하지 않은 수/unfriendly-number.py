n = int(input())
s = 0
for i in range(n):
    if(i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
        continue
    s += 1

print(s)