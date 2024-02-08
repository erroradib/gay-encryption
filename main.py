def gay_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr(((ord(char) - 65 + shift) % 26) + 65)
        elif char.islower():
            encrypted_text += chr(((ord(char) - 97 + shift) % 26) + 97)
        else:
            encrypted_text += char
    return encrypted_text

while True:
    plain_text = input("Enter your plain text: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = gay_encrypt(plain_text, shift)

    result = f'''Plain Text: {plain_text}
Gay Text: {encrypted_text}
Shift: {shift}
'''
    print(result)

    with open('gay_txt.txt', 'w') as f:
        f.write(result)
