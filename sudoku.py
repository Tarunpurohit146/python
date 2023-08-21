'''
Sudoku Game

The program creates a random question and uses the back-tracking method to solve it.

'''

import random
board=[]
def solve(bo): 
    find=find_empty(bo) 
    if not find:
        return True 
    else:
        row,col=find
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i
            if solve(bo):
                return True
            bo[row][col]=0
    return False 

def valid(bo,num,pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[0]!=i:
            return False
    #check 3x3 box
    box_x=pos[1]//3  
    box_y=pos[0]//3 
    for i in range(box_y*3 ,box_y*3+3): 
        for j in range(box_x*3,box_x*3+3): 
            if bo[i][j]==num and (i,j)!=pos: 
                return False  
    return True 

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j)
    return None

def question(bo):
    for i in range(len(bo)):
        r=random.sample(range(1,9),5)
        for j in range(len(bo[i])):
            if j in r:
                bo[i][j]=0

def genarate():
    for i in range(9):
        board.append([0  for j in range(9)])
    board[0]=random.sample(range(9),9) #add's random value to create different solution
    solve(board)

def print_board(bo):  
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("--------------------")
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print("|",end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ",end="")

genarate()
board1=[i[:] for i in board] #deep copy you can use copy.deepcopy() from copy module
question(board1)
print_board(board1)
print("\n~~~~~~~~~~~~~~~~~~~~\n")
print_board(board)



