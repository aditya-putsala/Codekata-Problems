## Given a number N, find the nearest greater multiple of 10.
## Input Size : N <= 10000
## Sample Testcase :
## INPUT
## 3
## OUTPUT
## 10

n = int(input())
k = n//10
l = n%10
if n<10:
    print(10)
elif l<6:
    print((k)*10)
else:
    print((k+1)*10)
