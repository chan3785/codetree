a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    if n < 1: 
        return
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_even(n):
    s = str(n)
    total = 0
    for i in s:
        total += int(i)
    if(total % 2 == 0):
        return True
    else:
        return False

cnt = 0
for i in range(a, b+1):
    if(is_prime(i) and is_even(i)):
        cnt += 1

print(cnt)