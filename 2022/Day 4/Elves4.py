
#constants
DISTRICT_DATA = { "first_person_min" : [],
                 "first_person_max" : [], 
                 "second_person_min" : [], 
                 "second_person_max" : []
}
DISTRICT_RANGE = {"first_elf_range" : [],
                  "second_elf_range" : []
}

# functions
def input_read():
    with open('input.txt') as file_h:
        lines = file_h.readlines()
        elves_data = DISTRICT_DATA
    elves_data_list = []
    for y in lines:
        elf_flag = 0
        elves_data["first_person_min"] = []
        elves_data["first_person_max"] = []
        elves_data["second_person_min"] = []
        elves_data["second_person_max"] = []
        for x in y:
            if(x.isnumeric()):
                if(elf_flag == 0):
                    elves_data["first_person_min"].append(x)
                
                elif(elf_flag == 1):
                    elves_data["first_person_max"].append(x)
            
                elif(elf_flag == 2):
                    elves_data["second_person_min"].append(x)
                
                elif(elf_flag == 3):
                    elves_data["second_person_max"].append(x)
            else:
                elf_flag = elf_flag + 1
        el_of_list = (make_int_dict(elves_data))
        elves_data_list.append(el_of_list.copy())
    return(elves_data_list)
       
def fully_contains_chceck(list1, list2):
    flag = False
    if(len(list1) > len(list2)):
        long_list = list1
        short_list = list2
    else:
        long_list = list2
        short_list = list1
        
    for sh_list_element in short_list:#234  12345
        if(sh_list_element in long_list):
            flag = True
            break
        else:
            flag = False
            
    return flag

def make_int_dict(x_dict):
    new_dict = DISTRICT_DATA
    
    temp = "".join(x_dict["first_person_min"])
    new_dict["first_person_min"] = int(temp)
    
    temp = "".join(x_dict["first_person_max"])
    new_dict["first_person_max"] = int(temp)
    
    temp = "".join(x_dict["second_person_min"])
    new_dict["second_person_min"] = int(temp)
    
    temp = "".join(x_dict["second_person_max"])
    new_dict["second_person_max"] = int(temp)
    
    return new_dict
     
def contains_number(y_dict_list):
    range_list = []
    range_dict = DISTRICT_RANGE
    for temp in y_dict_list:
        range_dict["first_elf_range"] = []
        range_dict["first_elf_range"] = [*range(temp["first_person_min"],temp["first_person_max"] + 1 )]
        range_dict["second_elf_range"] = []
        range_dict["second_elf_range"] = [*range(temp["second_person_min"],temp["second_person_max"] + 1 )]
        range_list.append(range_dict.copy())
    return range_list

def how_many_pair(z_range_list):
    counter = 0
    for x in z_range_list:
        z1 = x["first_elf_range"]
        z2 = x["second_elf_range"]
        if (fully_contains_chceck(z1,z2) == True):
            counter = counter + 1
    return counter
        
#main
numbers_of_range = contains_number(input_read())
print(how_many_pair(numbers_of_range))

