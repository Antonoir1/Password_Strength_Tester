import time
import numpy as np
import math
import Hash

#Tries to find a password with it Hash(min/max: minimum/maximum size of the password, alphabet: characters used to guess the password, TIME_LIMIT: in seconds)
def brute_force(password, min, max, aplhabet, TIME_LIMIT):
    print("Cracking...")
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
                if(values[0] != len(aplhabet)-1):
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

    end_time = time.clock()-start_time
    if(has_found == True):
        print("PASSWORD FOUND in "+str(trials)+" trials ("+str(end_time)+" seconds)\n" )
        return [True, end_time]
    elif(time.clock()-start_time >= TIME_LIMIT):
        print("PASSWORD NOT FOUND within The time limit of "+str(TIME_LIMIT)+" seconds after "+str(trials)+" trials\n" )
        return [False, TIME_LIMIT]
    else:
        print("PASSWORD NOT FOUND in "+str(trials)+" trials ("+str(end_time)+" seconds)\n")
        return [False, end_time]


def fast(password, alphabet, TIME_LIMIT, max_length):
    has_found = False
    alpha_found = []
    found = []
    crack_count = 0
    min_length = 1
    time_limit = int(TIME_LIMIT)
    combin_values = [] #Combination array of the characters arrayS 
    refl = [ j for j in range(0,len(alphabet))]
    for i in range(0,len(alphabet)):
        combin_values.append([])
        for j in range(0,len(alphabet)):
            combin_values[i].append([])
    for i in range(0,len(alphabet)):
        combin_values[0][i].append([refl[i]])

    #Fill the combination array with every combination possible (except between the same characters array)
    z = 1
    for i in range(1,len(combin_values)):
        for j in range(z,len(combin_values[0])):
            for m in range(0,j):
                if(len(combin_values[i-1][m]) != 0):
                    for n in range(0, len(combin_values[i-1][m])):
                        tmp = combin_values[i-1][m][n][:]
                        tmp.append(refl[j])
                        combin_values[i][j].append(tmp)
        z += 1

    #Go through the all the combination possible and use them to try to crack the password as fast as possible
    for i in range(0, len(combin_values)):
        for j in range(0,len(combin_values[0])):
            if(len(combin_values[i][j]) != 0):
                for k in range(0,len(combin_values[i][j])):
                    alphabet_tmp = np.array([])
                    for l in range(0,len(combin_values[i][j][k])):
                        alphabet_tmp = np.concatenate([alphabet_tmp, alphabet[combin_values[i][j][k][l]]])
                    found = brute_force(password, min_length, max_length, alphabet_tmp, time_limit)
                    crack_count += 1
                    has_found = found[0]
                    if(has_found == True):
                        alpha_found = alphabet_tmp
                        break
                if(has_found == True):
                    break
        if(has_found == True):
            break
    if(has_found == True):
        print("The password was cracked in "+str(found[1])+" seconds with the following character combination: "+("".join(alphabet_tmp)))
    else:
        print("The password wasn't cracked with the "+str(time_limit)+" seconds time limit")

def simple(password, aplhabet, TIME_LIMIT, max_length):
    has_found = []
    min_length = 1

    alphabet_tmp = np.array([])
    for i in range(0,len(aplhabet)):
        alphabet_tmp = np.concatenate([alphabet_tmp, aplhabet[i]])

    has_found = brute_force(password, min_length, max_length, alphabet_tmp, TIME_LIMIT)
    if(has_found[0] == True):
        print("The password was cracked in "+str(has_found[1])+" seconds")
    else:
        print("The password wasn't cracked with the "+str(TIME_LIMIT)+" seconds time limit")