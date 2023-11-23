from modules import faceTracker, OSCclient

# Setup OSC client --------------------------
OSC_IP = "127.0.0.1"  # OSC server IP
OSC_PORT = 8282       # OSC server port

# Setup face tracker ------------------------
MARGIN_X, MARGIN_Y = 300, 50
OFFSET_X, OFFSET_Y = 0, 0
SHARPNESS = 100
CONTRAST = 100
DETECTION_CONFIDENCE = 0.5
TRACKING_CONFIDENCE = 0.5 


# Main Process ------------------------------

# Create OSC client
osc_client = OSCclient.create_osc_client(OSC_IP, OSC_PORT)

# Run face tracker
faceTracker.run_face_tracker(MARGIN_X, MARGIN_Y, OFFSET_X, OFFSET_Y, SHARPNESS, CONTRAST, DETECTION_CONFIDENCE, TRACKING_CONFIDENCE, osc_client)

