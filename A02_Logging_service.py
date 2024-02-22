import socket
import datetime
import threading

def clientHandler(connection, address):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    connected_flag = False

    # Logging
    # with open("logfile.txt", "a") as logfile:
    #     logfile.write(f"{current_time} - {address} connected.\n")

    try:
        
        while True:
            data = connection.recv(4096)
            if not data:
                break

            received_message = data.decode()
            parts = received_message.split(maxsplit=2)
            
            if len(parts) == 3:
                number, command, file_name = parts

                # if not connected_flag:
                #     with open("logfile.txt", "a") as logfile:
                #         logfile.write(f"{current_time} - {number} is connected.\n")
                #     connected_flag = True
                
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
        #connection.close()


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



if __name__ == "__main__":
    ip = '10.169.92.221'  # the ip address which client sent
    port = 24  # the port number which client sent

    receive_TCP_message(ip, port)





# def receive_udp_message(ip, port):
#     # Create UDP socket
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # Binding ip and port to address
#     server_address = (ip, port)
#     sock.bind(server_address)

#     print("UDP Opened.")
#     with open("logfile.txt", "a") as logfile:
#         logfile.write(f"{current_time} - Logging service started. Waiting for connections...\n")


#     try:
#         # waiting
#         while True:
#             print("\nwaiting...")
#             data, address = sock.recvfrom(4096)  
            
            
#             print(f"received message: {data.decode()}")
#             received_message = data.decode()
#             parts = received_message.split(maxsplit=2)
#             if len(parts) == 3:
#                 number ,command, file_name = parts
#                 if command == "-o":
#                     with open("logfile.txt", "a") as logfile:
#                         logfile.write(f"{current_time} - {number} - {file_name} opened.\n")
#                 elif command == "-c":
#                     with open("logfile.txt", "a") as logfile:
#                         logfile.write(f"{current_time} - {file_name} closed.\n")
#                 elif command == "-r":
#                     with open("logfile.txt", "a") as logfile:
#                         logfile.write(f"{current_time} - {file_name} is open for read.\n")
#                 elif command == "-w":
#                     with open("logfile.txt", "a") as logfile:
#                         logfile.write(f"{current_time} - {file_name} modified.\n")
#                 else :
#                     with open("logfile.txt", "a") as logfile:
#                         logfile.write(f"{current_time} - Wrong command is sent.\n")
#     finally:
#         sock.close()

# if __name__ == "__main__":
#     ip = '10.169.92.221'  # the ip address which client sent
#     port = 24  # the port number which client sent

#     receive_udp_message(ip, port)


# with open("logfile.txt", "a") as logfile:
#                logfile.write(f"{current_time} - Connected.\n")