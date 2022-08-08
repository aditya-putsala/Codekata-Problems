## Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
## Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
## Sample Testcase :
## INPUT
## 2 5
## OUTPUT
## 3

l,r = list(map(int,input().split()))
def isprime(n):
    flag = 0
    for i in range(2,n):
        if n% i == 0:
            flag  = flag + 1
    if flag == 0:
        return n
final = []
for j in range(l,r+1):
    if isprime(j):
        final.append(j)
print(len(final))
