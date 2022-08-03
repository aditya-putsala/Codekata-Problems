## You are provided with a number ’n’. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits.

## Input Description:
## You are given with a number n.

## Output Description:
## Print Saturated if it is saturated else it is Unsaturated

## Sample Input :
## 121
## Sample Output :
## Saturated

n = input()
a = []
for i in n:
    if i in n:
        if i not in a:
            a.append(i)
if len(a)==2:
    print("Saturated")
else:
    print("Unsaturated")
