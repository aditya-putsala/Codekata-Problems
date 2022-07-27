## Sreelatha was confused with series. She is given with a number ‘n’. There is a pattern hidden the series. She has to understand and print  the series till nth number by looking into example.Sreelatha is confused and She hired you , you have to develop the series for sreelatha by observing the pattern from the below example.

## Input Description:
## She is given with a number ‘n’.

## Output Description:
## print  the series till nth number

## Sample Input :
## 3
## Sample Output :
## 1 9 36

n = int(input())
a = 1
b = 2
k = []
while n>0:
    k.append(a)
    a = a + b**3
    b = b + 1
    n = n -1
print(" ".join(map(str,k)))
