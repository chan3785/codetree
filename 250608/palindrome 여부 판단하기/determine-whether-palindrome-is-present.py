A = input()
l = len(A)
# Please write your code here.



def 대칭(i):
    if (i == l):
        return print("Yes")
    if A[i] == A[l - i - 1]:
        대칭(i+1)
    else:
        return print("No")
        
        
대칭(0)
