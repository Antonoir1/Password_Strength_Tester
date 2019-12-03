import BruteForce, Hash
import sys
import numpy as np

if __name__ == "__main__":
    if(len(sys.argv) != 5):
        print("ERROR: WRONG ARGUMENTS")
        print("Password_Strength_Tester password min_length max_length time_limit")
        print("password : STRING\nmin_length: INTEGER\nmax_length : INTEGER\ntime_limit : INTERGER (seconds)")
    try:
        if(int(sys.argv[2]) <= int(sys.argv[3]) and int(sys.argv[4]) > 0):
            lvl = 0
            crack_count = 0
            password = Hash.convert_sha256(sys.argv[1])
            min_length = int(sys.argv[2])
            max_length = int(sys.argv[3])
            time_limit = int(sys.argv[4])
            combin_values = [] #Combination array of the characters array in BruteForce.PRIMORDIAL 
            refl = [ j for j in range(0,len(BruteForce.PRIMORDIAL))]
            for i in range(0,len(BruteForce.PRIMORDIAL)):
                combin_values.append([])
                for j in range(0,len(BruteForce.PRIMORDIAL)):
                    combin_values[i].append([])
            for i in range(0,len(BruteForce.PRIMORDIAL)):
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

            #Go through the all the combination possible and use them to try to crack the password
            for i in range(0, len(combin_values)):
                for j in range(0,len(combin_values[0])):
                    if(len(combin_values[i][j]) != 0):
                        
                        for k in range(0,len(combin_values[i][j])):
                            alphabet = np.array([])
                            for l in range(0,len(combin_values[i][j][k])):
                                alphabet = np.concatenate([alphabet, BruteForce.PRIMORDIAL[combin_values[i][j][k][l]]])
                            print("Estimated maximum time: "+str(BruteForce.speed(min_length, max_length, alphabet))+" seconds")
                            lvl += BruteForce.brute_force(password, min_length, max_length, alphabet, time_limit)
                            crack_count += 1

            if(lvl < 0):
                print("The strength level of the password against brute-force "+str(sys.argv[1])+" (with min_length = "+str(min_length)+", max_length = "+str(max_length)+" and time_limit = "+str(time_limit)+") seconds) is LVL = 0/"+str(crack_count))
            else:
                print("The strength level of the password against brute-force "+str(sys.argv[1])+" (with min_length = "+str(min_length)+", max_length = "+str(max_length)+" and time_limit = "+str(time_limit)+" seconds) is LVL = "+str(lvl)+"/"+str(crack_count))
        else:
            print("ERROR: WRONG ARGUMENTS")
            print("Password_Strength_Tester password min_length max_length time_limit")
            print("password : STRING\nmin_length: INTEGER\nmax_length : INTEGER\ntime_limit : INTERGER (seconds)")
    except:
        print("ERROR: WRONG ARGUMENTS")
        print("Password_Strength_Tester password min_length max_length time_limit")
        print("password : STRING\nmin_length: INTEGER\nmax_length : INTEGER\ntime_limit : INTERGER (seconds)")