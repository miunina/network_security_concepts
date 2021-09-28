import string
def get_order(character):
    return ord(character)-65
def get_character(index):
    return chr(index+65)

def get_decouper(text1, text2_key):
 
    l1 = len(text1)
    l2 = len(text2_key)
    diff = l2-l1
    var = [text1[i:i+l2] for i in range(0,l1,l2)]  
    print (var)
    return var

def get_cipher(text1, text2_key):
    var = get_decouper(text1, text2_key)
    cipher = ''
    for part in var:
        for index in range(0,len(part)):
            cipher += get_character((get_order(part[index])+get_order(text2_key[index])) % 26)
    return cipher

text1 = "akli yassamine sisi mimi"
text2_key = "hello" 
print(get_cipher(text1,text2_key))