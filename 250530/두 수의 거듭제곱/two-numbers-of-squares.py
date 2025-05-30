a, b = map(int, input().split())

# Please write your code here.
def mul(a, b):
    mul = a
    for i in range(b-1):
        a *= mul
    return a

print(mul(a,b))