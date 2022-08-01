## Write a program to get a list of integers as input and find the LCM of the values without using GCD

## Input Description:
## First line contains an integer N, number of values. Second line contains N space separated values.

## Output Description:
## Print the LCM of the values.

## Sample Input :
## 1 2 3 4 5
## Sample Output :
## 60

max_num = 0;
k = int(input())
s = list(map(int,input().split()))
n = len(s)
for i in range(n):
    if (max_num < s[i]):
        max_num = s[i];
res = 1;
x = 2;
while (x <= max_num):
    indexes = [];
    for j in range(n):
        if (s[j] % x == 0):
            indexes.append(j);
    if (len(indexes) >= 2):
        for j in range(len(indexes)):
            s[indexes[j]] = int(s[indexes[j]] / x);
        res = res * x;
    else:
        x += 1;
for i in range(n):
    res = res * s[i];
print(res);
