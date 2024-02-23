# File name         : A02_Logging_service.py
# Programmer        : Minchul Hwang - 8818858
# Submission date   : 2/24/2024
# Purpose           : This program is service of logging.
#                     and it can take messages from client which is made by C++ file,
#                     the messages has some kind of information like command, file name, IP etc.
#                     this program distinguish that messages and translate them to print in log file.

import socket
import datetime
import threading

# Function header comment.
# function Name       : clientHandler
# Purpose             : this function can distinguish the messages and print properly messages in log file
# Input               : connection        the information what is come from client
#                       address           the IP and port address
# Output              : the input messages in log file 
# Return              : NONE
def clientHandler(connection, address):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        
        while True:
            data = connection.recv(4096)
            if not data:
                break

            received_message = data.decode()
            parts = received_message.split(maxsplit=2)
            
            if len(parts) == 3:
                number, command, file_name = parts

                with open("logfile.txt", "a") as logfile:
                    if command == "-o":
                        logfile.write(f"{current_time} - {number} - {file_name} opened.\n")
                    elif command == "-c":
                        logfile.write(f"{current_time} - {number} - {file_name} closed.\n")
                    elif command == "-r":
                        logfile.write(f"{current_time} - {number} - {file_name} is read.\n")
                    elif command == "-w":
                        logfile.write(f"{current_time} - {number} - {file_name} modified.\n")
                    elif command == "-q":
                        logfile.write(f"{current_time} - {number} is disconnected.\n")
                        connection.close() 
                        break
                    else:
                        logfile.write(f"{current_time} - {number}: Wrong command is sent.\n")
    finally:
        print(f"Connection from {address} (Client {number}) closed.")


# Function header comment.
# function Name       : receive_TCP_message
# Purpose             : This function can figure oout the information of IP and port.
#                       if the server is connected, the message is written down in logfile
# Input               : ip              the IP address
#                       port            the port of the IP
# Output              : the input messages in log file 
# Return              : NONE
def receive_TCP_message(ip, port):
# Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding ip and port to address
    server_address = (ip, port)
    server_socket.bind(server_address)

    print("TCP Opened.")
    with open("logfile.txt", "a") as logfile:
        logfile.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Logging service started. Waiting for connections...\n")

    connected_flag = False

    try:
        server_socket.listen(5)  # Listen for incoming connections
        while True:
            connection, address = server_socket.accept()  # Accept a new connection
            if not connected_flag:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("logfile.txt", "a") as logfile:
                    logfile.write(f"{current_time} - Client connected.\n")
                connected_flag = True
            threading.Thread(target=clientHandler, args=(connection, address), daemon=True).start()
    finally:
        server_socket.close()



# MAIN Function header comment.
# Purpose             : Save IP, port, and send them to receive_TCP_message function
# Input               : NONE
# Output              : NONE
# Return              : NONE
if __name__ == "__main__":
    ip = '10.169.92.221'  # the ip address which client sent
    port = 24  # the port number which client sent

    receive_TCP_message(ip, port)



