# Name: Andrea Marcosano
# Student Number: 10541054

#This is the main file for assingment 2 of Data structures and algorithms question 3
#LOTTO Question

import random #to generate random numbers
import math # to use floor and ceil in table operations\

from selectionSort import selectionSort  #selection sort of SWN
from insertionSort import insertionSort #insertion sort for PWN
from mergeSort import mergeSort  #merge sort for players numbers 


MAX_PLAYERS=1000 #global variable for maximum number of players
GENERATED_NUMBERS=6 #man number of numbers generated for each player 
WINNING_NUMBERS=8  #total number of winning numbers
SWN=2 ##length of SWN

#present main menu
def menu():
    while True:
        try:    
            print('MENU')
            print('1. Show initialised Data')
            print('2. Display statistics of winners')
            print('3. Check my Lotto Status')
            print('4. Exit')
            pick=int(input('Select option '))
            if pick>0 and pick<5:
                return pick
            else:
                print('Error.. try again')  #check if it is within range
        except ValueError:
            print("Error.. character is not valid  input")  #do not make program exit if input is a char 

#TASK 1     
#fucntion to generate distics integers random numbers
def initializeRow(numbers):
    random_numbers = []  #initialise list of random numbers

    while len(random_numbers) < numbers: #generate 6 numbers for 1 row
        random_number = random.randint(1, 30)  # Generate a random integer between 1 and 30 (inclusive)
        if random_number not in random_numbers:
            random_numbers.append(random_number)  #add the numbers only if they are unique

    return random_numbers

#fucntion to determine winning row number
def initializeWinningRow():
    winningHand=initializeRow(WINNING_NUMBERS)  #initialise winning numbers

    pwn=winningHand[:GENERATED_NUMBERS]
    ordered_pwn=insertionSort(pwn)  #use qucik sort module to sort out the list of numbers required
    swn=winningHand[GENERATED_NUMBERS:]
    ordered_swn=selectionSort(swn)  #use qucik sort module to sort out the list of numbers required

    winningRow=ordered_pwn+ordered_swn
    return winningRow

#fucntion to create the matrix of 1000 players
def initializeGame():
    
    lotto_players_data=[]
    for player in range(MAX_PLAYERS):  #generate 1000 players
        random_row=initializeRow(GENERATED_NUMBERS)
        random_numbers=mergeSort(random_row)  #use qucik sort module to sort out the list of numbers required
        lotto_players_data.append(random_numbers)

    return lotto_players_data

#function to print table on screen
def printTable(table,headers,length_row):
    for rowNumber, rows in enumerate(table):
        spaceFirst=(len(headers[0])-len(str(rowNumber)))  #calculate space of first element
        row = "| "+spaceFirst*' '+str(rowNumber)+" | "  #print the row of the table to recall players numbers
        for element in rows:
            spaceFirst=(math.floor(len(headers[1])/GENERATED_NUMBERS)-1-len(str(element)))  #calculate space of first element
            row=row+str(element)+spaceFirst*' '+'|'  #add values to one string
        print(row)
        print('-'*(length_row-3))

#function to print the headers of the table
def printHeaders(headers):

    #print headers
    headers_row='| '
    for header in headers:
        headers_row=headers_row+header+' | '  #create header row
    
    print('-'*(len(headers_row)-1))
    print(headers_row)  #print header row
    print('-'*(len(headers_row)-1))

    return headers_row

#function to print table of players and/or winners
def printInitialisedValues(Table,headers):
    headers_row=printHeaders(headers)
    if len(Table)>WINNING_NUMBERS:  #if the table given is a long table it means that the porgram is trying to print the list of players and their generated numbers
        printTable(Table,headers, len(headers_row))    #print the long tyable
    else:  #program is trying to print the winning table
        count=0
        spaceFirst=(len(headers[count])-len("Winning Hand"))  #calculate space of first element
        row = "| "+spaceFirst*' '+"Winning Hand"+" |"
        count+=1
        divisor=GENERATED_NUMBERS
        for index, element in enumerate(Table):
            space=math.ceil(len(headers[count])/divisor)-len(str(element))
            row=row+space*' '+str(element)
            if index==5:
                row+=' | '
                count+=1
                divisor= SWN
        print(row) #print row
        print('-'*(len(headers_row)-1))

#function to print requested data of players and winning numbers
def printPlayers(lotto,WinNo):
    headers = ["Players ID, i","Players i's game numbers"]  #headers of players table
    printInitialisedValues(lotto,headers)
    print("printing winning numbers...")
    headers = ["Winning ID, i","      PWNs       "," SWNs "]  #headers of winning table
    printInitialisedValues(WinNo,headers)

#TASK 2
#function that conducts binary search on rows and element of search
def binarySearch(element,winNumbers):
    left=0
    right=len(winNumbers)-1
    while left<=right:
        middle=math.floor((right + left) / 2)
        if element==winNumbers[middle]:
            return True
        else:
            if element<winNumbers[middle]:
                right=middle-1
            else:
                left=middle+1
    return False
#function to check wither the rows values ocorrspond to the PWNs values or SWns
def checkVictory(rows,winNumbers):
    matches=0  #matches to first 6 numbers 
    for element in rows:
        if binarySearch(element,winNumbers): #if the element is found then a match occured 
            matches+=1  
    return matches

