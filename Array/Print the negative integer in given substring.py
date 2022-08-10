## Assume you are a student studying in school.You are given a task to find first negative integer for each and every window of size k.

## Input Description:
## First line contains an integer n denoting the size of the array. The next line contains n space separated integers forming the array. The last line contains the window size k.

## Output Description:
## Print the first negative integer in that window.If all the numbers are positive print 0

## Sample Input :
## 7
## 1 -2 -3 -4 5 6 -7
## 3
## Sample Output :
## -2 -2 -3 -4 -7

n = int(input())
s = list(map(int,input().split()))
k = int(input())
l = []
for i in range(n-k+1):
    if (s[i] < 0):
        l.append(s[i])
    elif (s[i+1] < 0):
        l.append(s[i+1])
    elif (s[i+2] < 0):
        l.append(s[i+2])
    else:
        l.append(0)
print(" ".join(map(str,l)))
