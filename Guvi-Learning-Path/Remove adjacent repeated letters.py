## You are given a string s.Your task is to remove all the adjacent duplicate character from string.Print the string formed out of it.

## Input Description:
## You are given a string ‘s’

## Output Description:
## Print the resultant string

## Sample Input :
## Geeksforgeek
## Sample Output :
## Gksforgk

n = input()
l = []
for i in range(len(n)-1):
    if (n[i] != n[i+1]) and (n[i-1] !=n[i]):
        l.append(n[i])
if n[-2] != n[-1]:
    l.append(n[-1])
print("".join(l))
