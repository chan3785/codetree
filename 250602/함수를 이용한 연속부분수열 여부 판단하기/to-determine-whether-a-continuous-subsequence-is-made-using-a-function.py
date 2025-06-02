n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def is_연속부분수열():
    hashB = hash(str(b))
    for i in range(n1 - n2 + 1):
        substr = []
        for j in range(i, n2 + i):
            substr.append(a[j])
        hashA = hash(str(substr))
        if (hashA == hashB):
            return "Yes"
    return "No"

print(is_연속부분수열())