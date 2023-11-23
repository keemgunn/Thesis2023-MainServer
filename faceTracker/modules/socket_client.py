import socketio

# Create a Socket.IO client
sio = socketio.Client()

def connect_to_scoketio_server(url):
    ### Connect to Socket.IO server ###
    try:
        sio.connect(url)
        print("Connected to Socket.IO server")
    except Exception as e:
        print("Failed to connect to Socket.IO server")
        print(e)

def send_sockeio_message(event, data):
    ### Send a message to the Socket.IO server ###
    if sio.connected:
        sio.emit(event, data)
        print("Sent message to Socket.IO server: " + str(data))
    else:
        print("Failed to send message to Socket.IO server: " + str(data))