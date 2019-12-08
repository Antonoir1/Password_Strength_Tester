import BruteForce, Dictionnary, Hash, Load
import sys
import numpy as np

if __name__ == "__main__":
    if(len(sys.argv) == 4):
        if(str.isdecimal(sys.argv[3])):
            if(str(sys.argv[1]) == "simple"):
                if(int(sys.argv[3]) > 0):
                    BruteForce.simple(Hash.convert_sha256(str(sys.argv[2])),Load.get_Characters(),int(sys.argv[3]), len(str(sys.argv[2])))
                else:
                    print("ERROR: TIME LIMIT MUST BE SUPERIOR TO 0")

            elif(str(sys.argv[1]) == "fast"):
                if(int(sys.argv[3]) > 0):
                    BruteForce.fast(Hash.convert_sha256(str(sys.argv[2])),Load.get_Characters(),int(sys.argv[3]), len(str(sys.argv[2])))
                else:
                    print("ERROR: TIME LIMIT MUST BE SUPERIOR TO 0")

            elif(str(sys.argv[1]) == "word"):
                if(int(sys.argv[3]) > 0):
                    Dictionnary.word(Hash.convert_sha256(str(sys.argv[2])), Load.load_Wordlist("./passwords/"), int(sys.argv[3]))
                else: print("ERROR: TIME LIMIT MUST BE SUPERIOR TO 0")
            else:
                print("help: display the list of commands")
        else:
            print("ERROR: TIME LIMIT MUST BE AN INTEGER")
    elif(len(sys.argv) == 2):
        if(str(sys.argv[1]) == "help"):
            print("Functions:\n\nsimple password time_limit : Crack the password with brute-force attacks")
            print("fast password time_limit : Crack the password with brute-force attacks as fast as possible")
            print("word password time_limit : Crack the password with dictionnary attacks\n")
            print("\nArguments:\n\npassword: the plain password to test(STRING)\ntime_limit: the time limit to crack the password(INT > 0)")
        else:
            print("help: display the list of commands")
    elif(len(sys.argv) == 3):
        if(str(sys.argv[1]) == "check"):
            BruteForce.Check(str(sys.argv[2]), Load.get_Characters())
        else:
            print("help: display the list of commands")
    else:
        print("help: display the list of commands")
        