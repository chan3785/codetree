list1 = [int(input()) for x in range(10)]

cnt3 = 0
cnt5 = 0

for x in list1:
    if (x % 3 == 0):
        cnt3 += 1
    if (x % 5 == 0):
        cnt5 += 1

print(f'{cnt3} {cnt5}')