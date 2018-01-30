#Grid Printer Exercise
#Chay Casso, 1/29/18

def grid1():
    """Draw a simple 2x2 grid composed of 5x5 squares."""
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    blankminus = blank + minus
    print(plus + blankminus * 4 + blank + plus + blankminus * 4 + blank + plus)
    for i in range(1, 5):
        print(pipe + blank * 9 + pipe + blank * 9 + pipe)
    print(plus + blankminus * 4 + blank + plus + blankminus * 4 + blank + plus)
    for i in range(1, 5):
        print(pipe + blank * 9 + pipe + blank * 9 + pipe)
    print(plus + blankminus * 4 + blank + plus + blankminus * 4 + blank + plus)

def GridLine2(gridsize=3):
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    blankminus = blank + minus
    print(plus + blankminus * ((gridsize - 1) / 2) + blank + plus + blankminus * ((gridsize - 1) / 2) + blank + plus)

def GridSpace2(gridsize=3):
    plus = "+"
    minus = "-"
    blank = " "
    pipe = "|"
    blankminus = blank + minus
    print(pipe + blank * gridsize + pipe + blank * gridsize + pipe)

def grid2(gridsize=3):
    GridLine2(gridsize)
    for i in range(1, (gridsize + 1) / 2):
        GridSpace2(gridsize)
    GridLine2(gridsize)
    for i in range(1, (gridsize + 1) / 2):
        GridSpace2(gridsize)
    GridLine2(gridsize)
    
grid2(3)