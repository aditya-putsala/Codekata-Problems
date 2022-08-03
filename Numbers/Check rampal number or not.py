## Rampal is a number in which the sum of last two digits of that number is multiple of 4.Your teacher has given you the task to make a list of rampal numbers.Your task is to tell whether the number is rampal or not.

## Note : if the number is negative than rampal is a number which has sum of first and last digit as multiple of 4  

## Input Description:
## First line contains an input n

## Output Description:
## Print yes or no

## Sample Input :
## 20

## Sample Output :
## no

n = int(input())
a = 0
b = 0
if n > 0:
    a = n % 10
    n = n // 10
    b = n % 10
elif n < 0:
    k = str(n)
    a = int(k[1])
    b = int(k[-1])
if (a + b) % 4 == 0:
    print("yes")
else:
    print("no")
