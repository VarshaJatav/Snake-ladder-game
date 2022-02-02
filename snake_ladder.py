#================correct program===============

import random
def fun_ran(num):
    return (random.randint(1,num))

def show(l1):
    for i in range(1,101):
        if A==i:
            print("A",end="     ")
            if i%10==0:
                print()
            continue
        elif B==i:
            print("B",end="     ")
            if i%10==0:
                print()
            continue
        if i in l1.keys():
            if i>l1[i]:
                print(l1[i],end="     ")
            else:
                print("+",l1[i],end="     ")
        else:
            print(i,end="      ")
        if i%10==0:
            print()

def win(A,B):
    if A>=100:
        print("\n\n\n\t\t\tPlayer A win")
        exit()
    elif B>=100:
        print("\n\n\n\t\tPlayer B win")
        exit()

def player(A):
    x=fun_ran(6)
    print("\nDice:  ",x)
    if (A+x) in board.keys():
        A=A+x
        A=A+board[A]
    else:
        A=A+x
    return A



board={2:14,46:-26,9:24,32:-7,44:46,98:-20,50:5,65:-14,80:-48}
A,B=0,0
while(True):
    a=input("\n\nPlayer A chance(press Enter):  ")
    A=player(A)
    if A==B:
        B=0
        print("B:  0")
    print("\n\nPostion of A:  ",A)
    show(board)
    win(A,B)
    a=input("\n\nPlayer B chance(press Enter):  ")
    B=player(B)
    if A==B:
        A=0
        print("\nA  : 0")
    print("\nPosition of B:   ",B)
    show(board)
    win(A,B)






'''

# variable length argu
A=[[1,2,3],[3,4,5],[6,7,8]]
# import numpy as np
# print(np.matrix(A))


# for row in A:
#     for val in row:
#         print '{:4}'.format(val),
#     print

'''






'''================wrong code==================
import random
def fun_ran(num):
    return (random.randint(1,num))
game=[]
def printing(g):
    print(g)
def show(l1):
    for i in range(1,101):
        if A==i:
            game.append('A')
            continue
        elif B==i:
            game.append('B')
            continue
        if i in l1.keys():
            if i>l1[i]:
                game.append("s."+str(l1[i]))
            else:
                game.append("l."+str(l1[i]))
        else:
            game.append(i)
    printing(game)

board={2:14,46:-26,9:24,32:-7,44:66,98:-20,50:5,65:74,80:-48}
A,B=0,0
while(True):
    a=input("Player A chance(press Enter):  ")
    x=fun_ran(6)
    print("Dice:  ",x)
    if (A+x) in board.keys():
        A=A+x+board[x]
    else:
        A=A+x
    print("Postion of A:  ",A)
    show(board)
    a=input("Player B chance(press Enter):  ")
    x=fun_ran(6)
    print("Dice:  ",x)
    if (B+x) in board.keys():
        B=B+x+board[x]
    else:
        B=B+x
    print("Position of B:   ",B)
    show(board)
    if A==100:
        print("Player A win")
        exit()
    elif B==100:
        print("Player B win")
        exit()
'''


'''========correct code====================
import random
def fun_ran(num):
    return (random.randint(1,num))

def show(l1):
    for i in range(1,101):
        if A==i:
            print("A",end="     ")
            continue
        if B==i:
            print("B",end="     ")
            continue
        if i in l1.keys():
            if i>l1[i]:
                print(l1[i],end="     ")
            else:
                print("+",l1[i],end="     ")
        else:
            print(i,end="      ")
        if i%10==0:
            print()

board={2:14,9:24,32:-7,40:57,46:-26,44:46,50:5,65:14,77:-45,80:-48,98:-20}
A,B=0,0
while(True):
    a=input("Player A chance(press Enter):  ")
    x=fun_ran(6)
    print("Dice:  ",x)
    if (A+x) in board.keys():
        A=A+x
        A=A+board[A]
    else:
        A=A+x

    if A==B:
        B=0
    print("Postion of A:  ",A)
    # show(board)
    a=input("Player B chance(press Enter):  ")
    x=fun_ran(6)
    print("Dice:  ",x)
    if (B+x) in board.keys():
        B=B+x
        B=B+board[B]
    else:
        B=B+x
    
    if A==B:
        A=0
    print("Position of B:   ",B)
    # show(board)
    if A==100:
        print("Player A win")
        exit()
    elif B==100:
        print("Player B win")
        exit()
'''