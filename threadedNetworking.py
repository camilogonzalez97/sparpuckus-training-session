import socket
import struct
from threading import Thread
import time


def runServer():
    # Define a socket that will accept connections
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server to a specific address (IP + port)
    server.bind(("127.0.0.1", 40000))

    # Start listening for connections
    server.listen(1)

    # Accept connections
    print("Waiting for connection...")
    server, clientAddress = server.accept()
    # Notice how this doesn't pring until a connection is received.
    print("Received connection from: ", clientAddress)

    # Start sending messages
    messageFormat = "di"
    messageNumber = 1
    while True:
        timestamp = time.time()
        message = struct.pack(messageFormat, timestamp, messageNumber)
        server.sendall(message)

        messageNumber += 1

        time.sleep(0.1)


def runClient():
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


if __name__ == "__main__":

    # Server thread
    serverThread = Thread(target=runServer, daemon=True)

    # Client thread
    clientThread = Thread(target=runClient, daemon=True)

    # Start threads
    serverThread.start()
    clientThread.start()

    # Run until ctrl-c
    r = input()  # You need this because join is a blocking function
    serverThread.join()
    clientThread.join()
