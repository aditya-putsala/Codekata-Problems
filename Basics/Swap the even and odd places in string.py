## Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
## Input Size : |s| <= 10000000(complexity O(n))
## Sample Testcase :
## INPUT
## codekata
## OUTPUT
## ocedakat

n = input()
e = []
o = []
st = ""
for i in range(len(n)):
    if i % 2 == 0:
        e.append(n[i])
    else:
        o.append(n[i])
for i in range(len(e) or len(o)):
    st = st + o[i] + e[i]
print(st)
    
