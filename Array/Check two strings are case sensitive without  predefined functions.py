## Given 2 strings S1 and s2, check whether they are case senitively equal without using any predefined function(case sensitive).If they are not same print 'no'
## Sample Testcase :
## INPUT
## guvi guvi
## OUTPUT
## yes

a,b = list(input().split())
if a == b:
    print("yes")
else:
    print("no")
