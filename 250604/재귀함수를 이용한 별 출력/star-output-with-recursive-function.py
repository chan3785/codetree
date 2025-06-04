n = int(input())

# Please write your code here.
def retrieve(n):
    if n == 0:
        return
    
    retrieve(n-1)
    print("*" * n)

retrieve(n)