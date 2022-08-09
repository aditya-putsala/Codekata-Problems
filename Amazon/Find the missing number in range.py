## You are given a number n,ranging from 1 to n. Out of which one number is missing. Your task is to print that missing number.

## Input Description:
## You are given a number ‘n’.

## Output Description:
## Print the missing number.

## Sample Input :
## 5
## 1 3 5 2
## Sample Output :
## 4

n = int(input())
k = list(map(int,input().split()))
k.sort()
l = []
g = []
for i in range(1,n+1):
    l.append(i)
for j in range(len(l)):
    if l[j] not in k:
        g.append(l[j])
print("".join(map(str,g)))
