# import os
# print("Working dir:", os.getcwd())
file = open("input\Day_1\input.txt", "r")
lines = file.readlines()
count = 0
total = 0 
numbers =  {"one": 1, "two":2, "three": 3, "four": 4, "five": 5, "six":6, "seven": 7, "eight":8, "nine":9, "ten":10}


def checkString(word):
    for i in range(len(word)):
        tempWord = ""
        for j in range(i, len(word)):
            tempWord += word[j]
            if tempWord in numbers:
                return numbers[tempWord]
    return 0

for line in lines:
    # char_line = line.encode('utf-8')
    charArray = [*line]
    length =  len(charArray)
    left = 0
    right = 0
    leftWord = ""
    rightWord = ""
    for i in range(0, length):
        if(not charArray[i].isnumeric()):
            leftWord += charArray[i]
  
            left = checkString(leftWord)
            # print("i: " + str(i) + " word: " + leftWord)
            if(left != 0):
                break
        elif ord(charArray[i]) >= 48 and ord(charArray[i]) <= 57:
            left = int(line[i]) 
            break
    for i in range(length-1, -1, -1):   
        if(not charArray[i].isnumeric()):
            rightWord = charArray[i] + rightWord
         
            right = checkString(rightWord)
            if(right!= 0):
                break
        elif ord(charArray[i]) >= 48 and ord(charArray[i]) <= 57:
            right = int(line[i])
            break

    print("left: " + str(left) + " | right: " + str(right))
    # print((left * 10) + right)
    total += (left*10) + right
    
file.close()
print(total)


