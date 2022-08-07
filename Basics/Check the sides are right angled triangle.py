## Given 3 numbers A,B,C print 'yes' if they can form the sides of a right angled triangle,otherwise 'no'.
## Input Size : A,B,C <= 100000
## Sample Testcase :
## INPUT
## 3 4 5
## OUTPUT
## yes

s = list(map(int,input().split()))
max_num = 0
for i in range(len(s)):
    if (max_num < s[i]):
        max_num = s[i]
a = s[0]
b = s[1]
c = s[2]
if (2*(max_num **2) == a**2 + b**2 + c**2):
        print("yes")
else:
    print("no")
