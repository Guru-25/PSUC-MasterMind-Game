import random
from termcolor import colored
import os
def intro():
    print("\t\tMASTER MIND")
    print("* This is a code breaking game")
    print("* The computer generates a code consisting of 4 colours : RED,BLUE,GREEN,YELLOW")
    print("* The user is asked to input a string of 4 digits: 1,2,3,4")
    print("* Each digit corresponds to a colour : \n1-RED \n2-BLUE \n3-GREEN \n4-YELLOW")
    print("* A maximum of 10 attempts are provided to decode the system generated code")
    print("* Number of R'S corresponds to the number of digits which are RIGHT digits placed in RIGHT positions")
    print("* Number of W'S corresponds to the number of digits which are RIGHT digits placed in WRONG positions")
    print("* Number of X'S corresponds to the number of digits which are WRONG digits")
    print("* Score depends on the number of attempts used")
    k=True
    while(k):
        choice=input("Please type in YES to start the game ...")
        if(choice.upper()=="YES"):
            k=False
def keydict(temp):
    colour_key={1:"RED",2:"BLUE",3:"GREEN",4:"YELLOW"}
    retVal=colour_key[temp]
    return retVal
def correctCode(listPara):
    for temp in listPara:
        k=keydict(temp)
        print(colored(k[:3],'{}'.format(k.lower())),end="\t")
    print()
def codePrint(listPara):
    for temp in listPara[0]:
        k=keydict(temp)
        print(colored(k[:3],'{}'.format(k.lower())),end="\t")
    for temp in range(listPara[1]):
        print(colored("R","magenta"),end="\t")
    for temp in range(listPara[2]):
        print(colored("W","white"),end="\t")
    for temp in range(listPara[3]):
        print(colored("X","black"),end="\t")
    print()
def codemaker():
    codePara=[1,2,3,4]
    random.shuffle(codePara)
    return codePara
def codebreaker(codePara):
    colList=[]
    for i in range(10,-1,-1):
        try:
            codeGuessIn=input("Enter code :")
            codeGuess=[int(x) for x in codeGuessIn]
            os.system("cls")
        except:
            os.system('cls')
            print("Wrong input!! Try again")
            continue
        if(len(codeGuess)!=4):
            os.system('cls')
            print("Wrong input!! Try again")
            continue
        flag = 0
        for x in codeGuess:
            if x > 4 or x < 1:
                flag = 1
        if flag == 1:           
            os.system('cls')
            print("Wrong choice!! Try again!!")
            continue 
        if(codeGuess==codePara):
            break
        else:
            exactDigits=validDigits=0
            for j in range(len(codePara)):
                if(codePara[j]== codeGuess[j]):
                    exactDigits+=1
                elif(codeGuess[j] in codePara):
                    validDigits+=1
            incrctDigits=4-(exactDigits+validDigits)
            colList.append([codeGuess,exactDigits,validDigits,incrctDigits])
            for i in colList:
                codePrint(i)
    return i
intro()
os.system('cls')
code=codemaker()
score=codebreaker(code)
print("\n\n\n\n")
correctCode(code)
if (score in range(1,11)):
    print("Your Score : {}/10".format(score))
else:
    print("Your Score : 0/10")
