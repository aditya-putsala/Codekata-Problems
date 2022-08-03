## Ramesh is given a special series to print,as he has some other work to do.Help ramesh in printing the series.

## Note:Observe the series very keenly in examples

## Input Description:
## You are given a number ‘n’.

## Output Description:
## Print the n term of series.

## Sample Input :
## 6
## Sample Output :
## 1 6 120

n = int(input())
l = []
a = 1
res = 1
l.append(1)
l.append(n)
while(a<n):
    res = res * a
    a = a + 1
if res < 3:
    l[1] = l[1] * res
else:
    l.append(res)
print(" ".join(map(str,l)))
