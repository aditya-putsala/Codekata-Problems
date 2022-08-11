## Given a number N and an array of N integers, find the sum of all the negative numbers in the array.
## Input Size : N <= 100000
## Sample Testcase :
## INPUT
## 2
## 3 0
## OUTPUT
## 0

n = int(input())
k = list(map(int,input().split()))
sum1 = 0
for i in k:
    if i < 0:
        sum1 = sum1 + i
if sum1 == 0 :
    print(0)
else:
    print(sum1)