#fucntion to calculate and see whether a player has won and calculate  whhether  it has all the  PWNs values  or SWNs values or not
def calculateWinners(lotto, WinNo):
    print("checking for winners...")
    stats=[]
    #separate WinNo
    PWNs=WinNo[:6]
    SWNs=WinNo[6:]
    player=0 #count the number of the player to analyze
    for rows in lotto:
        secondMatch=0
        matches=0
        matches=checkVictory(rows,PWNs)
        if matches<3:  #check SWn only if players has lless  than 3 matches
            secondMatch=checkVictory(rows,SWNs)  #same procedure of the normal match
        stats.append([player, matches,secondMatch])  #append results to store player number, and type of win
        player+=1
    return stats
#function to print the winning statistics
def printWinningTable(winningStats,headers,length_row):
    for position,value in winningStats.items():
        spaceFirst=(len(headers[0])-len(position))  #calculate space of first element
        spaceSecond=math.floor((len(headers[1])-len(str(value)))/2)
        row = "| "+spaceFirst*' '+position+" | "+(spaceSecond)*' '+str(value)+spaceSecond*' '+' |'
        print(row)
        print('-'*(length_row-1))

#function to check how many winners there were and their cathegory
def checkStats(statistics):
    #initialise variables for reading the statiistics in a dictionary 
    winningStats={'1st Class':0,
                  '2nd Class':0,
                  '3rd Class':0,
                  '4th Class':0}
    #check if the statistics match first second thrid or forth winning 
    for rows in statistics:
        if rows[1]==6:
            winningStats['1st Class']+=1
        elif rows[1]==5:
            winningStats['2nd Class']+=1
        elif rows[1]==4:
            winningStats['3rd Class']+=1
        elif rows[1]==3 or rows[2]==2:
            winningStats['4th Class']+=1

    print("printing winning statistics")
    #initialise headers
    headers = ["Winner Class","Total Number of Winners"]
    headers_row=printHeaders(headers) #print headers
    printWinningTable(winningStats,headers,len(headers_row))

#TASK3 
#fucntion to request and  verify input from user of player number
def inputPlayer():
    while True:
        try:
            playerNumber=int(input('Insert player number '))
            if playerNumber>=0 and playerNumber<MAX_PLAYERS:
                return playerNumber
            else:
                print('Error.. number must be between 0 and 999')
        except ValueError:
            print("Error.. character is not valid  input")

#fucntion to determine output of status to player
def createMessage(rows,WinNo):
    PWNs=WinNo[:6]
    matches=match_value(rows,PWNs)  #call macthing function to calculate number of matches
    if  matches==6:
        return "You win the game, congratulations!"
    elif matches==5:
        return "You are a 2nd class winner, congratulations!"
    elif matches==4:
        return "You are a 3rd class winner, congratulations!"
    elif matches==3:
        return "You are a 4th class winner, congratulations!"
    elif matches<3:
        SWNs=WinNo[6:]
        if match_value(rows,SWNs)==2:
            return "You are a 4th prize with SWNs, congratulations!"
        else:
            return "you are not a winner. Thanks for playing lotto, Good luck next time!"

#fucntion to create dictionary to print
def parseDetails(player,rows,WinNo):
    details={"Player's ID:":player-1, #negative one has the actual list goes ffrom 0 to 999 not 1-1000
             "Player's game-numbers:":rows,
             "PWNs:": WinNo[:6],
             "SWNs:": WinNo[6:],
             "Player's status:": createMessage(rows,WinNo)}
    return details

#function to print players details and winning stats
def printPlayerInfo(player,rows,WinNo):
    details=parseDetails(player,rows,WinNo)
    longValue1="Player's game-numbers:" #longest value in first column 
    longValue2=details["Player's status:"]
    length_row=len(longValue1)+len(longValue2)
    print('-'*(length_row+5))
    for position,value in details.items():  #create table to print palyers details
        spaceFirst=(len(longValue1)-len(position))  #calculate space of first element
        spaceSecond=math.floor((len(longValue2)-len(str(value))))
        row = "| "+position+spaceFirst*' '+" | "+str(value)+(spaceSecond)*' '+'|'
        print(row)
        print('-'*(length_row+5))
def match_value(A,B):
    # merge existing sorted arrays a1[l1...r1] and a2[l2...r2]
    # into an array a3[l3...], while keeping a3 sorted
    left1=0
    left2=0
    right1=len(A)-1
    right2=len(B)-1
    C=[]
    while left1 <= right1 and left2 <= right2:
        if A[left1]==B[left2]:
            C.append(A[left1])
            left1+=1
            left2+=1
        elif A[left1]<B[left2]:
            left1+=1
        else:
            left2+=1
    return len(C)  #return length of C as it correpsoinds to the matched values

#function to search player within the game and their  results
def searchPlayer(lotto, WinNo):
    playerNumber=inputPlayer()
    print("Looking for player.. ",playerNumber)
    playerNumber+=1
    player=0
    for rows in lotto:
        player+=1
        if player==playerNumber:
            printPlayerInfo(playerNumber,rows,WinNo)
#main
if __name__== '__main__':
    lotto = initializeGame()  #initialize the game
    WinNo=initializeWinningRow()  #initalise winning
    while True:
        pick=menu()

        if pick==1:  #print players values and winning numbers
            print("printing players...")
            printPlayers(lotto,WinNo)
            
        elif pick==2:  #calculate statistics of who won
            statistics=calculateWinners(lotto,WinNo)
            checkStats(statistics) #print statistics on a table
        elif pick==3:
            searchPlayer(lotto, WinNo)  #search for enternered players
        else:#exit
            print("The program is exiting...")
            print("Thank you for playing") 
            break