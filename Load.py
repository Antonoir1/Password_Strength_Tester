import os
import numpy as np

#CHARACTERS CLASS
ALPHA = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
BETA = np.array(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
DELTA = np.array(["0","1","2","3","4","5","6","7","8","9"])
TETA = np.array(["{","}","(",")","[","]","#","~","&","\"","\'","-","|","`","_","\\","^","@","=","+","$","%","*","!",":",";",",","?",".","/"," ","<",">"])
PRIMORDIAL = np.array([ALPHA, BETA, DELTA, TETA])

def load_Wordlist(path):
    wordlist = np.array([])
    list_dir = os.listdir(path)
    for i in list_dir:
        words = open(path+i, "r")
        wordlist = np.concatenate([wordlist, words.readlines()])
        words.close()
    for i in range(0,len(wordlist)):
        if(i < len(wordlist)-1 ):
            wordlist[i] = wordlist[i][:len(wordlist[i])-1]
    return wordlist

def get_Characters():
    return PRIMORDIAL