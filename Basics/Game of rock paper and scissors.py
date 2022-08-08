## Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.
## Sample Testcase :
## INPUT
## R P
## OUTPUT
## P

a,b = list(input().split())
l = ["P","R","S"]
flag = 0
if a in l:
    flag = flag + 1
if b in l:
    flag = flag + 1
if flag == 2:
    if (a == "P" and b == "R") or (b == "P" and a == "R"):
        print("P")
    if (a == "P" and b == "S") or (b == "P" and a == "S"):
        print("S")
    if (a == "R" and b == "S") or (b == "R" and a == "S"):
        print("R")
    if a == b:
        print("D")
