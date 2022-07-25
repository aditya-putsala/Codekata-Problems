## Given length L and breadth B of a farm, print the area of the farm upto 5 decimal decimals.
## Sample Testcase :
## INPUT
## 1.626 2.31
## OUTPUT
## 3.75606

l,b = list(map(float,input().split()))
area = l*b
a = f'{area:.6f}'
print(round(float(a),5))
