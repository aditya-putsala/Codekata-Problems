## You are given a number ‘n’. You have to tell whether a number is great or not. A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back

## m+j=n

## Input Description:
## You are given a number n;

## Output Description:
## Print Great if a number is great else print the no

## Sample Input :
## 59
## Sample Output :
## Great

n = int(input())
m = 0
j = 1
for i in str(n):
    m = m + int(i)
    j = j * int(i)
    
if n == m + j:
    print("Great")
else:
    print("no")
    
