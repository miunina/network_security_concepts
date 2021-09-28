import string
def alphabet_generate():
    list_alphabet = string.ascii_uppercase
    print(list_alphabet)
    return {int (val) : num for val, num in enumerate(list_alphabet)}
def get_cipher(text, key):
    list_alphabet = alphabet_generate()
    print(list_alphabet.keys())
    text =text.upper()
    cipher =''
    for j in range(0, len(text), 1):
        for i in (list_alphabet.keys()):    
            if(text[j] == list_alphabet[i]): #I am in the character
                cipher += list_alphabet[(i+key) % 26]
                print("j="+str(j)+" "+text[j]+ "==" + list_alphabet[i]+" i="+str(i))
                break;
    return cipher           
print(get_cipher("YASMINE",2))