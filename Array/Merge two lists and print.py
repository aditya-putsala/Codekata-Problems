## Given 2 array of size N and M.merge them in sorted order and print it.
## Input Size : |N||M| <= 100000( O(n))
## Sample Testcase :
## INPUT
## 5 4
## 1 2 3 4 5
## 1 2 3 4
## OUTPUT
## 1 1 2 2 3 3 4 4 5

n = input().split()
a = input().split()
b = input().split()
a.extend(b)
a.sort()
print(" ".join(a))
