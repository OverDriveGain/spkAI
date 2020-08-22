from core import answerQuestion, setAnswersFile
from filesHandlers import getAnswersFile, readAnswersFile

userOptions = ['exit', 'set user file (Answers text file)', 'ask a question on current user file: ']
exit = False

print("Use 0 for exit")
print("Use 1 for settings user file")
print("Use 2 for answering question")
while exit == False:
    userInput = input("Choose option: ")
    option = 0
    #Validate
    try:
        val = int(userInput)
        assert val < len(userOptions) and val >= 0, 0
    except ValueError:
        print("Value is not an integer")
        continue
    except AssertionError:
        print(AssertionError)
        if(AssertionError == 0):
            print("Option not present")
        continue
    option = val
    if(option == 0):         ## Exit app
        exit = True
    elif(option == 1):    ## Get answers file relative directory
        print("Please " + userOptions[option])
        userInput = input("Text file dir: ")
        if(readAnswersFile(userInput) == False):
            print("Something went wrong")
        elif(setAnswersFile(getAnswersFile()) != False):
            print("Answers file successfully set")
    elif(option ==2):
        print("Please " + userOptions[option] + getAnswersFile())
        userInput = input("Question: ")
        if(answerQuestion(userInput) == False):
            print("Something went wronge")