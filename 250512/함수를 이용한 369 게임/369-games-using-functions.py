a, b = map(int, input().split())

# Please write your code here.
def judge(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if (is_in369(i) or is_3mul(i)):
            cnt += 1
    print(cnt)


def is_in369(n):
    n = str(n)
    return "3" in n or "6" in n or "9" in n

def is_3mul(n):
    return n % 3 == 0

judge(a, b)