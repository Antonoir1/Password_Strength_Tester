import Hash
import Speed
import time

#CRACK THE PASSWORD WITH DICTIONARY ATTACKS
def word(password, wordlist, TIME_LIMIT):
    has_found = False
    over_time = False
    start_time = time.perf_counter()
    count = 0

    for i in range(0,len(wordlist)):
        tmp = Hash.convert_sha256(wordlist[i])
        count += 1
        if(tmp == password):
            has_found = True
            break
        if(time.perf_counter()-start_time > TIME_LIMIT):
            over_time = True
            break
    if(has_found == True):
        return "PASSWORD FOUND in "+str(count)+" trials ("+Speed.display_time(time.perf_counter()-start_time)+")"
    elif(over_time == True):
        return "PASSWORD NOT FOUND within The time limit of "+str(TIME_LIMIT)+" seconds after "+str(count)+" trials"
    else:
        return "PASSWORD NOT FOUND in "+str(count)+" trials ("+Speed.display_time(time.perf_counter()-start_time)+")"

#RETURN THE TIME TAKEN TO TRY EACH HASH
def getTime(wordlist):
    TIME_LIMIT = 10000000
    password = "none"
    has_found = False
    over_time = False
    start_time = time.perf_counter()
    count = 0

    for i in range(0,len(wordlist)):
        tmp = Hash.convert_sha256(wordlist[i])
        count += 1
        if(tmp == password):
            has_found = True
            break
        if((time.perf_counter()-start_time) > TIME_LIMIT):
            over_time = True
            break

    return (time.perf_counter()-start_time)/len(wordlist)