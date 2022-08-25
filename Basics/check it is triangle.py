## Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.
## Input Size : A,B,C <= 100000
## Sample Testcase :
## INPUT
## 3 4 5
## OUTPUT
## yes

n = list(map(int,input().split()))
a = n[0]
b = n[1]
c = n[2]

if a!=b!=c!=a:
    print("yes")
else:
    print("no")
