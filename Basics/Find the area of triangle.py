## Given base(B) and height(H) of a triangle find its area.
## Input Size : N <= 1000000
## Sample Testcase :
## INPUT
## 2 4
## OUTPUT
## 4

n = list(map(int,input().split()))
a = n[0]
b = n[1]
area = 0.5*a*b
print(area)
