
letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def enc_dec(text, key, mode):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ': # making sure no space included
            index = letters.find(letter) # return index of text letter in the letters (return -1 if not found)
            if index == -1:
                result += letter # add it as it is
            else: #success
                new_index = index + key
                if new_index >= num_letters: # if index exceeded 25, is 26 (empty) (0-25 index) then go to the begining off the letters
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result

print('*** Caesar Cipher Program ***\n')
mode = input('Enter E to encrypt or D to decrypt\n').lower()

if mode == 'e':
    print('Encryption mode selected\n')
    key = int(input('Enter the key (from 1 to 26) '))
    text = input('Enter the text to encrypt ')
    ciphertext = enc_dec(text, key, mode)
    print(f'Cipher Text: {ciphertext}')
elif mode == 'd':
    print('Decryption mode selected\n')
    key = int(input('Enter the key (from 1 to 26)' ))
    text = input('Enter the text to decrypt ')
    plaintext = enc_dec(text, key, mode)
    print(f'Plain Text: {plaintext}')
else:
    print('Please enter a valid input')
