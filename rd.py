import random

def rd(choice, weight=[100], required=True):
    ''' Return random value in provided list.
    By default, if the default weight is [100] or if not any weight provided, it will the chance of outcome equally for each choice:
    ex: rd(['A', 'B', 'C']) => 100% / 3 => weight = ['33', '33', '33']
    ex: rd(['A', 'B', 'C', 'D']) => 100% / 4 =>  weight = ['25', '25', '25', '25']

    The number of weight value need to match the same number of choice values provided, except if required is False, then you need to provide the non choice weight.

    ex: rd(['A', 'B'], [60, 40], True) => Correct: the question is required, so 60% for A and 40% for B
    ex: rd(['A', 'B'], [50, 40], True) => Incorrect: since the sum of the weight is below 98%
    ex: rd(['A', 'B'], [50, 50], False) => Incorrect: the question is not required, so the none choice is enabled and you need to provide it's weight
    ex: rd(['A', 'B'], [30, 50, 20], False) => Correct: 30% for A, 50% for B, 20% for the none choice
    ex: rd(['A', 'B'], [100], False) => Correct: 33% for A, 33% for B, 33% for the none choice
    ex: rd(['A', 'B'], [100], True) => Correct: 50% for A, 50% for B and no none choice since it's a required question

    The sum of amount need to be around 100% (with a tolerance for about +/- 2% for rounded values)
    Weight values are rounded up, so it doesn't matter if you add the exact decimals or not.
    '''
    if not required: # add the none choice if not required
        choice.append("")
    print(choice, len(choice), len(weight))
    weight = [int(round(x)) for x in weight] # rounded up if floats
    if sum(weight) <= 98 or sum(weight) > 102:
        print("Error: Need 100% weight. (with +/- 2% if not rounded)")
        exit(1)
    if len(choice) != len(weight) and weight == [100]: # if weight not set (by default setted at 100)
        percent = 100 / len(choice) # dividing 100 by nb of elements in choice
        weight = [percent for i in range(len(choice))] # set same weight for all choices
    elif len(choice) != len(weight) and not required:
        print("Error: Choice and weight lists doesn't contains the same numbers of elements")
        print("Don't forget to add the percentage for the none choice at the end.")
        print("The none choice is enabled since it's a 'not required' question")
        exit(1)
    elif len(choice) != len(weight):
        print("Error: Choice and weight lists doesn't contains the same numbers of elements")
        exit(1)
    res = []
    for i in choice: # filling up the list : choice[0] * weight[0] + choice[1] * weight[1]...
        for j in range(weight[choice.index(i)]):
            res.append(i)
    return random.choice(res)
