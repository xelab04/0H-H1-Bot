array = []
file_dest = "input.txt"

with open(file_dest,"r") as file:
    lines = file.readlines()
    for line in lines:
        array.append((line.strip("\n")).split(","))

for row in array:
    print(row)

print("")
grid_size = len(array)

def output(array):
    for row in array:
        print(row)

def is_colour(x,y,dx1,dx2,dy1,dy2,grid):
    try:
        if grid[y][x] == "0":
            sq_one = grid[y+dy1][x+dx1]
            sq_two = grid[y+dy2][x+dx2]
            if (sq_one == sq_two) and sq_one != "0":
                return True,sq_one
            else:       return False,None
        else:       return False,None
        
    except IndexError:      return False,None

def not_really(colour):
    if colour == "R":
        return "B"
    elif colour == "B":
        return "R"
    else:
        print(f"Invalid Colour {colour} Passed Into Function")

def compare(line_one,line_two):
    length = len(line_one)
    stupid_list = []
    for i in range(length):
        if line_one[i] != line_two[i] and line_one[i] != "0":
            return False,None
        else:
            if line_one[i] == "0":
                stupid_list.append((i,line_two[i]))
    return True,stupid_list

def thing(direction):
    var = False
    colour = None

    if direction == "x":
        a,b,c,d = 1,-1,1,2
        e,f,g,h = 0,0,0,0

    else:
        a,b,c,d = 0,0,0,0
        e,f,g,h = 1,-1,1,2
    
    if var == False:
        try:    var,colour = is_colour(x,y,a,b,e,f,array)
        except:     pass

    if var == False:
        try:    var,colour = is_colour(x,y,c,d,g,h,array)
        except:     pass
        
    if var == False:
        try:    var,colour = is_colour(x,y,-c,-d,-g,-h,array)
        except:     pass

    return var,colour

change = True
while change == True:
    change = False

    #ROWS
    for y in range(grid_size):
        line = array[y]
        
        for x in range(grid_size):

            #START FIRST RULE
            var,colour = thing("x")

            if var == True:
                change = True
                array[y][x] = (not_really(colour))
            #END FIRST RULE


            #START SECOND RULE
            if line.count("0") > 0 and array[y][x] == "0":# and change == False:
                
                r_count = line.count("R")
                b_count = line.count("B")
                
                if r_count == grid_size/2:
                    array[y][x] = (not_really("R"))
                    change = True
                if b_count == grid_size/2:
                    array[y][x] = (not_really("B"))
                    change = True
            #END SECOND RULE

                    
            #START THIRD RULE
            if line.count("0") == 2:# and change == False:
                for line_2 in array:
                    if line_2.count("0") == 0:
                        same_list, stupid_list = compare(line,line_2)
                        if same_list == True:
                            array[y][stupid_list[0][0]] = not_really(stupid_list[0][1])#inversing colour
            #END THIRD RULE
                            
        #END ROWS

    #COLUMNS
    for x in range(grid_size):
        temp_list = []
        
        for y in range(grid_size):
            temp_list.append(array[y][x])
            
        for y in range(grid_size):
            var,colour = thing("y")
                    
            if var == True:
                change = True
                array[y][x] = (not_really(colour))

            if temp_list.count("0") > 0 and array[y][x] == "0" and change == False:
                
                r_count = temp_list.count("R")
                b_count = temp_list.count("B")
                
                if r_count == grid_size/2:
                    array[y][x] = (not_really("R"))
                    change = True
                if b_count == grid_size/2:
                    array[y][x] = (not_really("B"))
                    change = True

            if temp_list.count("0") == 2 and change == False:

                for nx in range(grid_size):
                    new_temp_list = []
                    
                    for ny in range(grid_size):
                        new_temp_list.append(array[ny][nx])
                    if new_temp_list.count("0") == 0:
                        same_list, stupid_list = compare(temp_list,new_temp_list)
                        if same_list == True:
                            array[stupid_list[0][0]][x] = not_really(stupid_list[0][1])#inversing colour
                            #changing array values
            

output(array)
with open("output.txt","w") as file:
    for line in array:
        text = ""
        for i in range(grid_size):
            if i > 0:
                text = text + "," + line[i]
            else:
                text = line[i]
        file.writelines(text + "\n")
