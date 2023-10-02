# Secret Message Decoder

This is a Python program that can decode secret messages encoded using different ciphers. The program currently supports two ciphers: a simple Caesar cipher and a Vigenère cipher.

## Caesar Cipher

The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. In this program, we provide functions for both encoding and decoding messages using a Caesar cipher.

### Usage

To decode a message using the Caesar cipher with an offset of 10, you can use the `decoder` function. Here's an example:

```python
message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
decoded_message = decoder(message_one, 10)
print(decoded_message)
```

This will decode the message and print the result.

## Brute Force Attack

If you have a message encoded using a Caesar cipher, but you don't know the offset, you can use the brute force approach provided in the code. The program will try all possible offsets (from 1 to 25) and print the decoded messages. You can then manually identify the correct decoding.

### Usage

Here's an example of how to use the brute force approach:

```python
message_to_decode = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for i in range(1, 26):
    print("Offset " + str(i))
    print(decoder(message_to_decode, i))
```

## Vigenère Cipher

The Vigenère cipher is a more complex polyalphabetic substitution cipher. To decode a message encoded using the Vigenère cipher, you need a keyword.

### Usage

You can decode a message using the Vigenère cipher with a keyword like this:

```python
message2 = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"
decoded_message = vigenere_decoder(message2, keyword)
print(decoded_message)
```

This will decode the message using the provided keyword and print the result.

Feel free to use this code to decode secret messages encoded with either the Caesar cipher or the Vigenère cipher.

Happy decoding!
