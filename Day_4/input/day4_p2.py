# import os
# print("Working dir:", os.getcwd())
file = open("Day_4/input/part1.txt")
lines = []
total = 0
totalScratchCards = 0
#get line
for i, line in enumerate(file):
    innerList = []
    line = line.split(":",1)[1].strip().split("|")
    res = [int(ele) for ele in line[0].split()]
    ans = [int(ele) for ele in line[1].split()]
    innerList.append(res)
    innerList.append(ans)
    innerList.append(1)
    lines.append(innerList)

#print(lines)
totalCards = 0
for i, line in enumerate(lines):
    winningNumbers = 0

   
    for number in line[1]:       
        if number in line[0]:
            winningNumbers += 1
    #print("i: " + str(i) + " | " + str(winningNumbers))
    #times
    for j in range(line[2]):

        for k in range(i+1, i+1+winningNumbers):
            lines[k][2] +=1
    #print("i: " + str(i) + "| line[2]: " + str(line[2]))
    totalCards += line[2]
print(str(totalCards))
