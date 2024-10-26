# Constants
KEY = 0x42
enc_flag_0 = 7 

def xor_decrypt(enc_char, key):
    return chr(enc_char ^ key)

decrypted_flag = xor_decrypt(enc_flag_0, KEY)

print("Decrypted flag:", decrypted_flag)
