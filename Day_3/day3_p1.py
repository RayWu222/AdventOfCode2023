file = open("Day_3/input.txt")
lines = file.readlines()


row = len(lines)
col = len(lines[0].rstrip("\n"))

ans  = 0
#check for symbol
def is_symbol(i,j):
    #condition to check if it out of range 
    if not (0 <= i < row and 0 <= j < col):
         return False
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
          if is_symbol(i, start -1) or is_symbol(i, j):
               ans+=num
               continue
          
          for k in range(start - 1, j + 1):
               #check previous and next line for symbol
               if is_symbol(i - 1, k) or is_symbol(i+1, k):
                    ans  += num
                    break
print(ans)
            
          