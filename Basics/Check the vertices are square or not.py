## Check whether the given 4 points form a square or not.
## Example:
## INPUT
## 10 10
## 10 20
## 20 20
## 20 10
## OUTPUT
## yes

a1,b1 = list(map(int,input().split()))
a2,b2 = list(map(int,input().split()))
a3,b3 = list(map(int,input().split()))
a4,b4 = list(map(int,input().split()))
s1 = ((a2-a1)**2 + (b2-b1)**2)**(0.5)
s2 = ((a3-a2)**2 + (b3-b2)**2)**(0.5)
s3 = ((a4-a3)**2 + (b4-b3)**2)**(0.5)
s4 = ((a1-a4)**2 + (b1-b4)**2)**(0.5)
s5 = ((a1-a3)**2 + (b1-b3)**2)**(0.5)
s6 = ((a2-a4)**2 + (b2-b4)**2)**(0.5)
l = [s1,s2,s3,s4,s5,s6]
l.sort()
flag = 0
if ((l[0]==l[1])and(l[1]==l[2])and(l[2] == l[3])) and (l[3] ==l[4]*(2**(0.5))):
    flag = flag + 1

if flag == 1:
    print("yes")
else:
    print("no")
