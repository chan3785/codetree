n = int(input())

# Please write your code here.
def totalsum(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s // 10

print(totalsum(n))

