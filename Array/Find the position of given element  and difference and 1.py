## Given a number N,K followed by array of N elements where the difference between any adjacent elements is 1. Find the position of the given number K.If K not found in the array print -1
## Sample Testcase :
## INPUT
## 5 1
## 3 2 1 2 3
## OUTPUT
## 3

n,k = list(map(int,input().split()))
s = list(map(int,input().split()))
count = 0
for i in range(len(s)):
    if k == s[i]:
        count = i + 1
if count == 0:
    print(-1)
else:
    print(count)
