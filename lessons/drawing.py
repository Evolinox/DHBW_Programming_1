charOne = "X"
charTwo = "O"

rows = 32
columns = 32

def draw(rows:int,columns:int):
    halfrow = rows/2
    halfcolumn = columns/2
    print(f"Drawing something on a {rows}Px by {columns}Px Canvas")
    for x in range(rows):
        if x < halfcolumn:
            print(charOne*int(x), end=" ")
            print(" "*int(halfrow-x), end=" ")
        else:
            temp = abs(rows - x)
            print(charOne*int(temp), end=" ")
            print(" "*int(halfrow-temp), end=" ")
        print(" "*int(halfrow-x), end="")
        
        if x < halfcolumn:
            print(charTwo*int(x), end=" ")
            print(" "*int(halfrow-x), end="")
        else:
            temp = abs(rows - x)
            print(" "*int(halfrow-temp), end="")
            print(charTwo*int(temp), end=" ")
        print("")

draw(rows,columns)