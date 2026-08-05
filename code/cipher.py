#Vigenère Cipher

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"

def encrypt_password(password, key):
    password, key = password.upper(), key.upper()
    encrypted_password = ""
    for j in range(len(password)):
        password_alphanumeric = password[j]
        key_alphanumeric = key[j % len(key)]

        password_number = ALPHABET.index(password_alphanumeric)
        key_number = ALPHABET.index(key_alphanumeric)

        encrypted_number = ( password_number + key_number) % len(ALPHABET)
        encrypted_number2character = ALPHABET[encrypted_number]

        encrypted_password += encrypted_number2character 
    return encrypted_password

def new_encrypt_password(new_password, login_key):
    new_password, login_key = new_password.upper(), login_key.upper()
    new_encrypted = ""
    for j in range(len(new_password)):
        new_password_alphanumeric = new_password[j]
        key_alphanumeric = login_key[j % len(login_key)]

        new_password_number = ALPHABET.index(new_password_alphanumeric)
        key_number = ALPHABET.index(key_alphanumeric)

        new_encrypted_number = ( new_password_number + key_number) % len(ALPHABET)
        new_encrypted_number2character = ALPHABET[new_encrypted_number]

        new_encrypted += new_encrypted_number2character 
    return new_encrypted


