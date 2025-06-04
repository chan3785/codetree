n = int(input())

# Please write your code here.
def retriever1(n):
    if n == 0:
        return
    
    retriever1(n-1)
    print(n, end=" ")

def retriever2(n):
    if n == 0:
        return
    
    print(n, end=" ")
    retriever2(n-1)

retriever1(n)
print()
retriever2(n)