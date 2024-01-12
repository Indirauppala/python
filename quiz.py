def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1
    for key in questions:
        print("-----------------")
        print(key)
        for i in answers[question_num-1]:
            print(i)
        guess=input("enter a,b,c or d..?")
        guesses.append(guess)
        correct_guesses+=checkAnswer(questions.get(key),guess)
        question_num+=1
    display_score(correct_guesses)
    x=input("\n Do you wanna play again(yes/no)")
    play_again(x)

def checkAnswer(key,guess):
    if key==guess:
        print("WOW..! correct")
        return 1
    else:
        print("shut..!wrong")
        return 0

def display_score(guesses):
    print("\n your score is",guesses,"points")
    score=int(guesses/len(questions)*100)
    print("Your percentage is ",score,"%")
    if guesses==7:
        print("wow..!you performed well")

def play_again(x):
    if x=="yes":
        new_game()
    else:
        print("\n Thats it for now!thank you for participating..!!")

questions={"1.who created python?":"b",
           "2.In which year python was created?":"b",
           "3.Is the earth round?":"a",
           "4.where is charminar loacated?":"a",
           "5.What is the chemical symbol for silver?":"b",
           "6.What is the world’s smallest bird?":"c",
           "7.who is the president of india":"d" }


answers=[["a.elon musk","b.guido van rossum","c.mark zukenberg","d.indira"],
         ["a.2020","b.1991","c.2003","d.1950"],
         ["a.yes","b.no","c.maybe","d.i dont know"],
         ["a.hyderabad","b.vijayawada","c.agra","d.mumbai"],
         ["a.br","b.ag","c.pt","d.si"],
         ["a.sparow","b.parrot","c.hummingbird","d.piegeon"],
         ["a.nehru","b.Ram Nath Kovind","c.Indira","d.Draupadi Murmu"]]

new_game()