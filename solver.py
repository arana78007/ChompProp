#NEW approach is to remove the chomped of columns then consider the board before and after in the recursive call

#function gives us a clean version of the game
def cleangrid(grid):
    grid = tuple(grid)
    if 0 in grid:
        grid = grid[:grid.index(0)]
    return grid

def moveoptns(grid):
    moves = []
    for rows in range(4):
        if rows == 3:
            for i in range(1,grid[3]+1):
                gridcopy = grid.copy()
                gridcopy[rows] = grid[rows]-i
                moves.append(cleangrid(gridcopy))
        elif rows == 2:
            for i in range(1,grid[2]+1):
                gridcopy = grid.copy()
                gridcopy[rows] = grid[rows]-i
                gridcopy[rows+1] = gridcopy[rows]
                moves.append(cleangrid(gridcopy))
        elif rows == 1:
            for i in range(1,grid[1]+1):
                gridcopy = grid.copy()
                gridcopy[rows] = grid[rows]-i
                gridcopy[rows+1] = gridcopy[rows]
                gridcopy[rows+2] = gridcopy[rows]
                moves.append(cleangrid(gridcopy))
        
        elif rows == 0:
            for i in range(1,grid[0]+1):
                gridcopy = grid.copy()
                gridcopy[rows] = grid[rows]-i
                gridcopy[rows+1] = gridcopy[rows]
                gridcopy[rows+2] = gridcopy[rows]
                gridcopy[rows+3] = gridcopy[rows]
                moves.append(cleangrid(gridcopy))
    return moves

## Logic works just need to add 2 for loop that goes through each of the ifs one by one and then outputs the cleaned grid

print(moveoptns([5,5,5,5]))


            
    
        
