## Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
## Sample Testcase :
## INPUT
## 4 2
## 1 2 3 3
## OUTPUT
## yes

a = list(map(int,input().split()))
b = list(map(int,input().split()))
k = a[1]
n = a[0]
for i in b:
    if i == k:
        print("yes")
        break

else:
    print("no")
