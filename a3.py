#a3.py
#In my computer, 'python a3.py' will work instead of 'python3 a3.py'

import random

#Display the Tic-Tac-Toe  
def display(tic):
    print("Current Tic-Tac-Toe: ")
    print(' ', tic[0], "|", tic[1], "|", tic[2],'\n')
    print(' ', tic[3], "|", tic[4], "|", tic[5],'\n')
    print(' ', tic[6], "|", tic[7], "|", tic[8])


#Determine the result is win, loss or draw
def result(tic):
    win = ' '
    for i in range(3):
        if tic[3*i] == tic[3*i+1] == tic[3*i+2]:
            win = tic[3*i]
            break
    for i in range(3):
        if tic[i] == tic[i+3] == tic[i+6]:
            win = tic[i]
            break
    if tic[0] == tic[4] == tic[8]:
        win = tic[0]
    if tic[2] == tic[4] == tic[6]:
        win = tic[2]
    
    if win == ' ':
        count = 0
        for i in tic:
            if i == ' ':
                count+=1
        
        if count == 0:
            return 'd'
        
    return win
    

#Return the total grades of random results(win+1, draw+1, loss-1)
def playout(tic, grade):
    position = []
    for i in range(len(tic)):
        if tic[i] == ' ':
            position+=[i]
    
    #Random playouts, and break loop if there is a result
    for i in range(1, len(position)+1):
        if i%2 == 1:
            rand = random.choice(position)
            tic[rand] = 'X'
            position.remove(rand)
            
        elif i%2 == 0:
            rand = random.choice(position)
            tic[rand] = 'O'
            position.remove(rand)
            
        res = result(tic)

        if res == 'O' or res == 'd':
            grade+=1
            break
        elif res == 'X':
            grade-=1
            break
        
    return grade


#Total random playouts control
def playouts(tic):
    count = 0
    determine = [] #store the selected results
    for i in range(len(tic)):
        if tic[i] == ' ':
            count+=1
            determine = determine + [[i, -1]]
    
    iter1 = 0
    while iter1 < count:
        wad = 0
        #Not sure 1000 is okay in TA's computer, in my test, all my tries are okay
        for j in range(1000):
            temp = tic.copy()
            temp[determine[iter1][0]] = 'O'
            wad = playout(temp, wad)
        determine[iter1][1] = wad
        iter1+=1
    
    #Compare the final grades, choose one biggest(best)
    finaldet, comp = 0, -1000000
    for x in range(len(determine)):
        if determine[x][1] > comp:
            comp = determine[x][1]
            finaldet = determine[x][0]
    
    tic[finaldet] = 'O'
    print("Computer Turn:")
    display(tic)


#Main function of Tic-Tac-Toe
def play_a_new_game():
    
    again = 1
    print("Index of  Tic-Tac-Toe: ")
    print(' ', '1', "|", '2', "|", '3','\n')
    print(' ', '4', "|", '5', "|", '6','\n')
    print(' ', '7', "|", '8', "|", '9')
    print("Your chess will be 'X'!")
    
    while again == 1:
        play = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        start = 0
        
        while(start == 0):
           first = input("Do you want to start first?(y/n):" )
           if first != 'n' and first != 'y':
               print("Error input, please enter again.")
           else:
               start = 1
             
        if(first == 'n'):
            playouts(play)
        
        win = result(play)
        while win == ' ':
            turn = 0
            while turn == 0:
                enter = int(input("Please enter position you want to put(1 to 9): "))
                if(enter <= 9 and enter >= 1):
                    if(play[enter-1] == ' '):
                        play[enter-1] = 'X'
                        turn = 1
                        display(play)
                    else:
                        print("Wrong input, please put chess again")
                else:
                    print("Wrong input, please put chess again")
            win = result(play)
            if win == ' ':
                playouts(play)
                win = result(play)
        
        if win == 'd':
            print("Draw Game!")
        elif win == 'X':
            print("You Win!")
        elif win == 'O':
            print("Computer win!")
            
        wantAgain = input("Do you want to play again?(y/n): ")
        if wantAgain != 'y':
            again = 0
        
    print("End game!")
                
        
        
if __name__ == '__main__':
    play_a_new_game()
