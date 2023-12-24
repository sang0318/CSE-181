import sys

def max(int1, int2, int3):
    if int1 >= int2 and int1 >= int3:
        if int1 > 0:
            return int1
    elif int2 >= int1 and int2 >= int3:
        if int2 > 0:
            return int2
    elif int3 >= int1 and int3 >= int2:
        if int3 > 0:
            return int3
    
    return 0


def BackTrack(v, w, match_reward, mismatch_pen, indel_penalty): #pam here
    m = len(v)
    n = len(w)

    field = [[0 for a in range (n + 1)] for b in range(m + 1)]

    Backtrack = [[0 for c in range (n + 1)] for d in range(m + 1)]

    field[0][0] = 0
    
    """ when using PAM 
    for x in range(1, m + 1):
        row_save = 0
        for letters in range(0, len(pam[0])):
                if v[x-1] == pam[0][letters]:
                    row_save = letters
        for y in range(1, n + 1):
            col_save = 0
            score = 0
            for letter in range(0, len(pam[0])):
                if w[y-1] == pam[0][letter]:
                    col_save = letter
            for row in range(1, len(pam)):
                for col in range(1, len(pam[row])):
                    if row_save == row and col_save == col:
                        score = int(pam[row+1][col+1])
    """ 
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            score = 0
            if v[x-1] == w[y-1]:
                score = match_reward
            if v[x-1] != w[y-1]:
                score = mismatch_penalty
            field[x][y] = max(field[x-1][y] + indel_penalty, field[x][y-1] + indel_penalty, field[x-1][y-1] + score)

            if field[x][y] == 0:
                Backtrack[x][y] = 0
            
            elif field[x][y] == field[x-1][y] + indel_penalty:
                #print("----down")
                Backtrack[x][y] = "down"
            elif field[x][y] == field[x][y-1] + indel_penalty:
                Backtrack[x][y] = "right"
                #print("----right")
            elif field[x][y] == field[x-1][y-1] + score and v[x-1] == w[y-1]:
                Backtrack[x][y] = "cross"
                #print("----cross")
            elif field[x][y] == field[x-1][y-1] + score and v[x-1] != w[y-1]:
                Backtrack[x][y] = "mismatch"
                #print("----mismatch")
        
            
    return Backtrack, field

def OutPutLCS(backtrack, vstring, wstring, vlen, wlen, newstr1, newstr2):
    if vlen == 0 and wlen != 0:
        if backtrack[vlen][wlen] == 0:
            n1 = ''.join(newstr1)
            n2 = ''.join(newstr2)
            return n1[::-1] + ' ' + n2[::-1]
        newstr1.append("-")
        newstr2.append(wstring[wlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen, wlen - 1, newstr1, newstr2)
    if wlen == 0 and vlen != 0:
        if backtrack[vlen][wlen] == 0:
            n1 = ''.join(newstr1)
            n2 = ''.join(newstr2)
            return n1[::-1] + ' ' + n2[::-1]
        newstr2.append("-")
        newstr1.append(vstring[vlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen - 1, wlen, newstr1, newstr2)


    if vlen == 0 and wlen == 0:
        if backtrack[vlen][wlen] == 0:
            n1 = ''.join(newstr1)
            n2 = ''.join(newstr2)
            return n1[::-1] + ' ' + n2[::-1]
        elif backtrack[vlen][wlen] == "down":
            newstr2.append("-")
            newstr1.append(vstring[vlen-1])
        elif backtrack[vlen][wlen] == "right":
            newstr1.append("-")
            newstr2.append(wstring[wlen-1])

        n1 = ''.join(newstr1)
        n2 = ''.join(newstr2)
        return n1[::-1] + ' ' + n2[::-1]
    
    if backtrack[vlen][wlen] == "down":
        newstr2.append("-")
        newstr1.append(vstring[vlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen - 1, wlen, newstr1, newstr2) 
    elif backtrack[vlen][wlen] == "right":
        newstr1.append("-")
        newstr2.append(wstring[wlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen, wlen - 1, newstr1, newstr2)
    elif backtrack[vlen][wlen] == 0 and vlen == len(vstring) and wlen == len(wstring):
        if backtrack[vlen-1][wlen] > backtrack[vlen][wlen-1]:
            return OutPutLCS(backtrack, vstring, wstring, vlen - 1, wlen, newstr1, newstr2)

        if backtrack[vlen-1][wlen] < backtrack[vlen][wlen-1]:
            return OutPutLCS(backtrack, vstring, wstring, vlen, wlen - 1, newstr1, newstr2)

    else:
        if backtrack[vlen][wlen] == 0:
            n1 = ''.join(newstr1)
            n2 = ''.join(newstr2)
            return n1[::-1] + ' ' + n2[::-1]
        newstr1.append(vstring[vlen-1])
        newstr2.append(wstring[wlen-1])
        return OutPutLCS(backtrack, vstring, wstring, vlen - 1, wlen - 1, newstr1, newstr2)


""" USING PAM
text_file = input()
input_name = '/Users/sanghyunlee/Desktop/' + text_file
pam=[]
with open(input_name) as f:
    lines = f.readlines()

for i in range(0, len(lines)):
    info = lines[i].strip()
    infos = info.split(' ')
    infos = [x for x in infos if x != '']
    pam.append(infos)

f.close()
"""

text_file = input()
input_name = '/Users/sanghyunlee/Desktop/' + text_file

with open(input_name) as f:
    lines = f.readlines()
info = lines[0].strip()
infos = info.split(' ')

str1 = lines[1].strip()
str2 = lines[2].strip()

match_reward = int(infos[0])
mismatch_penalty = -abs(int(infos[1]))
indel_penalty = -abs(int(infos[2]))
#indel_penalty = -abs(5)

track,field = BackTrack(str1,str2,match_reward, mismatch_penalty, indel_penalty) #put pam
newstr1 = []
newstr2 = []
result = (OutPutLCS(track, str1, str2, len(str1), len(str2), newstr1, newstr2))
r = result.split(' ')
for j in field:
    print(j)
print(field[len(str1)][len(str2)])

for i in r:
    print(i)
