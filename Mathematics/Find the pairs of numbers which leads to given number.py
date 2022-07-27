## You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.

## Note:Both numbers lie in range 1<=a,b<n

## Input Description:
## You are given a number ‘n’

## Output Description:
## Print the number of pairs satisfying above condition

## Sample Input : 
## 5
## Sample Output :
## 4

n = int(input())
a = 1
b = n - a
count = 0
while((1<=a) and (a<n)):
    count = count + 1
    a = a + 1
print(count)
