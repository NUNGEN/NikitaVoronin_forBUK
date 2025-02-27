"""
User managment system
id: 1, Name: Thomas, 44
id: 2, Name: Thomas, 44
id: 3, Name: Thomas, 44

file = open("myfile.txt","w") w-write a-append r-read
file.write("myTekst")
file.close()
"""

import bookCreator as bookCreator
import bookAction as activityBook
import fileReader as reader
import bukManager as bukManager

def testfile():
    print("1 - book of reports")
    print("2 - book of actions")
    print("3 - Read logs")
    userInput = input("Your choise: ")
    if userInput == "1":
        bookCreator.guestBook()
    elif userInput == "2":
        activityBook.activityBook()
    elif userInput == "3":
        userFile =input("which file you want to read ?")
        reader.readFile(userFile)
     elif userInput == "4":
         
    else:
        print("Incorrect choise")
        
testfile()