arr = [0 for x in range(10)]
arr[0], arr[1] = map(int, input().split())

for i in range(2, 10):
    arr[i] = arr[i-1] + arr[i-2]

for x in arr:
    print(x%10, end=" ")
