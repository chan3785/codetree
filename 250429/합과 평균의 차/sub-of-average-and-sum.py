a,b,c = map(int, input().split())

s = a+b+c
A = int(s/3)
t = s - A

print(s, A, t, sep="\n")