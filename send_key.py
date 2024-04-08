from BB84 import initiate_keygen

# Sending the key to receiver
key = initiate_keygen(2)
print(f"Key to be written: {key}")

# save the key to a file
with open('./key.txt', 'a') as file:
    file.write(str(key))

