import socket
import struct
import time

if __name__ == "__main__":

    # Create a client the short way
    client = socket.create_connection(("127.0.0.1", 40000))
    print("Connection established!")
    
    time.sleep(5)  # Create a delay on purpose

    # We can start parsing messages
    while True:

        bytes = client.recv(12)
        unpackedMessage = struct.unpack("di", bytes)

        messageReceived = time.time()
        print("Current time: {0:.2f}, message sent: {1:.2f}, delay: {2:.2f}s, message number: {3}".format(
            messageReceived, unpackedMessage[0], messageReceived - unpackedMessage[0], unpackedMessage[1]))

        # We can vary this and examine the effect that it has on the output
        time.sleep(0.1)
