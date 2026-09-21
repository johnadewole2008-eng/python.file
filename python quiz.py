#python quiz
questions=("How many elements are in the periodic table?",
"which bird lay the largest egg?",
"How many bones are in the human body?",
"What is the most abundant gas in the human atmosphere?",
"Which planet in the solar system is the hottest?")
options=(("A.116", "B.117", "C.118", "D.119"),
          ("A.whale ", "B.ostrich ", "C.eagle ", "D.goat "),
            ("A.304 ", "B.305 ", "C.306 ", "D.307 "),
            ("A.oxygen ", "B.Nitrogen ", "C.Carbon-dioxide ", "D.Hydrogen "),
              ("A.Mecury ", "B.Venus ", "C.Earth ", "D.Mars "))
answers=("C", "B", "C", "B", "B")
guesses=[]
score=0
question_num=0
for question in questions:
    print("---------------------------------------------------------")
    print(question)
    print("---------------------------------------------------------")
    for option in options[question_num]:
        print(option)
    guess=input("enter answer(A,B, C, D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("you are correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct option")
    question_num+=1

print(f"your total score is {score}")