import textwrap, string 
with open ('input.txt') as f:
    lines = f.readlines()
    f.close()
 
def calculate_priority():
    priority_values = {}
   
    low_alphabet = string.ascii_lowercase
    up_alphabet = string.ascii_uppercase
    number = 1
    
    for x in low_alphabet:
        priority_values[x] = number
        number = number + 1
        
    for y in up_alphabet:
        priority_values[y] = number
        number = number + 1
    
    return priority_values
    
def component_cutter(text):
    text_length = int(len(text.strip()) / 2)
    cut_text = textwrap.wrap(text, int(text_length))
    return cut_text

def shared_char(text_after_cut):
    shared_list = []
    if(len(text_after_cut)) == 2:
        for x in text_after_cut[0]:
            if x in text_after_cut[1]:
                shared_list.append(x)
    return shared_list

def shared_in_three(m1, m2, m3):
    for temp in m1:
        if(temp in m2 and temp in m3):
            return temp
          
def trinity_group(some_list):
    #if a is in x and in z
    list_of_trinity = []
    counter = 0
    member0 = []
    member1 = []
    member2 = []
    for a in some_list:
        if counter == 0:
            member0 = a
            counter = 1
        elif counter == 1:
            member1 = a
            counter = 2
        elif counter == 2:
            member2 = a
            member_of_trinity = shared_in_three(member0, member1, member2)
            list_of_trinity.append(member_of_trinity)
            counter = 0
    return list_of_trinity

        
    
calc_prio = calculate_priority()
sum_of_priorities = 0
for z in lines:
    divided_text = component_cutter(z)
    element_priority = calc_prio[shared_char(divided_text)[0]]
    sum_of_priorities = sum_of_priorities + element_priority

sum_of_trinities = 0 
for z1 in trinity_group(lines):
    sum_of_trinities = sum_of_trinities + calc_prio[z1]
print(sum_of_trinities)
    
    
    
    

