# Align two strings with given match reward, mismatch penalty, and indel penalty by using 
# graph that calculates each index as the maximum score of calculating down, right, and cross  
# -----------------------------------------------------------------------
import sys

def max(int1, int2, int3):
    if int1 >= int2 and int1 >= int3:
        return int1
    if int2 >= int1 and int2 >= int3:
        return int2
    if int3 >= int1 and int3 >= int2:
        return int3

# find 
def BackTrack(v, w, match_reward, mismatch_penalty, indel_penalty):
    m = len(v)
    n = len(w)

    field = [[0 for a in range (n + 1)] for b in range(m + 1)]

    Backtrack = [[[0,0] for c in range (n + 1)] for d in range(m + 1)]

    field[0][0] = 0
    counter = indel_penalty
    for i in range(1, m + 1):
        field[i][0] = counter
        counter = counter + indel_penalty
    counter2 = indel_penalty
    for j in range(1, n + 1):
        field[0][j] = counter2
        counter2 = counter2 + indel_penalty

    counter3 = indel_penalty
    for k in range(1, m + 1):
        Backtrack[k][0][1] = counter3
        counter3 = counter3 + indel_penalty
    counter4 = indel_penalty
    for l in range(1, n + 1):
        Backtrack[0][l][1] = counter4
        counter4 = counter4 + indel_penalty

    for x in range(1, m + 1):
        for y in range(1, n + 1):
            score = 0
            if v[x-1] == w[y-1]:
                score = match_reward
            if v[x-1] != w[y-1]:
                score = mismatch_penalty
            field[x][y] = max(field[x-1][y] + indel_penalty,field[x][y-1] + indel_penalty, field[x-1][y-1] + score)
            #print("max: " + str(field[x][y]))
            if mismatch_penalty > indel_penalty:
                if field[x][y] == field[x-1][y-1] + mismatch_penalty:
                    Backtrack[x][y] = ["mismatch", field[x][y]]
                elif field[x][y] == field[x-1][y] + indel_penalty:
                    #print("----down")
                    Backtrack[x][y] = ["down",indel_penalty]
                elif field[x][y] == field[x][y-1] + indel_penalty:
                    Backtrack[x][y] = ["right", field[x][y]]
                    #print("----right")
                elif field[x][y] == field[x-1][y-1] + match_reward:
                    Backtrack[x][y] = ["cross", field[x][y]]
                    #print("----cross")
            else:
                if field[x][y] == field[x-1][y] + indel_penalty:
                    #print("----down")
                    Backtrack[x][y] = ["down",field[x][y]]
                elif field[x][y] == field[x][y-1] + indel_penalty:
                    Backtrack[x][y] = ["right",field[x][y]]
                    #print("----right")
                elif field[x][y] == field[x-1][y-1] + match_reward and v[x-1] == w[y-1]:
                    Backtrack[x][y] = ["cross", field[x][y]]
                    #print("----cross")
                elif field[x][y] == field[x-1][y-1] + -abs(mismatch_penalty) and v[x-1] != w[y-1]:
                    Backtrack[x][y] = ["mismatch", field[x][y]]
                    #print("----mismatch")

    return Backtrack

def OutPutLCS(backtrack, vstring, wstring, vlen, wlen, newstr1, newstr2):
    if vlen == 0 and wlen != 0:
        newstr1.append("-")
        newstr2.append(wstring[wlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen, wlen - 1, newstr1, newstr2)
    if wlen == 0 and vlen != 0:
        newstr2.append("-")
        newstr1.append(vstring[vlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen - 1, wlen, newstr1, newstr2)


    if vlen == 0 and wlen == 0:
        if backtrack[vlen][wlen][0] == "down":
            newstr2.append("-")
            newstr1.append(vstring[vlen-1])
        elif backtrack[vlen][wlen][0] == "right":
            newstr1.append("-")
            newstr2.append(wstring[wlen-1])

        n1 = ''.join(newstr1)
        n2 = ''.join(newstr2)
        return n1[::-1] + ' ' + n2[::-1]
    
    if backtrack[vlen][wlen][0] == "down":
        newstr2.append("-")
        newstr1.append(vstring[vlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen - 1, wlen, newstr1, newstr2) 
    elif backtrack[vlen][wlen][0] == "right":
        newstr1.append("-")
        newstr2.append(wstring[wlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen, wlen - 1, newstr1, newstr2)

    else:
        newstr1.append(vstring[vlen-1])
        newstr2.append(wstring[wlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen - 1, wlen - 1, newstr1, newstr2)

text_file = input()
input_name = '/Users/sanghyunlee/Desktop/' + text_file

with open(input_name) as f:
    lines = f.readlines()
info = lines[0].strip()
infos = info.split(' ')


match_reward = int(infos[0])
mismatch_penalty = -abs(int(infos[1]))
indel_penalty = -abs(int(infos[2]))

str1 = lines[1].strip()
str2 = lines[2].strip()
newstr1 = []
newstr2 = []
backtrack = BackTrack(str1, str2, match_reward, mismatch_penalty, indel_penalty)
limit = sys.getrecursionlimit()
sys.setrecursionlimit(5000)
score = (backtrack[len(str1)][len(str2)][1])
print(score)
result = (OutPutLCS(backtrack, str1, str2, len(str1), len(str2), newstr1, newstr2))
r = result.split(' ')
for i in r:
    print(i)
