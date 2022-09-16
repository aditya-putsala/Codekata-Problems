## Joseph was going through topic of strings. He learnt about anagrams. But due to some circumstances he forget ,now he hired you to help him in completing the work.Your task is to tell whether the two given strings are anagrams

## Input Description:
## The first line of the input is a string N, the second line of the input is a string M

## Output Description:
## Compare the two string input N and M. Print 1 if they are anagram else print 0.

## Sample Input :
## abcd
## cdab
## Sample Output :
## 1

n = input()
m = input()
l = []
k = []
flag = True
for i in n:
    l.append(i)
for i in m:
    k.append(i)
l.sort()
k.sort()
flag = True
for i in range(len(l)):
    if(l[i]==k[i]):
        flag = True
    else:
        flag = False
if flag:
    print(1)
else:
    print(0)

a
a
a
