file = open("input.txt", "r")
lines = file.readlines()
count = 0
total = 0 
for line in lines:
    # char_line = line.encode('utf-8')
    charArray = [*line]
    length =  len(charArray)
    left = 0
    right = 0
    for i in range(0, length):
        if ord(charArray[i]) >= 48 and ord(charArray[i]) <= 57:
            left = int(line[i]) * 10
            
            break
    for i in range(length-1, -1, -1):
       
        if ord(charArray[i]) >= 48 and ord(charArray[i]) <= 57:
            right = int(line[i])
            break
    
    total += left + right

print(total)
        

