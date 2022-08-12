## Given an array of N elements which follows either even number or odd number series.There may exists at maximum 1 even number in the odd series or 1 odd number in the even series.Find the different number if exists otherwise print '-1'?
## Input Size : |N| <= 100000
## Sample Testcase :
## INPUT
## 5
## 1 3 4 5 7
## OUTPUT
## 4

n = int(input())
k = list(map(int,input().split()))
e = []
o = []
for i in range(n):
    if k[i] % 2 == 0:
        e.append(k[i])
    else:
        o.append(k[i])
if ((len(e) == 1) or (len(o) == 1)):
    if (len(e) + len(o) == len(k)):
        if len(e) == 1:
            print("".join(map(str,e)))
        else:
            print("".join(map(str,o)))
else:
    print(-1)
