import time, math, os
from multiprocessing import Pool, freeze_support
import Speed

import numpy as np
import Hash

#CHECK IF EACH VALUE HAS BEEN TRIED
def Check_isfinished(tab,limit):
    for i in tab:
        if i != limit:
            return False
    return True

#PROCESS BRUTE-FORCE FOR ONE PASSWORD LENGTH
def subWorker(password, aplhabet, plain, values, start_time, TIME_LIMIT):
    has_found = False
    trials = 1
    while(Check_isfinished(values,len(aplhabet)) == False  and time.perf_counter()-start_time < TIME_LIMIT):
        if(values[-1] == len(aplhabet)):
            tmp_index = len(values)-1
            while(values[tmp_index-1] == len(aplhabet) and tmp_index > 1):
                tmp_index -= 1
            #Check if every character combination was guessed 
            if(Check_isfinished(values,len(aplhabet)) == False):
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
    end_time = time.perf_counter()-start_time
    if(has_found == True):
        return [True, end_time, trials]
    else:
        return [False, end_time, trials]


#USE BRUTE-FORCE ATTACKS FOR EACH PASSWORD LENGTH
def brute_force(password, min, max, aplhabet, TIME_LIMIT):
    start_time = time.perf_counter()
    trials = 0

    for i in range(min-1, max):
        outputs = subWorker(password,aplhabet, [aplhabet[0] for a in range(0,i+1)], np.ones(i+1, dtype=int),  start_time, TIME_LIMIT)
        trials += outputs[2]
        if(outputs[0] == True):
            return [True, time.perf_counter()-start_time, trials]
        if(time.perf_counter()-start_time > TIME_LIMIT):
            return [False, TIME_LIMIT, trials]

#CALL THE BRUTE-FORCE ATTACKS AND CHECK IT RESULT
def simple(password, aplhabet, TIME_LIMIT, max_length):
    has_found = []

    alphabet_tmp = np.array([])
    for i in range(0,len(aplhabet)):
        alphabet_tmp = np.concatenate([alphabet_tmp, aplhabet[i]])

    has_found = brute_force(password, 1, max_length, alphabet_tmp, TIME_LIMIT)
    if(has_found[0] == True):
        return "PASSWORD FOUND in "+str(has_found[2])+" trials ("+Speed.display_time(has_found[1])+")"
    else:
        return "PASSWORD NOT FOUND within The time limit of "+str(TIME_LIMIT)+" seconds after "+str(has_found[2])+" trials"


#RETURN THE TIME TAKEN TO TRY EACH HASH
def getTime(aplhabet):
    TIME_LIMIT = 1000
    start_time = time.perf_counter()
    values = np.ones(3, dtype=int)
    plain = [aplhabet[0] for a in range(0,3)]

    subWorker("", aplhabet, plain, values, start_time, TIME_LIMIT)
    end_time = time.perf_counter()-start_time
    return end_time

