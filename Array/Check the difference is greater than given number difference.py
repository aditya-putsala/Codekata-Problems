## You are given with an circular array .Your task is calculate the difference between two consecutive number. And if difference is greater than ‘k’, print 1 else print 0

## Input Description:
## You are given two numbers ‘n’, ’m’. Next line contains n space separated integers.

## Output Description:
## Print 1 if the difference is greater than ‘m’.

## Sample Input :
## 5 15
## 50 65 85 98 35
## Sample Output :
## 0 1 0 1 0

nk = list(map(int,input().split()))
arr = list(map(int,input().split()))
a = []
dif = nk[1]
if nk[0] != len(arr):
    print("Error")
for i in range(len(arr)):
    if i == len(arr)-1:
        sum = arr[i] - arr[0]
    else:
        sum = arr[i+1] - arr[i]
    if sum < 0:
        sum = sum * (-1)
    if dif < sum:
        a.append("1")
    else:
        a.append("0")
print(' '.join(a))
    
