alphabet =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",' ']
I =         ["V","Z","B","R","G","I","T","Y","U","P","S","D","N","H","L","X","A","W","M","J","Q","O","F","E","C","K",' ']
II =        ["E","S","O","V","P","Z","J","A","Y","Q","U","I","R","H","X","L","N","F","T","G","K","D","C","M","W","B",' ']
III =        ["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J",' ']
IV =       ["A","J","D","K","S","I","R","U","X","B","L","H","W","T","M","C","Q","G","Z","N","P","Y","F","V","O","E",' ']
V =        ["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O",' ']
def coder(str, map1,map2):
    res = ""
    for i in range(len(str)):
        res +=map2[map1.index(str[i])]
    return res
def code():
    word = input("Input word: ")
    choose = input("encode or decode:")
    choose2 = input("Select key A/S/M/Q/Z")
    encode = ["Encode", "encode", "ENCODE"]
    decode = ["Decode", "decode", "DECODE"]
    #encoder
    if choose in encode and choose2 == "A":
        print(coder(word, I,alphabet))
    elif choose in encode and choose2 == "S":
        print(coder(word, II,alphabet))
    elif choose in encode and choose2 == "M":
        print(coder(word, III,alphabet))
    elif choose in encode and choose2 == "Q":
        print(coder(word, IV,alphabet))
    elif choose in encode and choose2 == "Z":
        print(coder(word, V,alphabet))
    #decoder
    elif choose in decode and choose2 == "A":
        print(coder(word, alphabet,I))
    elif choose in decode and choose2 == "S":
        print(coder(word, alphabet,II))
    elif choose in decode and choose2 == "M":
        print(coder(word, alphabet,III))
    elif choose in decode and choose2 == "Q":
        print(coder(word, alphabet,IV))
    elif choose in decode and choose2 == "Z":
        print(coder(word, alphabet,V))
    again = input("again? Y/n")
    if again == "Y" or "y":
        code()
code()