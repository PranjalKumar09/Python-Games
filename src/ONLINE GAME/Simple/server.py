import socket
from _thread import *
from player import Player
import pickle

server = ""
port = 5555

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e :
    print(str(e))

s.listen(2) # Leaving blank means unlimited clients

print("Waiting for connection, Server started")

connnected = set ()
games = []
idCount = 0





players = [Player(0,0,50,50,(255,0,0)) , Player(100,100,50,50,(0,0,255)) ]
def threaded_client(conn, current_player):
    # print("Type of players[current_player]:", type(players[current_player]))
    conn.send(pickle.dumps(players[current_player]))
    reply = ""
    while True: 
        try:
            data =pickle.loads(conn.recv(2048))
            players[current_player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if current_player == 1 :
                    reply = players[0]
                else: reply = players[1]
            print("Received: ", data)
            print("Sending: ", reply)
            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            print(e)
            break
    print("Lost Connection")
    conn.close()
    

current_player = 0
while True:
    conn , addr  = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,current_player ))
    current_player += 1
    current_player %=2 
    