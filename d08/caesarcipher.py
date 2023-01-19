from art import logo #imports a the logo alone from the module art
print(logo) #print the caesar cipher logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#inside alphabets there are two sets because if someone gives the message to encode as zulu, xxx or any letter that is almost end of alphabets, shifting will not happen likely. hence after z another set of alphabets have been given

#caeser function has does two functions inside which is encrypt and decrypt , based on the direction input the function calls whether to encrypt or decode
#cases added: 
#case 1. when the user also enters some characters symbols or numbers, we will encrypt only the alphabets and the remaining characters remains same
#case 2: when the user gives shift number that is greater than the number of letters we use modulo operator. eg.shift=45 , then 45%26 is 19. the shift amount becomes 19
#encrypt is to the encrypt the message given by based on the input (text) and the text is shifted by the amount (shift) given by user
#eg. text=hello, shift=2, encrypted message = jgnnq

def caesar(start_text,shift_amount,cipher_direction):
    position=0 #to find the position of the current letters in the input text
    new_position=0 #to find the new position of the letters after shifting ( position +shift)
    end_text="" #encoded text or decoded text
    if cipher_direction=="encode": #if input is encode, 
        for p in start_text: # we have to check every letter in the text for its position to shift it by the given shift amount. hence for p in start_text ( text=input eg hello)
            if p in alphabet: #for case1: check all the letters in text is present in alphabet, if they are present proceed with shifting eg. hello123 ->jgnnq. for the 123 it will go to else part and the text remains same
                position=alphabet.index(p) # using the list.index(letter) function to find the positions of the letter h,e,l,l,o inside the alphabet list
                new_position=position+shift_amount #after finding the position of h,e,l,l,o shifting happens eg. shift =2 , position of h is = 7 then new position =9 hence the new text will be j
                end_text+=alphabet[new_position] # adding the new letters from the new position and creating the encoded word until all the letters are checked for "hello" so 5 times
            else:
                end_text+=p
        print(f"Encrypted word is {end_text}")
    elif cipher_direction=="decode": # same as encode
        for p in start_text:
            if p in alphabet:
                position=alphabet.index(p)
                new_position=position-shift_amount #shifting alone differs for encode we went right to shift the letters here it will be left side as its decode. ciphered word will be jgnnq, to encode will shift it 2 times om left side hence its decoded to helloo
                end_text+=alphabet[new_position]
            else:
                end_text+=p
        print(f"Decrypted word is {end_text}")

#below part is where the function is called
#case 3: when the user completes one function , user should be asked if they wants to continue again yes or no. 


to_end=False #initially setting the value as false
while not to_end:  # not false: loop continues until the value is true
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26 #case2
    caesar(text,shift,direction)
    restart=input("Do you want to continue? Y or N : ") 
    if restart=='N': #when the user says N (no), we are setting the value to to_end=True, because the loop ends 
        to_end=True #setting it as True, because while ends when it is false
        print("Goodbye")
    elif restart=='Y':
        to_end=False #setting it as False, because while continues when it is True

