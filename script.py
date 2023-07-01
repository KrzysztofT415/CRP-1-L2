import os
from chacha20poly1305 import ChaCha20Poly1305

key = b'Krzysiek'.ljust(32, b'\0')
cip = ChaCha20Poly1305(key)
nonce = b'\0' * 12
ciphertext = cip.encrypt(nonce, b'\0' * 112)

print('Key: ', key)
print('Nonce: ', nonce)
print('Output: ', ciphertext)
print('Length: ', len(ciphertext))

decrypted = cip.decrypt(nonce, ciphertext)
print('Decrypted: ', decrypted)

with open("result.txt", "wb") as out:
    out.write(ciphertext)