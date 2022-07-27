## Given a number N, find its next immediate greater power of 2(i.e 2^1, 2^2, 2^3...).
## Input Size : N <= 1000
## Sample Testcase :
## INPUT
## 4
## OUTPUT
## 8

n = int(input())
k = 0
while n>(2**k):
    k = k +1
print(2**(k+1))
