import time
import numpy as np
import math
import Hash

#FISRT SECURITY LEVEL
ALPHA = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
BETA = np.array(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
DELTA = np.array(["0","1","2","3","4","5","6","7","8","9"])
TETA = np.array(["{","}","(",")","[","]","#","~","&","\"","\'","-","|","`","_","\\","^","@","=","+","$","%","*","!",":",";",",","?",".","/"," ","<",">"])

PRIMORDIAL = np.array([ALPHA, BETA, DELTA, TETA])

#SECOND SECURITY LEVEL
SYMBOLS = np.concatenate([DELTA, TETA])
LETTERS = np.concatenate([ALPHA, BETA])
LETTERS_NUMBERS_L = np.concatenate([ALPHA, DELTA])
LETTERS_NUMBERS_U = np.concatenate([BETA, DELTA])

#THIRD SECURITY LEVEL
LETTERS_NUMBERS = np.concatenate([LETTERS, DELTA])

#FOURTH SECURITY LEVEL
CHARACTERS = np.concatenate([LETTERS_NUMBERS, TETA])

#Tries to find a password with it Hash(min/max: minimum/maximum size of the password, alphabet: characters used to guess the password, TIME_LIMIT: in seconds)
def brute_force(password, min, max, aplhabet, TIME_LIMIT):
    start_time = time.clock()
    trials = 1
    values = np.ones(min, dtype=int)
    plain = [aplhabet[0] for a in range(0,min)]
    has_found = False

    #Loop for each password length
    for i in range(min-1,max):
        if(Hash.convert_sha256("".join(plain)) == password):
            has_found = True
            break
        
        while(values[0] != len(aplhabet) and time.clock()-start_time < TIME_LIMIT):
            if(values[-1] == len(aplhabet)):
                tmp_index = len(values)-1
                while(values[tmp_index-1] == len(aplhabet) and tmp_index > 1):
                    tmp_index -= 1
                #Check if every character combination was guessed 
                if(values[0] != len(aplhabet)):
                    values[tmp_index:len(values)] = 1
                    plain[tmp_index:len(values)] = [aplhabet[0] for i in range(tmp_index,len(values))]

                values[tmp_index-1] += 1
                plain[tmp_index-1] = aplhabet[values[tmp_index-1]-1]
                trials += 1
                if(Hash.convert_sha256("".join(plain)) == password):
                    has_found = True
                    break
            else:
                values[-1] += 1
                plain[-1] = aplhabet[values[-1]-1]
                trials += 1
                if(Hash.convert_sha256("".join(plain)) == password):
                    has_found = True
                    break
        if(has_found == True or time.clock()-start_time >= TIME_LIMIT):
            break
        values = np.ones(len(values)+1, dtype=int)
        plain = []
        for k in range(0,len(values)):
            plain.append(aplhabet[0])

    if(has_found == True):
        print("PASSWORD FOUND in "+str(trials)+" trials ("+str(time.clock()-start_time)+" seconds)\n" )
        #print("PASSWORD: "+"".join(plain))
        return -1
    elif(time.clock()-start_time >= TIME_LIMIT):
        print("TIMEOUT: The time limit of "+str(TIME_LIMIT)+" seconds has been reached after "+str(trials)+" trials\n" )
        return 1
    else:
        print("PASSWORD NOT FOUND in "+str(trials)+" trials ("+str(time.clock()-start_time)+" seconds)\n")
        return 1


#Estimate the maximum time taken
def speed(min, max, aplhabet):
    trials = 1
    values = np.ones(min, dtype=int)
    plain = [aplhabet[0] for a in range(0,min)]
    execution_time = time.clock()

    for i in range(0,1):
        if(Hash.convert_sha256("".join(plain)) == ""):
            break
        Q = 0
        while(Q < 9):
            Q += 1
            if(values[-1] == len(aplhabet)):
                tmp_index = len(values)-1
                while(values[tmp_index-1] == len(aplhabet) and tmp_index > 1):
                    tmp_index -= 1
                    
                if(values[0] != len(aplhabet)):
                    values[tmp_index:len(values)] = 1
                    plain[tmp_index:len(values)] = [aplhabet[0] for i in range(tmp_index,len(values))]

                values[tmp_index-1] += 1
                plain[tmp_index-1] = aplhabet[0]
                trials += 1
                if(Hash.convert_sha256("".join(plain)) == ""):
                    break
            else:
                values[-1] += 1
                plain[-1] = aplhabet[values[-1]-1]
                trials += 1
                if(Hash.convert_sha256("".join(plain)) == ""):
                    break
        values = np.ones(len(values)+1, dtype=int)
        plain = []
        for k in range(0,len(values)):
            plain.append(aplhabet[0])      
    total_time = (time.clock() - execution_time)
    num_of_combin = 0
    for k in range(min-1,max):
        num_of_combin += (math.pow(len(aplhabet),k+1))
    total_time *= num_of_combin
    return total_time/10
