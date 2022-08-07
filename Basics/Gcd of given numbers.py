## Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1
## Sample Testcase :
## INPUT
## 10 5
## OUTPUT
## 5

s = list(map(int,input().split()))
m = s[0]
n = s[1]
k = max(m,n)
l = min(m,n)
x = 2
res = 1
if (k == 0 or l ==0):
    res = res * (-1)
elif k % l == 0:
    res = res * l
else:
    while(x<=k):
        if (k % x == 0) and (l % x == 0):
            res = res * x
        else:
            x = x + 1
print(res)
