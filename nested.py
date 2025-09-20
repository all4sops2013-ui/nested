# nested conditional statements

n=100
if n<200:
    print("n is smaller than 200")

    if n<100:
        print("n is smaller than 100 too")





q1=input("what si the capital of India?")
if q1=="New dehli":
    print("good")
    q2=input("what is the capital of Nigeria?")
    if q2=="Abuja":
        print("well done")





q1=input("do you a medical cause?")
if q1=="yes":
    print("You are allowed to resit the exam")
else: 
    q2=input("is your attendance more than 75%")
    if q2=="yes":
        print("you are allowed to resit the exam")
    else:
        print("you are not allowed to resit the exam")





q1=input("which is you fav ride,a two wheeler or four wheeler")
if q1=="two wheeler":
    ans=input("which one bike or scooter?")
    if q1=="four wheeler":
        ans_2=input("which one jeep or car?")