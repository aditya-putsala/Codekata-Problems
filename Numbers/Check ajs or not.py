## You are given a number ‘n’.Your task is to develop an algorithm to tell whether the number is ‘ajs’ or not.An ‘ajs’ number is a number whose sum of first two digits is present in given number ‘n’

## Input Description:
## A number ’n’ is given to you

## Output Description:
## Print 1 if number is ajs or 0 if it is not

## Sample Input :
## 9817
## Sample Output :
## 1

a = input()
sum = 0
for i in range(0,2):
    sum = sum + int(a[i])
k = str(sum)
if k in a:
    print(1)
else:
    print(0)
