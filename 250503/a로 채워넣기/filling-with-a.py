str1 = input()
list1 = list(str1)
list1[1] = 'a'
list1[-2] = 'a'
str2="".join(list1)


print(str2)