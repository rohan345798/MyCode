from random import randint


def generate_key():
    original = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    copy = original.copy()
    encrypted = []
    randomrange = 25
    for i in range(26):
        newElem = copy[randint(0,randomrange)]
        encrypted.append(newElem)
        copy.remove(newElem)
        randomrange = randomrange-1
    key = {original[i]:encrypted[i] for i in range(len(original))}
    return key

def encryption(key, message):
    newMessage = []
    for i in message:
        if i in key:
            newMessage.append(key[i])
        else:
            newMessage.append(i)
    newMessage = ''.join(newMessage)
    return newMessage

def decrypt(key, encrypted):
    reverseKey = {key[i]:i for i in key}
    decrypted = []
    for i in encrypted:
        if i in reverseKey:
            decrypted.append(reverseKey[i])
        else:
            decrypted.append(i)
    decrypted = ''.join(decrypted)
    return decrypted

key = generate_key()
print (key)
message = encryption(key,"my name is rohan")
print (decrypt(key,message))