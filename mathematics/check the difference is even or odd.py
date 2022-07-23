## Given 2 numbers N,M. Find their difference and check whether it is even or odd.
## Sample Testcase :
## INPUT
## 5 5
## OUTPUT
## even

n,m = input().split()
k = int(n)-int(m)
if k%2 == 0:
    print("even")
else:
    print("odd")
