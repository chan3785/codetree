n = str(input())

# Please write your code here.
tens = int(n[0])
ones = int(n[1])

def five(a, b):
    if(a + b) % 5 == 0:
        print ("Yes")
    else:
        print("No")

five(tens,ones)