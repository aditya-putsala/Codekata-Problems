## Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).
## Input Size : N <= 100000
## Sample Testcase :
## INPUT
## 5
## 1 2 3 4 5
## OUTPUT
## 1 5

n = int(input())
s = list(map(int,input().split()))
min_num = 0
max_num = 0
k = []
for i in range(len(s)):
    if max_num < s[i]:
        max_num = s[i]
for i in range(len(s)):
    if max_num == s[i]:
        k.append(i+1)
min_num = max_num
for i in range(len(s)):
    if min_num > s[i]:
        min_num = s[i]
for i in range(len(s)):
    if min_num == s[i]:
        k.append(i+1)
k.reverse()
print(" ".join(map(str,k)))
