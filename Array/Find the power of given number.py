## Given numbers A,B find A^B.
## Input Size : 1 <= A <= 5 <= B <= 50
## Sample Testcase :
## INPUT
## 3 4
## OUTPUT
## 81

n = list(map(int,input().split()))
a = n[0]
b = n[1]
if 1<=a<=5 and a<=b<=50:
    print(a**b)
else:
    print("no")
