def split_len(seq, length):
    lili= [seq[i:i + length] for i in range(0, len(seq), length)]
    print(lili)
    return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
    order = {
        int(val): num for num, val in enumerate(key)
    }
    print("the order = "+str(order))
    print("the key order ="+str(order.keys()))
    ciphertext = ''
    #order= ('3214', 'HELLO')
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            print("order=" + str(order))
            print("index=" + str(index))
            print("part=" + str(part[order[index]]))
            print("\n")
            try:ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext
print(encode('32154', 'HELLOISISCMARIA'))