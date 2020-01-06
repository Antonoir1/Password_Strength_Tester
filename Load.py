import os
import numpy as np

#CHARACTERS
ALPHA = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
BETA = np.array(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
DELTA = np.array(["0","1","2","3","4","5","6","7","8","9"])
TETA = np.array(["{","}","(",")","[","]","#","~","&","\"","\'","-","|","`","_","\\","^","@","=","+","$","%","*","!",":",";",",","?",".","/"," ","<",">"])
PRIMORDIAL = np.array([ALPHA, BETA, DELTA, TETA])

#LOAD THE WORD LIST
def load_Wordlist(path):
    if(os.path.exists(path) == False):
        os.mkdir("./passwords")
        return np.array([])
    wordlist = np.array([])
    list_dir = os.listdir(path)
    has_found = False
    for i in list_dir:
        if(".txt" in i):
            has_found = True
            words = open(path+"/"+i, "r")
            wordlist = np.concatenate([wordlist, words.readlines()])
            words.close()
    if(has_found == False):
        return np.array([])
    for i in range(0,len(wordlist)):
        if("\n" in wordlist[i]):
            wordlist[i] = wordlist[i][:len(wordlist[i])-1]
        if(wordlist[i] == ""):
            wordlist = np.delete(wordlist, i)
    return np.unique(wordlist)

#LOAD THE LIST OF CHARACTERS
def get_Characters():
    return PRIMORDIAL