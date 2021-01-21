# -*- coding: utf-8 -*-

import random as rd
import utils

def fillInput(max, required, multiple, minAnwsers, maxAnswers):
    ''' Range for checkboxes (multiple choice)
        For 3 checkboxes:
        - With at least 1, 2 or all checked:        checkbox(1, 3) or checkbox(max=3)
        - With none of them, 1, 2, or all checked:  checkbox(0, 3)
    '''
    min = 1
    #max += 1 # make inclusive to be more logical
    if not required:
        minAnswers = 0
        min = 0 # allow no answer
    if not multiple and maxAnswers != 0:
        print("Warning: since multiple responses are disabled for this question, maxAnswers is gonna be 0 anyway")
    if minAnwsers == 0:
        minAnwsers = 1
    if maxAnswers == 0:
        maxAnswers = max
    if multiple:
        maxAnswers += 1
        res = set() # avoid duplicate
        utils.checkMinMax(min, max)
        if (minAnwsers + 1 == maxAnswers): # exact number of answers
            loop = maxAnswers
            minAnwsers = 1
        else:
            loop = rd.randrange(minAnwsers + 1, maxAnswers + 1)
        for i in range(minAnwsers, loop): #inclusive
            rand = str(rd.randrange(min, max))
            while rand in res:
                rand = str(rd.randrange(min, max))
            res.add(rand)
        return list(res) # convert set to list
    else:
        res = []
        utils.checkMinMax(min, max)
        rand = str(rd.randrange(min, max))
        res.append(rand) # avoid splitting double digits
        return str(list(res))

def linear():
    return

def choiceGrid():
    return

def checkboxGrid():
    return

def shortAnswer(min=1, max=1, textlist=None, required=True):
    #return rd(textlist, weight, required)
    return text(min, max, textlist, required)

def paragraph(min=1, max=1, textlist=None, required=True):
    return text(min, max, textlist, required)

def multipleChoice(number=2, textlist=None, minAnwsers=0, maxAnswers=0, required=True):
    return fillInput(max, required, False, minAnwsers, maxAnswers)

def checkboxes(number=2, min=1, max=2, fields=None, required=True):
    return fillInput(max, required, True, 1, 1)

def dropdown(number=2, fields=None, required=True):
    return fillInput(max, required, False, 1, 1)

def yesOrNo(required=True):
    return text(1, 1, ["Yes", "No"], required)

'''
def time(h=0, m=0, required=True):
    return [number(0, 24), number(0, 60)]

def date(d=1, m=1, y=2000, required=True):
    return number(0, 31)
'''

def number(min=0, max=1, required=True, positive=True, negative=False):
    ''' Range for number input (single choice)
        utils.checkMinMax will check if max and min are positive, negative and both
        0 count as a positive number
    '''
    max += 1 # make inclusive to be more logical
    utils.checkMinMax(min, max, positive, negative)
    # decimal to do
    return str(rd.randrange(min, max))

def text(min=1, max=2, textlist=None, weight=[100], required=True, separator=', '):
    ''' Range for text input (single or multiple words)
        Single word: text(1, 1, ...)
        Between 1 word and 4 words: text(1, 4, ...)

        To enable the none outcome (no words): text(list, 0, ...)
        No duplicate
    '''
    max += 1 # make inclusive to be more logical
    res = []
    utils.checkMinMax(min, max)
    utils.checkMinRequired(min, required)
    for i in range(0, rd.randrange(min, max)): # number of words to be inserted
        elem = rd(textlist, weight, required)
        res.append(elem)
        textlist.remove(elem)
    return utils.listToStrWithSeparator(res, separator)

mailProvider = {
    "yahoo": ["fr", "com"],
    "gmail": ["com"],
    "outlook": ["fr", "com"],
    "laposte": ["net"],
    "gmx": ["fr", "com"],
    "icloud": ["com"],
    "orange": ["fr"],
    "bbox": ["fr"],
    "sfr": ["fr"]
}

lastname = [
    "Petrou",
    "Verna",
    "Dupont"
]

firstname = [
    "gregoire",
    "nathan",
    "anthony"
]

initial = "abcdefgjlmnoprst"

def email():
    domain = rd.choice(mailProvider.keys())
    tld = rd.choice(mailProvider[domain])
    address = '@' + str(domain) + '.' + str(tld)
    first = rd.choice(firstname).lower()
    last = rd.choice(lastname).lower()
    choice = number(0, 4)
    if choice == 0:
        mail = first + '.' + last + address
    elif choice == 1:
        mail = last + '.' + first + address
    elif choice == 2:
        mail = first + last + address
    elif choice == 3:
        mail = first[0] + last + address
    elif choice == 4:
        mail = last + first[0] + address
    #utils.checkEmailList(mail)
    return mail
