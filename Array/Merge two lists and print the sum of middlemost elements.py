## You are given two arrays of equal length. Your task is to merge the two arrays then sort them too and then find the sum of two middlemost elements.

## Input Description:
## You are given a number ‘n’. Then Next line contains first list of 'n' separated numbers.Third line contains second list of 'n' space separated numbers.

## Output Description:
## Print the sum of two middle elements

## Sample Input :
## 5
## 1 9 16 25 46
## 2 3 4 5 6
## Sample Output :
## 11

n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l1.extend(l2)
l1.sort()
sum1 = l1[n] + l1[n-1]
print(sum1)
