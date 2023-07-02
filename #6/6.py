from pyperclip import copy

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(message, key):
    newMessage = ''
    message = message.upper()
    charToIndex = {char: index for index, char in enumerate(SYMBOLS)}
    for char in message:
        if char in SYMBOLS:
            numChar = charToIndex[char]
            numChar = (numChar + key) % 26
            char = SYMBOLS[numChar]
        newMessage += char
    return newMessage

def decrypt(message, key):
    newMessage = ''
    message = message.upper()
    charToIndex = {char: index for index, char in enumerate(SYMBOLS)}
    for char in message:
        if char in SYMBOLS:
            numChar = charToIndex[char]
            numChar = (numChar - key) % 26
            char = SYMBOLS[numChar]
        newMessage += char
    return newMessage

def getKey():
    while True:
        print('Please enter the key (0 to 26) to use:')
        try:
            key = int(input('>'))
            if key <= 26 and key >= 0: return key
        except: print('Invalid key!! try again')

def main():
    print('Caesar Cipher')
    print('Do you wat to (e)ncrypt or (d)ecrypt?')
    phase = input('>')
    if phase.startswith('e'):
        print('Enter the message to encrypt:')
        message = input('>')
        key = getKey()
        print(encrypt(message, key))
        copy(encrypt(message, key))
        print('Full encrypted text copied to clipboard')

    
    if phase.startswith('d'):
        print('Enter the message to decrypt:')
        message = input('>')
        key = getKey()
        print(decrypt(message, key))
        copy(decrypt(message, key))
        print('Full decrypted text copied to clipboard')

if __name__ == '__main__':
    main()