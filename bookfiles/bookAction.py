import datetime
print(datetime.datetime.now())
def activityBook():
    name = input("Your name ")
    action = input("Your last action")
    textAction = f"Date: {time} Name: {name}, what you did:  {action}\n"
    file = open("activityBook.txt","a", encoding="utf-8")
    file.write(textAction)
    file.close()
    print("action is confirmed")