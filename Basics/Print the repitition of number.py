## Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
## Sample Testcase :
## INPUT
## 6 2
## 1 2 3 5 7 8
## OUTPUT
## 0

a = list(map(int,input().split()))
n = a[0]
k = a[1]
sum = -1
b = list(map(int,input().split()))
for i in b:
    if i == k:
        sum = sum + 1
if sum == -1:
    print(-1)
else:
    print(sum)
