#zczytywanie wartości z pliku
def elfInput(fileTitle):
    with open(fileTitle) as ha:
        lines = ha.readlines()
    ha.close()
    print(lines[3])
    return lines

#dodawanie kalorii z listy
def addCalories(calLines):
    elfList = []
    x = 0
    for oneLine in calLines:
        if oneLine == "\n":
            x = x + 1
        else:
            if len(elfList) == (x + 1):
                elfList[x] = elfList[x] + int(oneLine) 
            else:
                elfList.append(int(oneLine))
    return elfList

#szukanie najwyższej wartości
def highestCal(caloriesList):
    caloriesList.sort()
    print("Elf that carries the most calories, carries", caloriesList[-1], " calories.")
    top3 = caloriesList[-1] + caloriesList[-2] + caloriesList[-3]
    print("Top three Elves carrying the most Calories, carries ", top3, " calories.")
    
#main
caloryLines = elfInput("input.txt")
listOfElves = addCalories(caloryLines)
highestCal(listOfElves)




