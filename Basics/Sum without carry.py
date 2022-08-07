## Write a code to get 2 integers as input and add the integers without any carry.

## Input Description:
## A single line containing 2 integers.

## Output Description:
## Print sum of the 2 integers without carry

## Sample Input :
## 44 66
## Sample Output :
## 0

ini = list(map(int,input().split()))
m = ini[0]
n = ini[1]
tot = 0
mul = 1
bit_sum = 0
while (n or m):
    bit_sum = (n % 10) + (m % 10)
    bit_sum = bit_sum % 10
    tot = bit_sum * mul + tot
    mul = mul * 10
    n = n // 10
    m = m // 10
print(tot)
