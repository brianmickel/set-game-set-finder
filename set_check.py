import math
from itertools import combinations
#input a board of cards
#output whether or not a set exists
"""
representing cards
    four digit number where
    +-------+-------+--------+------+
    | color | shape | number | fill |
    +-------+-------+--------+------+

    Color:
    1 - Green
    2 - Purple
    3 - Red

    Shape:
    1 - diamond
    2 - oval
    3 - S-shape

    number:
    1 - one
    2 - two
    3 - three

    fill:
    1 - empty
    2 - lined
    3 - solid

    ---
    15 nPr 3 = 2730
    18 nPr 3 = 4896

"""


#def generate_possibilities():
    #all combinations of 3 of 4 digits 123 numbers
    # (3*3*3*3)*(3^4)*(3^4) = 531,441
    #decided not to go down this route - too much spin up time

# THIS IS SHIT BUT LUCKILY COMPUTERS ARE FAST TO MAKE THIS NOT SLOW
#Idea
#code every card in the current group
# start with each card 1 -> 15
    # pair it with each other card i => 15
        # triple it with each other card j => 15
            #check if set (add to list of sets)

def allSame(card1, card2, card3, idx):
    return ( str(card1)[idx]==str(card2)[idx] and str(card2)[idx]==str(card3)[idx] )

def allDiff(card1, card2, card3, idx):
    return (sorted( [str(card1)[idx],str(card2)[idx],str(card3)[idx]]) == ['1','2','3'] )

#check length of list of sets
def allSameOrDiff(card1, card2, card3):
    for i in [0,1,2,3]:
        if not (allDiff(card1, card2, card3, i) or allSame(card1, card2, card3, i)):
            # this property is all same or all different
            return False
    return True

mapColor = {
    "g":1,
    "p":2,
    "r":3
}
mapShape = {
    "d":1,
    "o":2,
    "s":3
}
mapNumber = {
    "1":1,
    "2":2,
    "3":3
}
mapFill = {
    "e":1,
    "l":2,
    "s":3
}
###
mapColorBack = {
    1:'g',
    2:'p',
    3:'r'
}
mapShapeBack = {
    1:'d',
    2:'o',
    3:'s'
}
mapNumberBack = {
    1:'1',
    2:'2',
    3:'3'
}
mapFillBack = {
    1:'e',
    2:'l',
    3:'s'
}

def mapTextToNumber(text):
    a = mapColor[text[0]] * int(math.pow(10,3))
    #print(a)
    b = mapShape[text[1]] * int(math.pow(10,2))
    #print(b)
    c = mapNumber[text[2]] * int(math.pow(10,1))
    #print(c)
    d = mapFill[text[3]] * int(math.pow(10,0))
    #print(d)
    return (a + b + c + d)

def mapNumberToText(number):
    a = mapColorBack[int(str(number)[0])]
    #print(a)
    b = mapShapeBack[int(str(number)[1])]
    #print(b)
    c = mapNumberBack[int(str(number)[2])]
    #print(c)
    d = mapFillBack[int(str(number)[3])]
    #print(d)
    return a + b + c + d

def listToListOfCards(inputList):
    listOfCards = []
    for ele in inputList:
        listOfCards.append(mapTextToNumber(ele))
    return listOfCards
"""
#this bugs out because it can find the same set multiple times
def checkSets(listOfCards):
    aSetExists = False
    setList =[]
    for i, val_i in enumerate(listOfCards[:(len(listOfCards)-2)]):
        for j, val_j in enumerate(listOfCards[i+1:(len(listOfCards)-1)]):
            for k, val_k in enumerate(listOfCards[j+1:]):
                if ( allSameOrDiff(val_i, val_j, val_k) ):
                    aSetExists = True
                    print("set found:%s,%s,%s" % (mapNumberToText(val_i), mapNumberToText(val_j), mapNumberToText(val_k)) )
                    setList.append([mapNumberToText(val_i), mapNumberToText(val_j), mapNumberToText(val_k)])
    return {'setExistance': aSetExists, 'setList': setList}
    """

def checkSets(listOfCards):
    aSetExists = False
    setList = []
    combinationsOfCards = list(combinations(listOfCards, 3))
    # print(combinationsOfCards)
    for possibleSet in combinationsOfCards:
        val_i = possibleSet[0];
        val_j = possibleSet[1];
        val_k = possibleSet[2];
        if ( allSameOrDiff(val_i, val_j, val_k) ):
            aSetExists = True
            print("set found:%s,%s,%s" % (mapNumberToText(val_i), mapNumberToText(val_j), mapNumberToText(val_k)) )
            setList.append([mapNumberToText(val_i), mapNumberToText(val_j), mapNumberToText(val_k)])
    return {'setExistance': aSetExists, 'setList': setList}


def set_check(inputList):
    cardList = listToListOfCards(inputList)
    #print(cardList)
    return checkSets(cardList)


#  color,    shape,   number,   fill
#  (g|p|r)  (d|o|s)  (1|2|3)  (e|l|s)