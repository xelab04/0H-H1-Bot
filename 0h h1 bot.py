array = []
file_dest = <INSERT GRID TEXT FILE HERE>

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
    #x,y = (x,y)
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
    #print(colour)
    if colour == "R":
        return "B"
    elif colour == "B":
        return "R"
    else:
        print(f"Invalid Colour {colour} Passed Into Function")

change = True
while change == True:
    change = False

    #ROWS
    for y in range(grid_size):
        line = array[y]
        
        for x in range(grid_size):
            square_colour = line[x]
            if x == 0:
                var,colour = is_colour(x,y,1,2,0,0,array)
            elif x == grid_size-1:
                var,colour = is_colour(x,y,-1,-2,0,0,array)
            else:
                var,colour = is_colour(x,y,1,-1,0,0,array)

                if var == False:
                    var,colour = is_colour(x,y,-1,-2,0,0,array)
                if var == False:
                    var,colour = is_colour(x,y,1,2,0,0,array)

            if var == True:
                change = True
                array[y][x] = (not_really(colour))
            
            if line.count("0") > 0 and array[y][x] == "0" and change == False:
                
                r_count = line.count("R")
                b_count = line.count("B")
                
                if r_count == grid_size/2:
                    array[y][x] = (not_really("R"))
                    change = True
                if b_count == grid_size/2:
                    array[y][x] = (not_really("B"))
                    change = True
        #END ROWS

    #COLUMNS
    for x in range(grid_size):
        temp_list = []
        
        for y in range(grid_size):
            temp_list.append(array[y][x])
            
        for y in range(grid_size):
            if y == 0:
                var,colour = is_colour(x,y,0,0,1,2,array)
            elif y == grid_size-1:
                var,colour = is_colour(x,y,0,0,-1,-2,array)
            else:
                var,colour = is_colour(x,y,0,0,1,-1,array)
                #checks if in middle

                if var == False:
                    var,colour = is_colour(x,y,0,0,-1,-2,array)
                if var == False:
                    var,colour = is_colour(x,y,0,0,1,2,array)
                    
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
            

output(array)
with open(file_dest,"w") as file:
    for line in array:
        text = ""
        for i in range(grid_size):
            if i > 0:
                text = text + "," + line[i]
            else:
                text = line[i]
        file.writelines(text + "\n")
