import socket

def receive_udp_message(ip, port):
    # UDP 소켓 생성
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 주소와 포트에 바인딩
    server_address = (ip, port)
    sock.bind(server_address)

    print("UDP 서버가 시작되었습니다.")

    try:
        # 메시지 수신 대기
        while True:
            print("\n대기 중...")
            data, address = sock.recvfrom(4096)  # 데이터를 받을 때까지 대기

            print(f"수신된 메시지: {data.decode()}")

    finally:
        sock.close()

if __name__ == "__main__":
    ip = '127.0.0.1'  # 클라이언트에서 보낸 IP 주소
    port = 20001  # 클라이언트에서 보낸 포트 번호

    receive_udp_message(ip, port)



# import socket

# localIP     = "10.169.92.221"
# localPort   = 20001
# bufferSize  = 1024

# msgFromServer       = "Hello UDP Client, This is the Server talking."
# bytesToSend         = str.encode(msgFromServer)

# # Create a datagram socket
# UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# # Bind to address and ip
# UDPServerSocket.bind((localIP, localPort))

# print("UDP server up and listening")

# # Listen for incoming datagrams

# while(True):

#     bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

#     message = bytesAddressPair[0]

#     address = bytesAddressPair[1]

#     clientMsg = "Message from Client:{}".format(message)
#     clientIP  = "Client IP Address:{}".format(address)
    
#     print(clientMsg)
#     print(clientIP)

#     # Sending a reply to client
#     UDPServerSocket.sendto(bytesToSend, address)
