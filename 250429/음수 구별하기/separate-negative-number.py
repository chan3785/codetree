N = int(input())

if (N > 100 or N < -100):
    print("out of range number!")

if (N < 0):
    print(N, "minus", sep="\n")
else:
    print(N)
