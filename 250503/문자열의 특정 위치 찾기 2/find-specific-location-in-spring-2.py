char = input()

list1 = ['apple', 'banana', 'grape', 'blueberry', 'orange']
cnt = 0
for word in list1:
    if (word[2] == char or word[3] == char):
        print(word)
        cnt += 1
print(cnt)