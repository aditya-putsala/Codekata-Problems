## you are given with ‘arasu’ series(shown in example).You have to understand it and you will be given a number ‘n’ ,you have to print the series till n numbers.

## Input Description:
## You are given a number n;

## Output Description:
## Print series till nth number

## Sample Input :
## 4
## Sample Output :
## 2 5 10 17

n = int(input())
l = []
for i in range(0,n):
    d = (i/2)*(2*3 + (i -1)*2)
    k = 2 + d
    l.append(int(k))    
print(" ".join(map(str,l)))
