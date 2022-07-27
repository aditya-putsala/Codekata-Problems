## You are given with a string which comprises of some numbers. Your task is to find the largest integer by converting the string to the corresponding integer.

## Input Description:
## First line contains n denoting number of Test Cases. The first and only Line of testcase has the string

## Output Description:
## Print the largest number

## Sample Input :
##  I was born on 12 october 1998.
## Sample Output :
## 1998

n = input()
n.strip()
n = n[:(len(n)-1)]
l = list(n.split())
a = []
for i in l:
    if i[len(i)-1]==".":
        b = i[:len(i)-1]
    else:
        b = i
    try:
        int(b)
        a.append(int(b))
    except:
        "ValueError"
a.sort()
print(a[len(a)-1])
