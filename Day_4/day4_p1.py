import os
print("Working dir:", os.getcwd())
file = open("Day_4/input/part1.txt")
lines = []
total = 0

#get line
for i, line in enumerate(file):
    innerList = []
    line = line.split(":",1)[1].strip().split("|")
    res = [int(ele) for ele in line[0].split()]
    ans = [int(ele) for ele in line[1].split()]
    innerList.append(res)
    innerList.append(ans)
    lines.append(innerList)
    
#print(lines)

for line in lines:
    count = 0
    for number in line[1]:       
        if number in line[0]:
      
            if count == 0:
                count += 1
            else:
                count *= 2
    total += count

print(str(total))
