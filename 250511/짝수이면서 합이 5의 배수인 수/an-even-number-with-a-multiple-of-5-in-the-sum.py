n = str(input())

# Please write your code here.
tens = int(n[0])
ones = int(n[1])
n = int(n)
def five(a, b):
    if (n % 2 == 0) and (a + b) % 5 == 0:
        print ("Yes")
    else:
        print("No")

five(tens,ones)