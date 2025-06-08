n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for x in arr:
    if x % 2 == 0:
        print(x//2, end=" ")
    else:
        print(x, end=" ")