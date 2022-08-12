## Given 2 numbers N,K print the array after deleting the last K elements.
## Input Size : N,K <= 100000
## Sample Testcase :
## INPUT
## 5 4
## 1 2 3 4 5
## OUTPUT
## 1

n,k = list(map(int,input().split()))
s = list(map(int,input().split()))
while (k > 0):
    s.pop()
    k = k -1
if len(s) !=0:
    print(" ".join(map(str,s)))
else:
    print(-1)
