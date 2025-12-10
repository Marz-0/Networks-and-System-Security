# Week 2 Practical Summary  

## RSA, AES & Socket Programming

In this week’s practical session, I implemented a secure communication system using a hybrid cryptographic approach combining RSA and AES. To begin, I generated an RSA key pair using `generate_keys.py`, which creates a 2048-bit RSA private key and derives the corresponding public key. These keys are saved as PEM files and represent a simulated key-exchange process where the public key is used for encryption and the private key for decryption. 

NOTE: The keys generated may be located outside of the "Lab 2" folder, but generating the keys should still successfully run the entire lab. 

I then ran the receiver script, which starts a TCP socket server on `localhost:65432`. It waits for a client connection, receives the encrypted payload in chunks, and unpacks it into three components: the RSA-encrypted AES key, the IV, and the AES-encrypted ciphertext. Using the private RSA key and OAEP padding with SHA-256, it decrypts the AES key and then uses AES-256 in CFB mode to decrypt the message.

Next, I ran the sender script. This script loads the recipient’s public RSA key, generates a random 32-byte AES key and a 16-byte IV, and encrypts a plaintext message using AES-CFB. It then encrypts the AES key using RSA-OAEP and sends the entire payload (encrypted key, IV, ciphertext) to the receiver over a TCP connection.

Finally, the receiver successfully decrypted the AES key and message. The output observed was:

Decrypted message: Hello from the secure sender! This is confidential.

This demonstrated a complete hybrid encryption workflow and strengthened my understanding of secure key exchange, symmetric encryption, and socket-based data transmission.
