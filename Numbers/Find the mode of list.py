## You are given an array of digits. Your task is to print the digit with maximum frequency.

## Input Description:
## You are given length of array ’n’,next line contains n space separated numbers.

## Output Description:
## Print the number with maximum frequency. If two number have equal freqency prin the number that comes first

## Sample Input :
## 7
## 1 2 3 4 4 4 5
## Sample Output :
## 4

l = int(input())
n = list(map(int,input().split()))
k = []
max = n[0]
for i in range(len(n)):
    if n.count(n[0])<n.count(n[i]):
        max = n[i]
if l == len(n):
    print(max)
