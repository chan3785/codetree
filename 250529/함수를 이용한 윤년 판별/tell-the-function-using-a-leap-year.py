y = int(input())

# Please write your code here.
def 윤년인가(n):
    if n % 100 == 0 and n % 400 != 0:
        return "false"
    elif n % 4 == 0:
        return "true"
    else:
        return "false"

print(윤년인가(y))