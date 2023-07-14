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
def random_pw(len_min = 4,
             len_max = 4, 
             uppercase = True,
             lowercase = False,
             numbers = False,
             special = False,
             cut_I_and_l = True,
             cut_O_and_0 =True):
    
    
    #password complexity:
    complexity = ''
    lowercase_ls = ''
    uppercase_ls = ''
    numbers_ls = ''
    special_ls = ''

    if uppercase == True: 
        uppercase_ls = string.ascii_uppercase 
        complexity += string.ascii_uppercase
    if lowercase == True:
        lowercase_ls = string.ascii_lowercase 
        complexity += string.ascii_lowercase
    if numbers == True:
        numbers_ls = string.digits
        complexity += string.digits
    if special == True:
        special_ls = '!"§$%&/()?' #no equal sign will be provided or else Excel will do weird things to your password list. 
        complexity += '!"§$%&/()?'
    if cut_I_and_l == True:
        complexity = complexity.replace("I", "")
        complexity = complexity.replace("l", "")
        complexity = complexity.replace("1", "")
        uppercase_ls = uppercase_ls.replace("I", "")
        lowercase_ls = lowercase_ls.replace("l", "")
        numbers_ls = numbers_ls.replace("1", "")
    if cut_O_and_0 == True:
        complexity = complexity.replace("O", "")
        complexity = complexity.replace("0", "")
        uppercase_ls = uppercase_ls.replace("O", "")
        numbers_ls = numbers_ls.replace("0", "")
    
    
    #password length
    length = random.randint(len_min, len_max)

    a = random.choice(uppercase_ls) if uppercase == True else random.choice(complexity)
    b = random.choice(lowercase_ls) if lowercase == True else random.choice(complexity)
    c = random.choice(numbers_ls) if numbers == True else random.choice(complexity)
    d = random.choice(special_ls) if special == True else random.choice(complexity)

    pw = a+b+c+d
    
    while length > len(pw):
        pw += random.choice(complexity)
    
    #print(pw)

    #shuffle the letters in the password
    pw = ''.join(random.sample(pw, len(pw)))
    #print(pw)


    return pw

#find the closest distance between the created password and a list password from a list of passwords 
def closest_distance(pw, ls):
    
    ls_dist = []
    for i in range(len(ls)):
        dist = editdistance.eval(pw, ls[i])
        ls_dist.append(dist)
    
    return ls_dist
