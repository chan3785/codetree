n, m = map(int, input().split())

# Please write your code here.

def gcd(n,m):
    while n!=0:
        if (n > m):
            n,m = m,n
        m %= n
        if m == 0:
            return n

def lcm(n,m):
    return (n * m) // gcd(n,m)

    
print(lcm(12,18))
        