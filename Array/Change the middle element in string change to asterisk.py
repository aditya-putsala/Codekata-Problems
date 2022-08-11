## Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).
## Sample Testcase :
## INPUT
## hello
## OUTPUT
## he*lo

n = input()
l = []
for i in n:
    l.append(i)
k = len(l)
if k % 2 != 0:
    l[k//2] = "*"
else:
    l[k//2] = "*"
    l[(k//2)-1] = "*"
print("".join(l))
