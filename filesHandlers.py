import os
currentDir = os.path.dirname(os.path.realpath(__file__)) + '/'
answersFile = ''

def getAnswersFile():
    return answersFile

def readAnswersFile(dir):
    global answersFile
    fileDir = currentDir +  dir
    if(os.path.isfile(fileDir) == False):
        return False
    with open(fileDir, 'r') as file:
        answersFile = file.read().replace('\n', '')
    return True