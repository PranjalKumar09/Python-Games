""" 

Server Setup:

    A socket is created (server_socket) using IPv4 and TCP.
    The server attempts to bind to the specified address and port.
    If binding fails, an error message is printed.
    The server listens for incoming connections with a maximum backlog of 2.

Client Handling Thread:

    The handle_client_thread function is defined to handle client connections and gameplay within a separate thread.
    It receives the client connection, player number, and game ID.
    It continuously receives and processes data from the client, updating the game state and sending it back.
    If the client disconnects or an error occurs, the thread closes and removes the game.

Main Loop:

    The server continuously accepts incoming connections.
    For each connection, it determines the player number and game ID based on the current state of the game.
    If it's the first player, a new game is created. If it's the second player, the existing game is marked as ready.
    A new thread is started to handle the client connection.


"""



import socket
from _thread import *
import pickle
from game import Game

SERVER = "127.0.0.1"
PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((SERVER, PORT))
except socket.error as e:
    print(str(e))

server_socket.listen(2)
print("Waiting for a connection. Server started.")

connected_clients = set()
games = {}
game_id_counter = 0


def handle_client_thread(client_connection, player_number, game_id):
    global game_id_counter
    client_connection.send(str.encode(str(player_number)))

    while True:
        try:
            data = client_connection.recv(4096).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset_play_status()
                    elif data != "get":
                        game.play(player_number, data)

                    client_connection.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection.")
    try:
        del games[game_id]
        print("Closing Game", game_id)
    except:
        pass
    game_id_counter -= 1
    client_connection.close()


while True:
    client_connection, address = server_socket.accept()
    print("Connected to:", address)

    game_id_counter += 1
    player_number = 0
    game_id = (game_id_counter - 1) // 2
    if game_id_counter % 2 == 1:
        games[game_id] = Game(game_id)
        print("Creating a new game...")
    else:
        games[game_id].ready = True
        player_number = 1

    start_new_thread(handle_client_thread, (client_connection, player_number, game_id))
