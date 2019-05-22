import random
flag=True
my_score=0
score=0
temp=1
print("CRICKET")
toss=['head','tail']
turn=['bat','bowl']
line='....................................'

choice_toss=input("head OR tail???:")
print(line)
choice=random.choice(toss)

if choice_toss==choice:
    print("You won the toss!!!!!")
    print(line)
    choice_turn=input("Do you want to bat or bowl???:")
    if choice_turn=='bat':
        print("Now you are batting...")
        print(line)
        my_score=0
        score=0
        while flag==True:
            ms=int(input("Enter any number:"))
            s=random.randint(1,10)
            if ms!=s:
                my_score+=ms
                print("Your final score is:",my_score)
                print(line)
                
            else:
                print("OOOPS!!!!\nYou are out!!!!")
                print("Your final score is:",my_score)
                print(line)

                print("Now you are bowling...")
                print(line)
                while temp==1:
                    ms1=int(input("Enter any number:"))
                    s1=random.randint(1,10)
                    if ms1!=s1:
                        score+=s1
                        print("Oponent\'s score is:",score)
                        print(line)
                    else:
                        print("Opopnent is out!!!")
                        print("Oponent\'s score is:",score)
                        print(line)
                        flag=False
                        temp=0
    elif choice_turn=='bowl':
        print("Now you are bowling....")
        print(line)
        my_score=0
        score=0
        while flag==True:
            ms1=int(input("Enter any number:"))
            s1=random.randint(1,10)
            if ms1!=s1:
                score+=s1
                print("Oponent\'s score is:",score)
                print(line)
            else:
                print("Opopnent is out!!!")
                print("Oponent\'s score is:",score)
                print(line)

                print("Now you are batting....")
                print(line)
                while temp==1:
                    ms=int(input("Enter any number:"))
                    s=random.randint(1,10)
                    if ms!=s:
                        my_score+=ms
                        print("Your final score is:",my_score)
                        print(line)
                    else:
                        print("OOOPS!!!!\nYou are out!!!!")
                        print("Your final score is:",my_score)
                        print(line)
                        flag=False
                        temp=0

elif choice_toss!=choice:
    ch=random.choice(turn)
    if ch=='bowl':
        print("You are batting...")
        print(line)
        my_score=0
        score=0
        while flag==True:
            ms=int(input("Enter any number:"))
            s=random.randint(1,10)
            if ms!=s:
                my_score+=ms
                print("Your final score is:",my_score)
                print(line)
            else:
                print("OOOPS!!!!\nYou are out!!!!")
                print("Your final score is:",my_score)
                print(line)

                print("Now you are bowling...")
                print(line)
                while temp==1:
                    ms1=int(input("Enter any number:"))
                    s1=random.randint(1,10)
                    if ms1!=s1:
                        score+=s1
                        print("Oponent\'s score is:",score)
                        print(line)
                    else:
                        print("Opopnent is out!!!")
                        print("Oponent\'s score is:",score)
                        print(line)
                        flag=False
                        temp=0
    elif ch=='bat':
        print("Now you are bowling...")
        print(line)
        my_score=0
        score=0
        while flag==True:
            ms1=int(input("Enter any number:"))
            s1=random.randint(1,10)
            if ms1!=s1:
                score+=s1
                print("Oponent\'s score is:",score)
                print(line)
            else:
                print("Opopnent is out!!!")
                print("Oponent\'s score is:",score)
                print(line)

                print("Now you are batting....")
                print(line)
                while temp==1:
                    ms=int(input("Enter any number:"))
                    s=random.randint(1,10)
                    if ms!=s:
                        my_score+=ms
                        print("Your final score is:",my_score)
                        print(line)
                    else:
                        print("OOOPS!!!!\nYou are out!!!!")
                        print("Your final score is:",my_score)
                        print(line)
                        flag=False
                        temp=0
if my_score>score:
    print(line)
    print(line)
    print(line)
    print("CONGO!!!!\nYOU WON!!!!!")
    print(line)
    print(line)
    print(line)
elif my_score<score:
    print(line)
    print(line)
    print(line)
    print("OOOPS!!!!\nYOU LOOSE!!!!")
    print(line)
    print(line)
    print(line)
else:
    print(line)
    print(line)
    print(line)
    print('!!!TIEEE!!!')
    print(line)
    print(line)
    print(line)
