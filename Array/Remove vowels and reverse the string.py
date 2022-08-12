## Given a string S, print the reverse of the string after removing the vowels.If the resulting string is empty print '-1'.
## Input Size : 1 <= N <= 100000
## Sample Testcase :
## INPUT
## codekata
## OUTPUT
## tkdc

n = input()
k = ["a","A","e","E","i","I","o","O","u","U"]
b = []
l = []
for i in n:
    l.append(i)
for i in l:
    if i not in k:
        b.append(i)
a = "".join(b)
if len(a)!=0:
    print(a[len(a)-1::-1])
else:
    print(-1)
