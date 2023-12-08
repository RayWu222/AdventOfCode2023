file = open("Day_3/input.txt")
lines = file.readlines()


row = len(lines)
col = len(lines[0].rstrip("\n"))

ans  = 0

#create 2d array 
goods = [[[] for _ in range(col)] for _ in range(row)]
print(goods)

#check for symbol
def is_symbol(i,j, num):
    #condition to check if it out of range 
    if not (0 <= i < row and 0 <= j < col):
         return False
    
    if lines[i][j] == "*":
        goods[i][j].append(num)
    return lines[i][j] != "." and not lines[i][j].isdigit()

for i, line in enumerate(lines):
     start = 0
     j = 0
     #iterate thru the column 
     while j < col:
          
          start = j
          num = ""
          #check for digit
          while j < col and line[j].isdigit():
               
               num += line[j]
               j += 1
          
          if num == "":
               j += 1
               continue
          num = int(num)
          #Got Number, look for symbol
          #i = line number
          #start is index at current line
          #check before and after for symbol
          is_symbol(i, start -1, num) or is_symbol(i, j, num)
               
          for k in range(start - 1, j + 1):
               #check previous and next line for symbol
            is_symbol(i - 1, k, num) or is_symbol(i+1, k, num)


for i in range(row):
     for j in range(col):
          nums = goods[i][j]
          if lines[i][j] == "*" and len(nums)==2:
               ans += nums[0] * nums[1]
print(ans)
            
          