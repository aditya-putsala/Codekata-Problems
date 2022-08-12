## Given a string S, print 2 strings such that first string containing all characters in odd position(s) and other containing all characters in even position(s).
## Sample Testcase :
## INPUT
## XCODE
## OUTPUT
## XOE CD

n = input()
l = []
k = []
for i in range(len(n)):
    if i % 2 == 0:
        l.append(n[i])
    else:
        k.append(n[i])
a = "".join(l)
b = "".join(k)
print(a+" " +b)
