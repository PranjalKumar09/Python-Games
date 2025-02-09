""" 
the double the size in reciving is because we know the data we are sending while we not know the reciving data so we increase its chunk size to 2048*2 


Initialization:
    The connect_to_server method is called to establish a connection and retrieve the player number.

Connection to Server:
    The connect_to_server method attempts to connect the client socket to the server address.
    If successful, it receives the player number from the server and returns it.

Sending Data:
    It encodes the data into bytes using str.encode() and sends it over the socket.
    It then receives a response from the server using recv() and deserializes it using pickle.loads() before returning it.

"""

import socket
import pickle

class Network:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = "127.0.0.1"
        self.port = 5555
        self.address = (self.server_address, self.port)
        self.player_number = self.connect_to_server()

    def get_player_number(self):
        return self.player_number

    def connect_to_server(self):
        try:
            self.client_socket.connect(self.address)
            return self.client_socket.recv(2048).decode()
        except socket.error as e:
            print(f"Socket error during connection: {e}")
        except Exception as e:
            print(f"An error occurred during connection: {e}")

    def send_data(self, data):
        try:
            self.client_socket.send(str.encode(data))
            return pickle.loads(self.client_socket.recv(2048*2))
        except socket.error as e:
            print(f"Socket error during data transmission: {e}")
        except Exception as e:
            print(f"An error occurred during data transmission: {e}")
