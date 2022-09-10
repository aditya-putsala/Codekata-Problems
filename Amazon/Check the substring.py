## Given 2 strings S1 and S2. Find if String2 is substring of String1. If it is print the index of the first occurrence. else print -1.
## Input Size : 1<= N <= 100000
## Sample Testcases :
## 1)INPUT
## test123string
## 123
## OUTPUT
## 4

n1 = input()
n2 = input()
count = 0
if n2 in n1:
    for i in range(len(n1)):
        if n1[i] == n2[0]:
            count = i
            break
if count == 0:
    print(-1)
else:
    print(count)
a
a
a
