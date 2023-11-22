import cv2

def find_available_cameras(upper_limit=10):
    available_cameras = []
    for i in range(upper_limit):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # CAP_DSHOW is used specifically for Windows. You can remove it if you're on Linux or MacOS.
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

cameras = find_available_cameras()
print(f"Available camera indices: {cameras}")
