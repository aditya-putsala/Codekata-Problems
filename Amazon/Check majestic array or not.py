## You are given given task is to print whether array is ‘majestic’ or not.A ‘majsetic’ array is an array whose sum of first three number is equal to last three number.

## Input Description:
## You are given a number ‘n’,Next line contains ‘n’ space separated

## Output Description:
## Print 1 if array is majestic and 0 if it is not

## Sample Input :
## 7
## 1 2 3 4 6 0 0
## Sample Output :
## 1

n = int(input())
k = list(map(int,input().split()))
sum1 = 0
sum2 = 0
for i in range(0,3):
    sum1 = sum1 + k[i]
for j in range(len(k)-3,len(k)):
    sum2 = sum2 + k[j]
if sum1 == sum2:
    print(1)
else:
    print(0)

