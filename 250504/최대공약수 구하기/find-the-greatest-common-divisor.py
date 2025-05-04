n, m = map(int, input().split())

# Please write your code here.
def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)
    
print(gcd(n,m))