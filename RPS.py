gameDict= {'Rock':1,'Paper':3,'Scissor':2}
while True:
    def getInput():
        p1=str(input("Enter your option from 'Rock', 'Paper', 'Scissor':" ))
        p2=str(input("Enter your option from 'Rock', 'Paper', 'Scissor':" ))
        return(p1,p2)
    while True:
        global a,b
        a,b=getInput()
        if not(a in gameDict.keys() and b in gameDict.keys()):
            print("Please enter a valid input")
            continue
        break

    u1=gameDict.get(a)
    u2=gameDict.get(b)
    diff=u1-u2
    if diff in [-1,2]:
        print('Congratulations! Player 1 wins:)')

    elif diff in[-2,1]:
        print('Congratulations! Player 2 wins:)')
    else:
        print("It's a draw!")
    if input("Do you wany to play again?(Y/N): ")=='Y':
        continue
    else:
        break
