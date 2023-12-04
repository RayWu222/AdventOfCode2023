
# import os
# print("Working dir:", os.getcwd())
balls = {"red":12, "green":13, "blue":14}
file = open("Day_2/part1/input.txt","r")
lines = file.readlines()

power = 0
res = 0
#each line
for line in lines:
    line = line.rstrip("\n")
    isPossible = True
    red = 0
    green = 0
    blue = 0
    id = 0
    #get game id
    game =  line.split(":")
    id = game[0][5::1]
    #subsets of game 
    subset = game[1].split(";")
    #print(subset[0])
    maxColorCubes = {"red": 0, "blue": 0, "green":0}
    #colors part
    for i in subset:
        
        shallowCopy =  balls.copy()
        colors = i.split(",")
        #each color
        for color in colors:
            #print(color)
            quantity = color.split(" ")
            #print("color : " + quantity[2] + " | quantity: " + quantity[1])
            #print(maxColorCubes[quantity[2]])
           
            maxColorCubes[quantity[2]] = max(maxColorCubes[quantity[2]], int(quantity[1]))
            shallowCopy[quantity[2]] -= int(quantity[1])

        
        #check dict to see if values lower than 0
        for key in shallowCopy:
            
            if shallowCopy[key] < 0:
                isPossible = False
                break
    if isPossible:
        res += int(id)

    #part 2
    tempPower = 1
    for key in maxColorCubes:
        tempPower *= maxColorCubes[key]
    #print(tempPower)
    power += tempPower
print(power)
#print(res)





    


