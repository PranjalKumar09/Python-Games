from math import isqrt


questions = [["The International Literacy Day is observed on" , "Sep 8","Nov 28" , "May 2" , "Sep 22" , 1],
            ["The language of Lakshadwee is" , "Tamil","Hindi" , "Malayalam" , "Telugu" , 3],
            ["Which of these is measured with the help of a glucometer?" , " Heartbeat","Blood pressure" , " Vision" , "Blood sugar",3],
            ["With which of these states does Telengana not share its border?" , "Tamil Nadu","Karnataka" , "Chattisgarh" , "Maharashtra",1],
            ["How many watts equal a megawatt?" , "One hundred","One thousand" , "Ten thousand" , "One lakh",4],
            ["Which of these is the largest planet in our solar system?" , "Jupiter","Saturn" , "Uranus" , "Neptune",1],
            ["What is the name of the largest continent on Earth?" , "Asia","Africa" , "North America" , "Antarctica",2],
            ["Which of these is a type of reptile?" , "Lion","Elephant" , "Giraffe" , "Crocodile",3],
            ["What is the name of the smallest bone in the human body?" , "Ear bone" , "Nose bone" , "Tooth bone" , "Finger bone",4],
            ["Which of these is a type of bird?" , "Camel","Kangaroo" , "Zebra" , "Ostrich",4],
            ["Which of these is a type of fruit?" , "Apple","Orange" , "Banana" , "Pineapple",3],
            ["What is the name of the process by which plants make food?" , "Photosynthesis","Respiration" , "Digestion" , "Circulation",1],
            ["Which of these is a type of mammal?" , "Snake","Bird" , "Fish" , "Elephant",4],
            ["Which of these is a type of flower?" , "Sunflower","Rose" , "Lily" , "Daisy",3],
            ["Which of these is a type of vegetable?" , "Carrot","Potato" , "Cabbage" , "Tomato",3]
            ]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"Question is {question[0]}")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            c. {question[4]}")
    reply = int(input ("Enter you answer (1-4)  or 0 to Quit "))
    if reply == 0:
        break
    if (reply == question[-1]):
        print(f"\n\ncorrect answer, you have won  {levels[i]}")
        if (i == 4 or i == 9 or i ==14 ):
            money = levels[i]
    
        
    else:
        print("Wrong answer!")
        break
    
print(f"\n\nYour take home money is {money}")
    
    
    
    