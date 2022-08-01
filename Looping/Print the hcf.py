## Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

## Input Description:
## A single line containing 2 integers separated by space.

## Output Description:
## Print the HCF of the integers.

## Sample Input :
## 2 3
## Sample Output :
## 1

n = list(map(int,input().split()))
a = n[0]
b = n[1]
if a > b:
    a % b == 0
    print(b)
elif b > a:
    b % a == 0
    print(a)
