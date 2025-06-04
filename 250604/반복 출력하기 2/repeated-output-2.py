n = int(input())

# Please write your code here.
def retriever(n):
    if n == 0:
        return
    print("HelloWorld")
    retriever(n-1)

retriever(n)