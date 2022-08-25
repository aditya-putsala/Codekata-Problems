## The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.For the given input string(S) and shift print the encrypted string.
## Sample Testcase :
## INPUT
## ABCdEFGHIJKLMNOPQRSTUVWXYz 23
## OUTPUT
## XYZaBCDEFGHIJKLMNOPQRSTUVw

l = list(input().split())
n = l[0]
k = l[1]
f = []
j = 0
flag = 0
for i in n:
    if ((ord(i)>64) and (ord(i)<91)):
        j = ord(i) + int(k)
        if j >90:
            flag = j - 90
            j = 65 + flag
        else:
            j = j
    elif ((ord(i)>96) and (ord(i)<123)):
        j = ord(i) + int(k)
        if j > 122:
            flag = j - 122
            j = 97 + flag
        else:
            j = j
    f.append(chr(j))
print("".join(f))
