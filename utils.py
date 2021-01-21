import time
import random

def checkEmailList(emailList):
    for i in emailList:
        if not '@' in i or not '.' in i:
            print('Error: wrong email format')
            exit(1)

def delay(min, max, minutes=False, hours=False):
    if minutes:
        return time.sleep(random.randrange(min, max) * 60)
    else:
        return time.sleep(random.randrange(min, max))

def listToStrWithSeparator(list, separator):
    res = separator.join(map(str, list))
    return res

def isPositive(int):
    if int >= 0:
        return True
    else:
        return False

def isMinInferiorMax(min, max):
    if min < max:
        return True
    else:
        return False

def checkMinMax(min, max, positive=True, negative=False):
    if positive and not negative:
        if not isPositive(min):
            print("Error: Min value needs to be postive")
            exit(1)
        if not isPositive(max):
            print("Error: Max value need to be postive")
            exit(1)
    elif negative and not positive:
        if isPositive(min):
            print("Error: Min value need to be negative")
            exit(1)
        if isPositive(max):
            print("Error: Max value need to be negative")
            exit(1)
    if not isMinInferiorMax(min, max):
        print("Error: Min value needs to be inferior to max")
        exit(1)

def checkMinRequired(min, required):
    if required and min == 0:
        print("Error: can't be a required text and a minimum of 0 word")
        exit(1)
    elif not required and min != 0:
        print("Error: can't be a not required text and a minimum of not 0 word"")
        exit(1)
