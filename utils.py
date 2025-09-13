import os
from reversy import encrypt
from reversy import decrypt

def save_password(entity_name, password):
    file = entity_name + ".passwd"
    encrypted_password = encrypt(password)
    f = open(file, "w")
    f.write(encrypted_password)
    print("Password saved successfully")
    print(file)
    f.close()

def retrieve_password(entity_name):
    file = entity_name + ".passwd"
    if os.path.exists(file):
        f = open(file, "r")
        encrypted_data = f.read()
        decrypted_password = decrypt(encrypted_data)
        print("Password retrieved successfully")
        f.close()
        return decrypted_password
    else:
        return "error"



