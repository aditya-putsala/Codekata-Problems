## You are given a ‘true’ string. String is called true if weight of string is multiple of 8. Your task is to tell whether a string can be declared True or Not. Weight of string is the sum of ASCII value of Vowel character(s) present in the string.

## Input Description:
## You are given as string ‘s’ in lower cases

## Output Description:
## Print 1 for true and 0 for false

## Sample Input :
## raja
## Sample Output :
## 0

k = ["a","e","i","o","u","A","E","I","O","U"]
b = input()
l = []
for i in range(len(b)):
    if b[i] in k:
        l.append(b[i])
res = 0
for i in l:
    res = res + ord(i)
if res % 8 == 0:
    print(1)
else:
    print(0)
