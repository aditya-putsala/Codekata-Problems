## You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.

## Input Description:
## First line contains a number ‘n’. Then next line contains n space separated numbers.

## Output Description:
## Print the difference of indices of largest and smallest array

## Sample Input :
## 5
## 1 6 4 0 3
## Sample Output :
## -2

n = int(input())
l = list(map(int,input().split()))
if n == len(l):
    pass
for i in range(len(l)):
    if l[i] == max(l):
        a = i
    if l[i] == min(l):
        b = i
print(a-b)
