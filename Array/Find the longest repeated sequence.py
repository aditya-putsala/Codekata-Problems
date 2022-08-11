## Given a number N and an array of N elements, find the length of the longest repeating sequence of the elements.If no such sequence is found print -1
## Input Size : N <= 100000
## Sample Testcase :
## INPUT
## 8
## 1 2 2 2 3 4 5 6
## OUTPUT
## 3

n = int(input())
k = list(map(int,input().split()))
count = 0
for i in range(n-1):
    if k[i] == k[i + 1]:
        count = count +1
if count==0:
    print(-1)
else:
    print(count+1)
