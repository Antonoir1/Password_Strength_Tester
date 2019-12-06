import Hash
import time

def word(password, wordlist, TIME_LIMIT):
    print("Cracking...")
    has_found = False
    over_time = False
    start_time = time.clock()
    count = 0

    for i in range(0,len(wordlist)):
        tmp = Hash.convert_sha256(wordlist[i])
        count += 1
        if(tmp == password):
            has_found = True
            break
        if(time.clock()-start_time > TIME_LIMIT):
            over_time = True
            break
    if(has_found == True):
        print("PASSWORD FOUND in "+str(count)+" trials ("+str(time.clock()-TIME_LIMIT)+" seconds)\n")
    elif(over_time == True):
        print("PASSWORD NOT FOUND within The time limit of "+str(TIME_LIMIT)+" seconds after "+str(count)+" trials\n" )
    else:
        print("PASSWORD NOT FOUND in "+str(count)+" trials ("+str(time.clock()-TIME_LIMIT)+" seconds)\n")