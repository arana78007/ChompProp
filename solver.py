# want to store everything in a cache
grid_test = [0,0,0,0]
cache = [(grid_test,True)]
grid = [5,5,5,5]


# take a grid input check if it is all 0 (lose), then check other chomps and based on that see if we can get a recursive solution

def solver(grid):
    grid_tuple = tuple(grid)
    if grid_tuple == (0,0,0,0):
        print("DEAD")
        cache.append((grid ,False))
        return cache
    
    if (grid, True) in cache:
        return cache
        
    gridcopy = grid.copy()
    for rows in range(len(grid)):
        for col in range(grid[rows]):
            postchomp = gridcopy[:rows] + [min(col, gridcopy[i]) for i in range(rows, len(grid))]
            print(postchomp)
        
        
solver(grid)

## TO DO    SO FAR HAVE A PYGAME SET UP, NEED TO COMPLETE THE SOLVER, CURRENTLY IT CAN CHOMP CORRECTLY WHICH IS GOOD, ADD RECURSIVE ELEMENT NEXT, AND SOLVE BY PICKING TRUE OPTIONS FROM CACHE
## THEN COMBINE BOTH FILES TOGETHER TO GET A OVERALL OUTCOME. 
        


            
    
        
