import sys
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
output = []

def main():
    answer = int(input("do you want to encrypt(1) or decrypt(2)? "))
    while answer != 1 and answer != 2:
            print("not a correct number!")
            answer = int(input("do you want to encrypt(1) or decrypt(2)?"))
    word = input("now give me a word: ").lower().strip()
    shift = int(input("and a letter shift: "))
    if answer == 1:
            print(crypto(word,shift))
    elif answer == 2:
            print(decrypto(word, shift))
        
def crypto(a, b):   

    for letter in a:
        if letter in alpha:   
            num = alpha.index(letter)
            new_pos = num + b
            while new_pos >= 25: 
                new_pos -=  25  
                if new_pos == 0:
                    break
            new_pos = int(new_pos)
            output.append(alpha[new_pos])  
        elif letter not in alpha:
            output.append(letter)
    return "".join(output)

def decrypto(a, b):   
    for letter in a:
        if letter in alpha:   
            num = alpha.index(letter)
            new_pos = num - b
            while new_pos < 0: 
                new_pos +=  25  
                new_pos = int(new_pos)
                if new_pos > 0:
                    break
            output.append(alpha[new_pos])
        elif letter not in alpha:
            output.append(letter)    
    return "".join(output)

         
main()