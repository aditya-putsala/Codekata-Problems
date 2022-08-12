## Given 2 numbers N,K followed by N elements print all the elements lesser than K in sorted order.If the elements could not be found print -1
## Input Size : N <= 100000
## Sample Testcase :
## INPUT
## 5 3
## 1 2 1 4 1
## OUTPUT
## 1 1 1 2

n,k = list(map(int,input().split()))
s = list(input().split())
s.sort()
l = []
for i in range(n):
    if int(s[i]) < k:
        l.append(s[i])
if len(l)>0:
    print(" ".join(map(str,l)))
else:
    print(-1)
