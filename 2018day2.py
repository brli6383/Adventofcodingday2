
import sys                  #when doing stdin (standard input)  
                            #when using cmd line 
ids = list()



# reads in from redirected standard input
for line in sys.stdin:              #stdin helps read initial characters in input.txt
    ids.append (line.strip())       #strip clears out whitespace

twos = 0
threes = 0


for id in ids:
    lineDict = dict()
    for char in id:
        if char in lineDict:
            lineDict[char] += 1
        else:
            lineDict[char] = 1

    if 3 in lineDict.values():
        threes += 1
    if 2 in lineDict.values():
        twos += 1

print(twos * threes)

ans = ""

# ids = ids[0][2:]



for i in range(len(ids)):                # loops through whole list
    for j in range(i, len(ids)):         # before i gets to 1, j has to iterate through all of it
        for k in range(len(ids[i])):     #K itterates through letters
            if ids[i][k] == ids[j][k]:
                ans += ids [i][k]       #adds unique characters to answer
        if len(ids[i]) -1 == len(ans):  #if they arent equal, they are different and does not add to answer
            print (ans)                 #once we compare all letters of ID checking (we look for difference of 1 length)
            break
        else:
            ans = ""                    #el fin

print(ans)


# [Bob, Cathy, Rob, Tom]
#---0----1------2----3--
# for i in range (4)
# for j in range (i, 4)


