# -*- coding: utf-8 -*-

import requests
import datetime
import time
import sys
from input import *
import config
from rd import *


def mainxxx():
    values_list = []
    values = {
    #"entry.2017728346": dropdown(3, True, ["list 1", "list 2", "list 3"]),
    "entry.1084809842": shortAnswer(1, 1, ["salut", "sa", "va"]),
    "entry.875771871": paragraph(1, 1, ["oui\naze", "et", "toi"]),
    #"entry.2108574651": multipleChoice(1, 1, ["cm 1", "cm 2", "cm 3"]),
    #"entry.429731579": checkboxes(1, 3, ["box 1", "box 2", "box 3"]),

    "entry.429731579": "box 2",
    "entry.429731579": "box 1",
    "entry.492970550_hour": 15,
    "entry.492970550_minute": 12,
    "entry.711423891_year": 2020,
    "entry.711423891_month": 11,
    "entry.711423891_day": 12
    }
    values_list.append(values)
    return values_list
    #values_list.append(values)
#print(rd(["A", "B", "C", "D"], [100], False))

#bruh%0D%0A%0D%0A%0D%0Aaze
#%0D%0A

def main():
    data = {
        #"entry.1084809842": shortAnswer(1, 1, ['''salut\nsava \r\n e%0D%0At toi''']),
        "entry.1084809842": rd(['salut', 'sa', 'va'], [90, 5, 5]),
        "entry.492970550_hour": number(0, 24),
        "entry.492970550_minute": number(0, 60),
        "entry.711423891_year": number(1990, 2000),
        "entry.711423891_month": number(1, 12),
        "entry.711423891_day": number(1, 31, False)
    }
    try:
        res = requests.post(config.url, data=data)
        print(res)
        print(data)
        if res.status_code == 400:
            print("Error: An entry number might be wrong")
        elif res.status_code == 404:
            print("Error: Invalid form URL")
        elif res.status_code != 200:
            print("Error: Unknown - GoogleForm returned code " + str(res.status_code))
    except:
        print("Error: Something went wrong")


main()
