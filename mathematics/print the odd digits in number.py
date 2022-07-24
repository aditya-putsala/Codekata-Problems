## Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
## Input Size : N <= 100000
## Sample Testcase :
## INPUT
## 2143
## OUTPUT
## 1 3

n = input()
l = len(n)
n = int(n)
k = []
while(l > 0):
    a = n % 10
    if a % 2 != 0:
      k.append(a)
    n = n // 10
    l = l - 1
if len(k)>0:
    k.reverse()
    print(" ".join(map(str,k)))
else:
    print(-1)
