import editdistance
import string
import random 



#define necessary functions
#---------------------------
#---------------------------

def find_consecutive_chars(pw):
    count = 0
    prev_char = None
    result = []

    for char in pw:
        if char == prev_char:
            count += 1
        else:
            if count > 0:
                result.append(count+1)
            count = 0
        prev_char = char

    if count > 0:
        result.append(count+1)

    prop_consecutive = sum(result)/len(pw)
    
    return prop_consecutive

#create a random password
def random_pw(len_min = 1,
             len_max = 1, 
             uppercase = True,
             lowercase = False,
             numbers = False,
             special = False,
             cut_I_and_l = True,
             cut_O_and_0 =True):
    
    
    #password complexity:
    complexity = ''
    
    if uppercase == True: 
        complexity += string.ascii_uppercase
    if lowercase == True:
        complexity += string.ascii_lowercase
    if numbers == True:
        complexity += string.digits
    if special == True: 
        complexity += '!"§$%&/()=?'
    if cut_I_and_l == True:
        complexity = complexity.replace("I", "")
        complexity = complexity.replace("l", "")
        complexity = complexity.replace("1", "")
    if cut_O_and_0 == True:
        complexity = complexity.replace("O", "")
        complexity = complexity.replace("0", "")
    
    
    #password length
    length = random.randint(len_min, len_max)

    pw = ''
    
    while length > len(pw):
        pw += complexity[random.randint(0, len(complexity)-1)]
    
    return pw

#find the closest distance between the created password and a list password from a list of passwords 
def closest_distance(pw, ls):
    
    ls_dist = []
    for i in range(len(ls)):
        dist = editdistance.eval(pw, ls[i])
        ls_dist.append(dist)
    
    return ls_dist
