from modules import faceTracker, OSCclient
from tools import load_configs


# Load configs
configs = load_configs.load()
UNREAL_IP = configs['UNREAL_IP'] # OSC server IP
UNREAL_OSC_PORT = configs['UNREAL_OSC_PORT'] # OSC server port
UNREAL_HTTP_PORT = configs['UNREAL_HTTP_PORT'] # HTTP server port
MARGIN_X = configs['MARGIN_X']
MARGIN_Y = configs['MARGIN_Y']  
OFFSET_X = configs['OFFSET_X']  
OFFSET_Y = configs['OFFSET_Y']  
DETECTION_CONFIDENCE = configs['DETECTION_CONFIDENCE']
TRACKING_CONFIDENCE = configs['TRACKING_CONFIDENCE']



# Main Process ------------------------------

# Create OSC client
osc_client = OSCclient.create_osc_client(UNREAL_IP, UNREAL_OSC_PORT)

# Run face tracker
faceTracker.run_face_tracker(MARGIN_X, MARGIN_Y, OFFSET_X, OFFSET_Y, DETECTION_CONFIDENCE, TRACKING_CONFIDENCE, osc_client)

