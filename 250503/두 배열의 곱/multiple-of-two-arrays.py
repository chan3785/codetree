arr1 = [list(map(int,input().split())) for _ in range(3)]
none = input().split()
arr2 = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(f'{arr1[i][j] * arr2[i][j]}', end=" ")
    print()