#1 for Rock, 2 for Paper, and 3 for Scissors
def input_additon(x):
    if x[2] == 'X':
        points = 0
        if x[0] == 'A':
            return points + 3
        elif x[0] == 'B':
            return points + 1
        elif x[0] == 'C':
            return points + 2
    
    elif x[2] == 'Y':
        points = 3
        if x[0] == 'A':
            return points + 1
        
        elif x[0] == 'B':
            return points + 2
        
        elif x[0] == 'C':
            return points + 3
    
    elif x[2] == 'Z':
        points = 6
        if x[0] == 'A':
            return points + 2
        
        elif x[0] == 'B':
            return points + 3
        
        elif x[0] == 'C':
            return points + 1
        
    
def loop_addition(filehandler):
    counter = 0
    for line in filehandler:
        result = input_additon(line)
        print(result)
        counter = counter + result
    print(counter)
    


with open("input") as f:
    loop_addition(f)
f.close()
    
    
        


