from pythonosc.udp_client import SimpleUDPClient

# Creates and returns an OSC client instance.
def create_osc_client(ip, port):
    client = SimpleUDPClient(ip, port)
    return client