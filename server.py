import socket
import struct
import time

if __name__ == "__main__":

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

        print("I have sent {:d} messages current time: {:.2f}".format(
            messageNumber, timestamp))
        messageNumber += 1

        time.sleep(0.1)
