## Given an array of N elements switch(swap) the element with the adjacent element and print the output.
## Sample Testcase :
## INPUT
## 5
## 3 2 1 2 3
## OUTPUT
## 2 3 2 1 3

n = int(input())
s = list(map(int,input().split()))
a = 0 
for i in range(n):
    if i % 2== 0:
        a = s[i]
        if (i+1) < n:
            s[i] = s[i+1]
            s[i+1] = a
            continue
print(" ".join(map(str,s)))
