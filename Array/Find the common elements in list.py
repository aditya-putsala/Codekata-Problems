## Given a number N and 2 arrays A and B of sorted order of size N, print the common elements.If it is not found print -1.
## Input Size : 1 <= N <= 100000
## Sample Testcase :
## INPUT
## 5
## 1 1 1 1 1
## 1 2 3 4 5
## OUTPUT
## 1

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = []
for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            l.append(a[i])
if len(l) > 0:
    print(" ".join(map(str,l)))
else:
    print(-1)
