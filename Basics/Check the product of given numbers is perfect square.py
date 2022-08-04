## Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
## Sample Testcase :
## INPUT
## 5 5
## OUTPUT
## yes


k = list(map(int,input().split()))
n = k[0]
m = k[1]
sum = 0
pro = n * m
for i in range(1,int(pro/2)):
    if pro/i == i:
        sum = sum + 1
    else:
        sum = sum 
if sum == 0:
    print("no")
else:
    print("yes")
