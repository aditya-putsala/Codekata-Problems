## You are given a set of numbers, out of which you have to tell which of them are finest. A finest number ‘n’ is a number which is formed by a number ‘t’ such that

## n=t^3+(t+1)^3

 

## t is a natural number

## Input Description:
## You are given a number ‘z’ representing total numbers in an array, Next line contains z space separated numbers.

## Output Description:
## Print the numbers which are finest in ascending order if there are no such numbers print -1.

## Sample Input :
## 2
## 1729 189
## Sample Output :
## 189 1729

n = int(input())
k = list(map(int,input().split()))
l = []
def finest(a):
    b = int(round(a**(1/3)))
    for i in range(1,b+1):
        if (a == (i**3) + ((i+1)**3)):
            return True
    else:
        return False
if n == len(k):
    for i in k:
        if finest(i):
            l.append(i)
if len(l)>0:
    l.sort()
    print(" ".join(map(str,l)))
else:
    print("-1")
