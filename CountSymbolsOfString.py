# --conding:utf-8--
import os

os.system("cls")
print("Input a string")
strLine = input()
print("Input a symbol")
nLen = len(strLine)
for i in range(nLen):
    c = 0
    chSym1 = strLine[i]
    for j in range(nLen):
        chSym2 = strLine[j]
        if (chSym1 == chSym2):
            c += 1
    print(f"The symbol {chSym1} occurs {c} times")
