## Given 2 numbers N and K print the number after performing bitwise right shift 'K' times(upto 2 decimal places).
## Input Size : 1 <= N, K <= 1000
## Sample Testcase :
## INPUT
## 5 2
## OUTPUT
## 1

n,k = list(map(int,input().split()))
l = n>>k
print(l)
