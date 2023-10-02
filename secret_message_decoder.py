# Define the alphabet and punctuation
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

# Define the encoded message
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

# Initialize an empty string to store the translated message
translated_message = ""

# Iterate through each character in the message
for letter in message:
    if not letter in punctuation:
        # Find the position of the letter in the alphabet
        letter_value = alphabet.find(letter)
        # Shift the letter by 10 positions and wrap around if needed
        translated_message += alphabet[(letter_value + 10) % 26]
    else:
        # If the character is in punctuation, keep it unchanged
        translated_message += letter

# Print the translated message
print(translated_message)


############## 2 ################
# Define functions for Caesar cipher encoding and decoding
# Note: These functions require the strings `alphabet` and `punctuation` to be defined before use

def decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message


def coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message


# Example usage of the `decoder` function
message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
decoded_message = decoder(message_one, 10)
print(decoded_message)

##############################
# Define a message encoded using a Caesar cipher with an unknown offset
text = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# Attempt to decode the message by brute force with all possible offsets
for i in range(1, 26):
    print("offset " + str(i))
    print(decoder(text, i))
# offset 7:
# "computers have rendered all of these old ciphers as obsolete. we'll have to really step up our game if we want to
# keep our messages safe."

##############################
# Define a message encoded using a Vigenère cipher and a keyword
message2 = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

# Define the alphabet and punctuation for the Vigenère cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "


# Define a function to decode a Vigenère cipher message
def vigenere_decoder(coded_message, keyword):
    point = 0
    kw_phrase = ""

    # Generate a keyword phrase that matches the length of the coded message
    for i in range(0, len(coded_message)):
        if coded_message[i] in punctuation:
            kw_phrase += coded_message[i]
        else:
            kw_phrase += keyword[point]
            point = (point + 1) % len(keyword)

    # Initialize an empty string to store the translated message
    translated_message = ""

    # Decode the message using the Vigenère cipher
    for i in range(0, len(coded_message)):
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(kw_phrase[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]

    return translated_message


# Example usage of the `vigenere_decoder` function
print(vigenere_decoder(message2, keyword))
