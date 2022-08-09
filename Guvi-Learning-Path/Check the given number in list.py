## Given 2 numbers N,K and an array of N integers, find if the element K exists in the array.
## Input Size : N <= 100000
## Sample Testcase :
## INPUT
## 5 2
## 1 2 3 4 5
## OUTPUT
## yes
## HINT: Read about Binary Search

n,k = list(map(int,input().split()))
l = list(map(int,input().split()))
if k in l:
    print("yes")
else:
    print("no")
