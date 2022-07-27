## Assume your brother studies in class 2. He has to  complete his homework on co-primes. As an elder sibling help him in finding whether the given two numbers is co-prime or not.

## Input Description:
## You will be given two numbers ‘n’ and ‘m’

## Output Description:
## Your task is to tell whether numbers is co prime or not. If it is a co-prime print 1 else 0

## Sample Input :
## 3 5
## Sample Output :
## 1

n = list(map(int,input().split()))
a = n[0]
b = n[1]
c = min(a,b)
d = max(a,b)
flag = 0
for i in range(2,c):
    if (a % i == 0) or ( b%i == 0):
        flag = flag +1
if d % c !=0:
    flag =0
if flag ==0:
    print("1")
else:
    print("0")
