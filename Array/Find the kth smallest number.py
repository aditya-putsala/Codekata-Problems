## Given 2 numbers N and K followed by N elements, find the Kth smallest element.If the element cannot be found then print -1
## Input Size : N <= 100000
## Sample Testcase :
## INPUT
## 5 2
## 1 1 2 4 5
## OUTPUT
## 2

n,k = list(map(int,input().split()))
s = list(map(int,input().split()))
s.sort()
se = set(s)
l = list(se)
a = len(l)
if (k-1 >= 0) and (k-1<=a):
    print(l[k-1])
else:
    print(-1)
