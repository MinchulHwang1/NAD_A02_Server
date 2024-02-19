import socket
import datetime

def receive_udp_message(ip, port):
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Binding ip and port to address
    server_address = (ip, port)
    sock.bind(server_address)

    print("UDP Opened.")
    with open("logfile.txt", "a") as logfile:
            logfile.write(f"{current_time} - Connected.\n")

    try:
        # waiting
        while True:
            print("\nwaiting...")
            data, address = sock.recvfrom(4096)  

            
            print(f"received message: {data.decode()}")
            received_message = data.decode()
            parts = received_message.split()
            if len(parts) == 2:
                command, file_name = parts
                if command == "-o":
                    with open("logfile.txt", "a") as logfile:
                        logfile.write(f"{current_time} - {file_name} opened.\n")
                elif command == "-c":
                    with open("logfile.txt", "a") as logfile:
                        logfile.write(f"{current_time} - {file_name} closed.\n")
                elif command == "-r":
                    with open("logfile.txt", "a") as logfile:
                        logfile.write(f"{current_time} - {file_name} is open for read.\n")
                elif command == "-w":
                    with open("logfile.txt", "a") as logfile:
                        logfile.write(f"{current_time} - {file_name} modified.\n")
                else :
                    with open("logfile.txt", "a") as logfile:
                        logfile.write(f"{current_time} - Wrong command is sent.\n")
    finally:
        sock.close()

if __name__ == "__main__":
    ip = '10.169.92.221'  # the ip address which client sent
    port = 24  # the port number which client sent

    receive_udp_message(ip, port)


