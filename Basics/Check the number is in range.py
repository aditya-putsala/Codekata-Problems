## Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
## Sample Testcase :
## INPUT
## 3
## 2 6
## OUTPUT
## yes

n = int(input())
lr = list(map(int,input().split()))
l = lr[0]
r = lr[1]
if l < n and n < r:
    print("yes")
else:
    print("no")
    
