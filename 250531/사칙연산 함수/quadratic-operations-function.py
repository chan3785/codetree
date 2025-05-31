a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def 사칙연산(a, o, c):
    if (o == '+'):
        return print(f'{a} {o} {c} = {a+c}')
    elif (o == '-'):
        return print(f'{a} {o} {c} = {a-c}')
    elif (o == '/'):
        return print(f'{a} {o} {c} = {a//c}')
    elif (o == '*'):
        return print(f'{a} {o} {c} = {a*c}')
    else:
        return print('False')

사칙연산(a,o,c)