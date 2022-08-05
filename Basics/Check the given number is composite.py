## Given a number N, print 'yes' if it is composite else print 'no'.
## Sample Testcase :
## INPUT
## 123
## OUTPUT
## yes

n = int(input())
sum = 0
for i in range(2,int(n/2)):
    if n % i == 0:
        sum = sum + 1
    else:
        sum = sum
if sum == 0:
    print("no")
else:
    print("yes")
