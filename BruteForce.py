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
        return [True, end_time, trials]
    elif(time.clock()-start_time >= TIME_LIMIT):
        print("PASSWORD NOT FOUND within The time limit of "+str(TIME_LIMIT)+" seconds after "+str(trials)+" trials\n" )
        return [False, TIME_LIMIT, trials]
    else:
        print("PASSWORD NOT FOUND in "+str(trials)+" trials ("+str(end_time)+" seconds)\n")
        return [False, end_time, trials]

#Fast mode
def fast(password, alphabet, TIME_LIMIT, max_length):
    has_found = False
    alpha_found = []
    found = []
    crack_count = 0
    trials = 0
    time_used = 0
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
                    found = brute_force(password, max_length, max_length, alphabet_tmp, time_limit)
                    time_used += found[1]
                    trials += found[2]
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
        print("The password was cracked in "+str(trials)+" trials ("+str(time_used)+" seconds)\n")
    else:
        print("The password wasn't cracked within The time limit of "+str(TIME_LIMIT)+" seconds after "+str(trials)+" trials\n")

#Simple mode
def simple(password, aplhabet, TIME_LIMIT, max_length):
    has_found = []

    alphabet_tmp = np.array([])
    for i in range(0,len(aplhabet)):
        alphabet_tmp = np.concatenate([alphabet_tmp, aplhabet[i]])

    has_found = brute_force(password, max_length, max_length, alphabet_tmp, TIME_LIMIT)
    if(has_found[0] == True):
        print("The password was cracked in "+str(has_found[2])+" trials ("+str(has_found[1])+" seconds)\n")
    else:
        print("The password wasn't cracked within The time limit of "+str(TIME_LIMIT)+" seconds after "+str(has_found[2])+" trials\n")


#Get the computation time for len(alphabet)^3
def getTime(aplhabet):
    password = "0"
    min = 3
    max = 3
    TIME_LIMIT = 1000
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
    return end_time

#Check how much time it would take to crack a password
def Check(password, alphabet):
    #Simple
    full = np.array([])
    for i in range(0,len(alphabet)):
        full = np.concatenate([full, alphabet[i]])
    simple_trials = 1
    for i in range(0,len(password)):
        simple_trials += (np.where(full == password[i])[0][0])*(pow(len(full),len(password)-1-i))

    #Fast
    has_characters = [False for i in range(0,len(alphabet))]
    for i in range(0,len(alphabet)):
        for j in range(0,len(password)):
            if(password[j] in alphabet[i]):
                has_characters[i] = True
    values = []
    for i in range(0,len(has_characters)):
        if(has_characters[i] == True):
            values.append(i)
    
    fast_trials = 1
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
    #Go through each combination and get the number of trials
    is_done = False
    for i in range(0,len(combin_values)):
        for j in range(0,len(combin_values[i])):
            for k in range(0,len(combin_values[i][j])):
                has_found = True
                for z in range(0,len(values)):
                    if(values[z] not in combin_values[i][j][k]):
                        has_found = False
                alphabet_tmp = np.array([])
                for l in range(0,len(combin_values[i][j][k])):
                    alphabet_tmp = np.concatenate([alphabet_tmp, alphabet[combin_values[i][j][k][l]]])
                if(has_found == False):
                    fast_trials += math.pow(len(alphabet_tmp),len(password))
                else:
                    for w in range(0,len(password)):
                        fast_trials += (np.where(alphabet_tmp == password[i])[0][0])*(pow(len(alphabet_tmp),len(password)-1-w))
                    is_done = True
                    break
            if(is_done == True):
                break
        if(is_done == True):
            break
    print("Getting your computer computation speed...\n")
    time_simple = (getTime(full)/(math.pow(len(full),3)))
    print("In simple mode cracking this password would take "+str(simple_trials)+" trials and take approximately "+str(simple_trials*time_simple)+" seconds")
    print("In fast mode cracking this password would take "+str(fast_trials)+" trials and take approximately "+str(fast_trials*time_simple)+" seconds\n")
