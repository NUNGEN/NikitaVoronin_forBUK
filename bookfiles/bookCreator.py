def guestBook():
    name = input("Your name ")
    comment = input("Your message")
    time = datetime.datetime.now()
    text = f"Nimi: {name}, message:  {comment}\n"
    file = open("guestBook.txt","a", encoding="utf-8")
    file.write(text)
    file.close()
    print("message was full of feedback")