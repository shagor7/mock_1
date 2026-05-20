# Caesar Cipher Encryption and Decryption Program

# This function encrypts the original text
def caesar_cipher(text, shift):
    # This variable will store the encrypted text
    encrypted_text = ""

    # Loop through each character in the given text
    for char in text:

        # Check if the character is an alphabet letter
        if char.isalpha():

            # Move the character forward by the shift value
            shifted = ord(char) + shift

            # Check if the character is lowercase
            if char.islower():

                # If the shifted value goes after 'z',
                # wrap around to the beginning of lowercase alphabet
                if shifted > ord('z'):
                    shifted -= 26

                # If the shifted value goes before 'a',
                # wrap around to the end of lowercase alphabet
                elif shifted < ord('a'):
                    shifted += 26

            # Check if the character is uppercase
            elif char.isupper():

                # If the shifted value goes after 'Z',
                # wrap around to the beginning of uppercase alphabet
                if shifted > ord('Z'):
                    shifted -= 26

                # If the shifted value goes before 'A',
                # wrap around to the end of uppercase alphabet
                elif shifted < ord('A'):
                    shifted += 26

            # Convert the shifted ASCII value back to a character
            encrypted_text += chr(shifted)

        else:
            # If the character is not a letter,
            # keep it unchanged
            # Example: space, number, comma, full stop
            encrypted_text += char

    # Return the final encrypted text
    return encrypted_text


# This function decrypts the encrypted text
def caesar_decipher(encrypted_text, shift):
    # This variable will store the decrypted/original text
    decrypted_text = ""

    # Loop through each character in the encrypted text
    for char in encrypted_text:

        # Check if the character is an alphabet letter
        if char.isalpha():

            # Move the character backward by the shift value
            # This is the opposite of encryption
            shifted = ord(char) - shift

            # Check if the character is lowercase
            if char.islower():

                # If the shifted value goes before 'a',
                # wrap around to the end of lowercase alphabet
                if shifted < ord('a'):
                    shifted += 26

                # If the shifted value goes after 'z',
                # wrap around to the beginning of lowercase alphabet
                elif shifted > ord('z'):
                    shifted -= 26

            # Check if the character is uppercase
            elif char.isupper():

                # If the shifted value goes before 'A',
                # wrap around to the end of uppercase alphabet
                if shifted < ord('A'):
                    shifted += 26

                # If the shifted value goes after 'Z',
                # wrap around to the beginning of uppercase alphabet
                elif shifted > ord('Z'):
                    shifted -= 26

            # Convert the shifted ASCII value back to a character
            decrypted_text += chr(shifted)

        else:
            # If the character is not a letter,
            # keep it unchanged
            decrypted_text += char

    # Return the final decrypted text
    return decrypted_text


# Example usage

# Original message
text = "Hello World!"

# Shift value for encryption and decryption
shift = 3

# Encrypt the original text
encrypted = caesar_cipher(text, shift)

# Decrypt the encrypted text
decrypted = caesar_decipher(encrypted, shift)

# Display the results
print("Original text:", text)
print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)