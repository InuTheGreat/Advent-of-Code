def checkDigit(fileX):  #sprawdza, czy znak jest cyfrą
    print(fileX)
    digitList = []
    for x in fileX:
        if x.isdigit():
            digitList.append(x)
    return digitList

def firstLast(numString): #wyszukuje pierwszą i ostatnią cyfrę
    freshString = []
    freshString.append(numString[0])
    freshString.append(numString[-1])
    print(numString)
    print(freshString,'\n')
    return freshString

def intoInt(numString): #zamienia listę cyfr na liczbę
    newNumString = int("".join(numString))
    return newNumString

def addition(numbers): #dodawanie liczb z listy
    result = 0
    for x in numbers:
        result = result + x
    return result

#sprawdzanie czy ciąg znaków opisuje liczbę
def letterDigitToInt(someString):
    print(someString)
    digitDict = {
        'one' : -1,
        'two' : -1,
        'three': -1,
        'four' : -1,
        'five' : -1,
        'six' : -1,
        'seven' : -1,
        'eight' : -1,
        'nine' :-1
    }
    for keyX in digitDict:
        digitDict.update({keyX: someString.find(keyX)})
    print(digitDict)
    CopyDigitDict = digitDict.copy()
    for keyX, itemX in digitDict.items():
        if itemX<0:
            CopyDigitDict.pop(keyX)
    if bool(CopyDigitDict) == True:
        newString = turnLetterIntoDigit(someString, CopyDigitDict)
        return newString
    else:
        return someString

#zamiana ciągu znaku na liczbę
def turnLetterIntoDigit(someString, someDict):
    digitTable = {
        'one' : '1',
        'two' : '2',
        'three': '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' :'9'
    }
    
    if max(someDict.values()) == min(someDict.values()):
        newString = someString.replace((min(someDict, key=someDict.get)), digitTable[min(someDict, key=someDict.get)])
        return newString
    else:
        newString = someString.replace((min(someDict, key=someDict.get)), digitTable[min(someDict, key=someDict.get)])
        newString = newString.replace((max(someDict, key=someDict.get)), digitTable[max(someDict, key=someDict.get)])
        return newString
    
    
    
with open('input.txt')as f:
    text = f.readlines()


print(letterDigitToInt(text[996]))
with open('SuperText.txt','w') as nf:
    nf.write('')
for x in text:
    with open('superText.txt', 'a') as nf:
        nf.write(letterDigitToInt(x))    

with open('SuperText.txt') as nf:
    text2 = nf.readlines()
    

listOfNumbers = []
for y in text2:
    listOfNumbers.append(intoInt(firstLast(checkDigit(y))))
    print(addition(listOfNumbers))


