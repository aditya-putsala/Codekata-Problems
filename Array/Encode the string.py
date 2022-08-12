## Given a string S, print the encoded string by adding 3 to each character(a maps to d,b maps to e,c maps to f and so on).
## Input Size : 1 <= N <= 100000
## Sample Testcase :
## INPUT
## RADAR
## OUTPUT
## UDGDU


n = input()
l = []
k = []
for i in n:
    l.append(i)
for i in l:
    if (ord(i)+3)<90:
        k.append(chr(ord(i)+3))
    else:
        d = (ord(i)+2) - 90
        k.append(chr(65+d))
print("".join(k))
