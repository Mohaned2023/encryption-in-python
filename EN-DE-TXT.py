# Writing by Mohaned Mohammed Sherhan or The LEGEND

# import time 
import os
import time 
os.system("clear")

# list of letters
liste_of_letters = 'qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM012345.6;78:9'

# list of kay   
liste_of_kay = "!p@dflkBM#$%^&*a(90)HJKSngj_+?></.,678:;QER[]{23 }\|~14xczqW5-=mNA"
# def to encryption 
def encryption(The_input):
    # list to add the message
    liste_of_message = ""
    for search in The_input:
        if search in liste_of_letters:
            index = liste_of_letters.index(search)
            liste_of_message += liste_of_kay[index]
        else:
            print ("\033[1;34mError input = \033[1;35m"+search)
            liste_of_message += search
    print("")
    print ("\033[1;34mThe Encryption is :\033[1;35m"+liste_of_message)

# def to decryption
def decryption(The_input):
    # list to add the message
    liste_of_message = ""
    for search in The_input:
        if search in liste_of_kay:
            index = liste_of_kay.index(search)
            liste_of_message += liste_of_letters[index]
        else:
            print ("\033[1;34mError input = \033[1;35m"+search)
            liste_of_message += search
    print("")
    print ("\033[1;34mThe Decryption is :\033[1;35m"+liste_of_message)

# def to encryption_files
def encryption_files(The_file_input):
    try:
        open_file = open(The_file_input,"r")
        read_file = open_file.readline()
        open_file.close()
        open_to_read = open(The_file_input,"r")
        open_read = open_to_read.readlines()
        liste_of_message = ""
        for x in open_read:
            for search in x:
                if search in liste_of_letters:
                    index = liste_of_letters.index(search)
                    liste_of_message += liste_of_kay[index]
                else:
                    liste_of_message += search
            else:
                liste_of_message += "\n"
        open_file_to_add = open (The_file_input,"w")
        open_file_to_add.writelines(liste_of_message)
        open_file_to_add.close()
        print ("")
        print ("\033[1;34mThe Encryption is don..")
    except FileNotFoundError:
        print ("\033[1;35mPlease Enter the correct location...!")
        
# def to Decryption_files
def Decryption_files(The_file_input):
    try:
        open_file = open(The_file_input,"r")
        read_file = open_file.readline()
        open_file.close()
        open_to_read = open(The_file_input,"r")
        open_read = open_to_read.readlines()
        liste_of_message = ""
        for x in open_read:
            for search in x:
                if search in liste_of_kay:
                    index = liste_of_kay.index(search)
                    liste_of_message += liste_of_letters[index]
                else:
                    liste_of_message += search
            else:
                liste_of_message += "\n"
        open_file_to_add = open (The_file_input,"w")
        open_file_to_add.writelines(liste_of_message)
        open_file_to_add.close()
        print ("")
        print ("\033[1;34mThe Decryption is don..")
    except FileNotFoundError:
        print ("\033[1;35mPlease Enter the correct location...!")

# def the user 
def choose ():
    print ("""
    \033[1;35m _____   _____       \033[1;34m _____   __   _        \033[1;35m_____  __    __  _____  
    \033[1;35m|  _  \ | ____|      \033[1;34m| ____| |  \ | |      \033[1;35m|_   _| \ \  / / |_   _| 
    \033[1;35m| | | | | |__ \033[1;32m-------\033[1;34m| |__   |   \| |\033[1;32m--------\033[1;35m| |    \ \/ /    | |   
    \033[1;35m| | | | |  __|\033[1;32m-------\033[1;34m|  __|  | |\   |\033[1;32m--------\033[1;35m| |     }  {     | |   
    \033[1;35m| |_| | | |___\033[1;32m-------\033[1;34m| |___  | | \  |\033[1;32m--------\033[1;35m| |    / /\ \    | |   
    \033[1;35m|_____/ |_____|      \033[1;34m|_____| |_|  \_|        \033[1;35m|_|   /_/  \_\   |_|   
   
    \033[1;34m{ \033[1;35m1 \033[1;34m} To Encryption the message.
    \033[1;34m{ \033[1;35m2 \033[1;34m} To Decryption the message.
    \033[1;34m{ \033[1;35m3 \033[1;34m} To Encryption the file.
    \033[1;34m{ \033[1;35m4 \033[1;34m} To Decryption the file.
    \033[1;34m{ \033[1;35m0 \033[1;34m} To go out the tool.
    
    """)
    inp_choose = int (input("\033[1;32mHome >  "))
    if inp_choose == 1:
        os.system("clear")
        print ("""
        
        \033[1;34mEnter the message you want 
        to Encrypt.

        """)
        The_input = input("\033[1;32mHome > Encryption Message >  ")
        encryption(The_input)
        time.sleep(0.2)
        choose()
    elif inp_choose == 2:
        os.system("clear")
        print ("""
        
        \033[1;34mEnter the message you want 
        to Decrypt.
        
        """)
        The_input = input("\033[1;32mHome > Decryption Message >  ")
        decryption(The_input)
        choose()
    elif inp_choose == 3:
        os.system("clear")
        print("""

        \033[1;34mEnter the File location for Example { \033[1;35m\Home\D\Mrx\LEGEND.txt \033[1;34m} you want 
        to Encrypt.
        
        """)
        The_file_input = input("\033[1;32mHome > Encryption File >  ")
        encryption_files(The_file_input)
        time.sleep(0.2)
        choose()
    elif inp_choose == 4:
        os.system("clear")
        print("""

        \033[1;34mEnter the File location for Example { \033[1;35m\Home\D\Mrx\LEGEND.txt \033[1;34m} you want 
        to Decrypt.
        
        """)
        The_file_input = input("\033[1;32mHome > Decryption File >  ")
        Decryption_files(The_file_input)
        time.sleep(0.2)
        choose()
    elif inp_choose == 0:
        os.system("clear")
        print ("\033[1;32mSee you ......!")
        time.sleep(0.2)
    else:
        print ("\033[1;35minput error....!")
        choose()

choose()
