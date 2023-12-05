file = open("Day_3/input.txt")
lines = file.readlines()

row = len(lines)
col = len(lines[0])

ans  = 0
#check for symbol
def is_symbol(i,j):
    if not (0 <= i < row and 0 <= j <= col):
         return False
    return lines[i][j] != "." and not lines[i][j].isdigit()

for i, line in enumerate(lines):
     start = 0
     j = 0

     while j < col:
          
          start = j
          num = ""
          while j < col and line[j].isdigit():
               
               num += line[j]
               j+=1

          if num == "":
               j += 1
               continue
          num = int(num)


          #Got Number, look for symbol
          if is_symbol(i, start -1) or is_symbol(i, j):
               ans+=num
               continue
          
        
            
          