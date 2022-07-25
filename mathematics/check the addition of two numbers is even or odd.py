## Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
## Sample Testcase :
## INPUT
## 9 2
## OUTPUT
## odd

n = list(map(int,input().split()))
a = n[0]
b = n[1]
sum = a + b
if sum % 2 == 0:
    print("even")
else:
    print("odd")
