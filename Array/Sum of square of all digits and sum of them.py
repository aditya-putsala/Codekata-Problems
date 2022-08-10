## Given a number N, print the sum of squares of all its digits.
## Input Size : 1 <= N <= 100000
## Sample Testcase :
## INPUT
## 12
## OUTPUT
## 5

n = input()
sum = 0
for i in n:
    sum = sum + (int(i)**2)
print(sum)
