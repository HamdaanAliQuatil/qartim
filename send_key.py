
from BB84 import initiate_keygen

# Sending the key to receiver
key = initiate_keygen(2)

# save the key to a file
with open('./key.txt', 'w') as file:
    file.write(str(key))

