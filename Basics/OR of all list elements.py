## Given a number N and an array of N elements, find the Bitwise OR of the array elements.
## Input Size : N <= 100000
## Sample Testcase :
## INPUT
## 2
## 2 4
## OUTPUT
## 6

n = int(input())
s = list(map(int,input().split()))
sum = s[0]
if n == len(s):
    for i in range(1,n):
        sum = sum|s[i]
print(sum)
