
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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

def main():
    print('Enter the encrypted message:')
    message = input('>')
    for key in range(0,26):
        print('Key #{}: {}'.format(key,decrypt(message, key)))

if __name__ == '__main__':
    main()