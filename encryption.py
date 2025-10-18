"""
encryption.py - 
encrypts and decrypts the user's  input.
the user enters their sentences, the program encrypts the
sentences into numbers and saves them in a file called
"encrypted_msg.txt", then if asked to decrypt the program
decrypts the numbers back to letters and chars.

october 2025
author Roni Prital
"""

import sys

import logging
 
log_format = '%(levelname)s: %(message)s'
log_level = logging.INFO
logging.basicConfig(level=log_level, format=log_format)

encryption_map = {
        'A' : 56 , 
        'B' : 57 , 
        'C' : 58 , 
        'D' : 59 ,
        'E' : 40 ,
        'F' : 41 , 
        'G' : 42 ,
        'H' : 43 , 
        'I' : 44 , 
        'J' : 45 , 
        'K' : 46 , 
        'L' : 47 , 
        'M' : 48 , 
        'N' : 49 , 
        'O' : 60 , 
        'P' : 61 ,
        'Q' : 62 ,
        'R' : 63 ,
        'S' : 64 , 
        'T' : 65 , 
        'U' : 66 ,
        'V' : 67 ,
        'W' : 68 ,
        'X' : 69 ,
        'Y' : 10 ,
        'Z' : 11 ,
        'a' : 12 ,
        'b' : 13 ,
        'c' : 14 ,
        'd' : 15 ,
        'e' : 16 ,
        'f' : 17 ,
        'g' : 18 ,
        'h' : 19 ,
        'i' : 30 ,
        'j' : 31 ,
        'k' : 32 ,
        'l' : 33 ,
        'm' : 34 ,
        'n' : 35 ,
        'o' : 36 ,
        'p' : 37 ,
        'q' : 38 ,
        'r' : 39 ,
        's' : 90 ,
        't' : 91 ,
        'u' : 92 ,
        'v' : 93 ,
        'w' : 94 ,
        'x' : 95 ,
        'y' : 96 ,
        'z' : 97 ,
        ' ' : 98 ,
        ',' : 99 ,
        '.' : 100 ,
        "'" : 101 ,
        '!' : 102 ,
        '-' : 103 ,
 }


file_name = "encrypted_msg.txt"


def encrypt_func():

    """
    this function gets input from the user, 
    writes each letter and character from the users input
    as the number they are assigned with in the dictionary
    encryption_map and seperates them with " , "
    in the file file_name that is called "encrypted_msg.txt".

    """
    #print ("Function encrypt running")
    og_text = input("enter message to encrypt: ")
    #print("You entered:", og_text)
    

    with open(file_name, "w") as file1:
            for i , c in enumerate(og_text):
                    #print ("character is: " ,  c)

                    num = encryption_map.get (c,c)
                    #print("number= " , num)

                    file1.write (str(num))
                    if i < len(og_text) - 1:
                        file1.write (',')







def decrypt_func():

    """
    this function decrypts the content in the file "encrypted_msg.txt"
    with the dictionary encryption_map.

    the function creates a dictionary decryption_map that is 
    numbers to letters based on the letters to numbers decryption_map, 
    then reads the file and switches the numbers back into characters

    the function checks if the files content is empty and if it is
    it prints nothing

    with the assert command the function checks if all the parts in numbers
    are integers
    numbers that are not in the map are replaced with "?" 
    """
    
    #print ("Function decrypt running")
    
    # create dictionery dycreption_map number to letter

    decryption_map={}

    for letter , number in encryption_map.items():
         decryption_map[number] = letter
    #print("decryption map = " , decryption_map)


    with open(file_name, "r") as file1:
         file_content = file1.read()
         if len(file_content) == 0:
                print("")
                exit()
         
         #print("file content= " , file_content)
         parts = file_content.split(',')
         #print("parts = " , parts)

         numbers = []
         for part in parts: 
              assert part.isdigit() , 'error! only intiger numbers allowed'
              numbers += [int (part)]
         #print (numbers)

         text = ""
         for i in numbers:
              text = text + decryption_map.get(i , "?")
         #print("decrypted text is: " , text)    
         logging.info("decrypted text is: %s", text)     




def main(): 

    """
    this function prints an error if the users argument
    is different from encryption.py encrypt or encryption.py decrypt.
    also with the assert command.

    the function recognizes which action was chosen and calls
    the right function for the rest of the code.
    for encrypt encrypt_func , for decrypt decrypt_func.

    """ 

    if len(sys.argv) !=2 :
        print("error! only encryption.py encrypt or encryption.py decrypt")
        exit()

    else:
        action = sys.argv[1]
        #print("hello" , action , "from python")

        assert action in ('encrypt' , 'decrypt') , "only 'encrypt' or 'decrypt'!"

    # check action to be encrypt or decrypt else exit with error

    if action == 'encrypt' :
        #print ("action = ", action )
        encrypt_func()
    else : 
        if action == 'decrypt' :
            #print ("action = ", action )
            decrypt_func()
        else :
            print("error! invalid argument ", action, "! Only encrypt or decrypt are valid!")
            

if __name__ == '__main__':
    main()
