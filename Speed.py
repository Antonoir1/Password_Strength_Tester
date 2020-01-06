import BruteForce, Dictionary
import numpy as np
import math, os


#CONVERT TIME DURACTION (SECONDS) INTO A STRING
def display_time(seconds, granularity=5):
    if(seconds < 1):
        return str(seconds)+" second"
    seconds_tmp = seconds
    seconds = int(seconds)
    intervals = (
    ('years', 31536000),
    ('days', 86400),
    ('hours', 3600),
    ('minutes', 60),
    ('seconds', 1),
    )
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            if("second" in name):
                result.append("{} {}".format(value+seconds_tmp%1, name))
            else:
                result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

#GET THE COMPUTATION SPEED OF THE COMPUTER
def Check(password, alphabet, wordlist):

    #DICTIONARY
    wordtmp = ["test" for i in range(0,100000)]
    time_word = Dictionary.getTime(wordtmp)

    #BRUTE-FORCE
    full = np.array([])
    for i in range(0,len(alphabet)):
        full = np.concatenate([full, alphabet[i]])
    time_simple = (BruteForce.getTime(full)/(math.pow(len(full),3)))


    if(len(password) > 0):
        #BRUTE-FORCE
        simple_trials = 1
        for i in range(1,len(password)):
            simple_trials += math.pow(len(full),i)
        for i in range(0,len(password)):
            simple_trials += (np.where(full == password[i])[0][0])*(pow(len(full),len(password)-1-i))
        simple_t = simple_trials*time_simple

        if(len(wordlist) > 0):
            
            #DICTIONARY
            word_trials = 0
            if(password in wordlist):
                word_trials = np.where(wordlist == password)[0][0] +1
            else:
                word_trials = len(wordlist)
            word_t = word_trials*time_word

            if(password in wordlist):
                return "Brute-Force: "+str(time_simple)+" seconds/Hash, found after "+str(int(simple_trials))+" trials and "+display_time(simple_t)+"\nDictionary: "+str(time_word)+" seconds/Hash, found after "+str(int(word_trials))+" trials and "+display_time(word_t)
            else:
                return "Brute-Force: "+str(time_simple)+" seconds/Hash, found after "+str(int(simple_trials))+" trials and "+display_time(simple_t)+"\nDictionary: "+str(time_word)+" seconds/Hash, not found after "+str(int(word_trials))+" trials and "+display_time(word_t)
        else:
            return "Brute-Force: "+str(time_simple)+" seconds/Hash, found after "+str(int(simple_trials))+" trials and "+display_time(simple_t)+"\nDictionary: "+str(time_word)+" seconds/Hash, NO .txt FILES WERE FOUND IN "+str(os.getcwd())+"\\passwords"
                
    else:
        if(len(wordlist) > 0):
            return "Brute-Force: "+str(time_simple)+" seconds/Hash, NO PASSWORD ENTERED\nDictionary: "+str(time_word)+" seconds/Hash, NO PASSWORD ENTERED"
        else:
            return "Brute-Force: "+str(time_simple)+" seconds/Hash, NO PASSWORD ENTERED\nDictionary: "+str(time_word)+" seconds/Hash, NO PASSWORD ENTERED AND NO .txt FILES WERE FOUND IN "+str(os.getcwd())+"\\passwords"