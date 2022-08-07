## Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.
## Input Size : A,B,C <= 100000
## Sample Testcase :
## INPUT
## 3 4 5
## OUTPUT
## yes

n = list(map(int,input().split()))
a,b,c = n[0],n[1],n[2]
s = (a+b+c)/2
d= (s*(s-a)*(s-b)*(s-c))**0.5
if d > 0:
    print("yes")
else:
    print("no")
