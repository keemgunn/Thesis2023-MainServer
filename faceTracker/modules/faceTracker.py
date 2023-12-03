import cv2
import mediapipe as mp
import numpy as np
import time

# Import the create_osc_client function from the OSCclient module
from .OSCclient import create_osc_client

def run_face_tracker(margin_x, margin_y, offset_x, offset_y, detection_confidence, tracking_confidence, osc_client):
    #### Initialize mediapipe ####
    # For facemesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=detection_confidence, min_tracking_confidence=tracking_confidence)

    # For drawing landmarks
    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

    # For webcam input
    cap = cv2.VideoCapture(0)

    # Get the resolution of the camera
    img_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    img_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define boundaries (ROI)
    roi_x_min, roi_x_max = margin_x, img_w - margin_x
    roi_y_min, roi_y_max = margin_y, img_h - margin_y
    roi_w = roi_x_max - roi_x_min
    roi_h = roi_y_max - roi_y_min

    #### Print Program Info ####
    print("\n\n")
    print("==== Face Tracker Module Activated ==== \n")

    # Get the camera index
    camera_index = cap.get(cv2.CAP_PROP_POS_FRAMES)
    print("Camera Index:", camera_index)

    # Get the camera device name
    camera_device_name = cap.getBackendName()
    print("Camera Device Name:", camera_device_name)

    # print boundaries
    print("boundaries")
    print(roi_x_min, roi_x_max)
    print(roi_y_min, roi_y_max)

    #### Main Process ####
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("!! NO IMAGE INPUT !!")
            continue

        #### Reset variables for each frame ####
        start = time.time() # Start timer (for calculating frame rate)
        face_3d, face_2d = [], [] # Arrays to store the coordinates

        #### Crop the image for Face Tracking ####
        roi = image[roi_y_min:roi_y_max, roi_x_min:roi_x_max]
        roi = cv2.cvtColor(cv2.flip(roi, 1), cv2.COLOR_BGR2RGB)
        roi.flags.writeable = False
        results = face_mesh.process(roi)
        roi.flags.writeable = True
        roi = cv2.cvtColor(roi, cv2.COLOR_RGB2BGR)

        #### Preprocess the Original Image ####
        image = cv2.flip(image, 1)

        #### Draw Basic Info ####
        cv2.putText(roi, f"Original Resolution: {img_w} x {img_h}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(roi, f'Resolution: {roi_w}x{roi_h}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(roi, f'Margins X:{margin_x} Y:{margin_y}', (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

        #### Main Face Tracking Process ####
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for idx, lm in enumerate(face_landmarks.landmark):
                    if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                        if idx == 1: # Face Landmark 1 (Nose)
                            nose_2d = (lm.x * roi_w, lm.y * roi_h)
                            nose_3d = (lm.x * roi_w, lm.y * roi_h, lm.z * 3000)
                            # Calculate the absolute coordinates
                            pos_x, pos_y = int(lm.x * roi_w + offset_x), int(lm.y * roi_h + offset_y)
                            rel_x, rel_y = np.round(lm.x, 3), np.round(lm.y, 3)

                        # Calculate the absolute coordinates
                        lm_x, lm_y = int(lm.x * roi_w), int(lm.y * roi_h)

                        # Get the coordinates
                        face_2d.append([lm_x, lm_y])
                        face_3d.append([lm_x, lm_y, lm.z])

                # Convert it to the NumPy array
                face_2d = np.array(face_2d, dtype=np.float64)
                face_3d = np.array(face_3d, dtype=np.float64)

                # The camera matrix
                focal_length = 1 * roi_w 
                cam_matrix = np.array([ [focal_length, 0, roi_h / 2],
                                        [0, focal_length, roi_w / 2],
                                        [0, 0, 1]])

                # The distortion parameters
                dist_matrix = np.zeros((4, 1), dtype=np.float64)

                # Solve PnP
                success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

                # Get rotational matrix
                rmat, jac = cv2.Rodrigues(rot_vec)

                # Get angles
                angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

                # Get the rotation in terms of degrees
                rot_x = angles[0] * 360
                rot_y = angles[1] * 360
                rot_z = angles[2] * 360

                # Display the nose direction
                nose_3d_projection, jacobian = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)
                p1 = (int(nose_2d[0]), int(nose_2d[1]))
                p2 = (int(nose_2d[0] + rot_y * 10) , int(nose_2d[1] - rot_x * 10))
                cv2.line(roi, p1, p2, (255, 0, 0), 3)

                #### Draw info on the ROI ####
                cv2.putText(roi, "ROTATION", (10, 125), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(roi, "- rot_x: " + str(np.round(rot_x,2)), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(roi, "- rot_y: " + str(np.round(rot_y,2)), (10, 175), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(roi, "- rot_z: " + str(np.round(rot_z,2)), (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(roi, "POSITION", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(roi, "- pos_x: " + str(pos_x), (10, 275), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(roi, "- pos_y: " + str(pos_y), (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(roi, "- rel_x: " + str(rel_x), (10, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(roi, "- rel_y: " + str(rel_y), (10, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                

            #### Send OSC message ####
            osc_client.send_message("/face/position", [pos_x, pos_y])
            osc_client.send_message("/face/relavantPosition", [rel_x, rel_y])
            osc_client.send_message("/face/rotation", [rot_x, rot_y, rot_z])


            #### Draw landmarks ####
            mp_drawing.draw_landmarks(
                        image=roi,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=drawing_spec,
                        connection_drawing_spec=drawing_spec)

            #### Calculate FPS ####
            end = time.time()
            totalTime = end - start
            fps = 1 / totalTime
            cv2.putText(roi, f'FPS: {int(fps)}', (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        cv2.imshow('Face Tracking', roi)

        # Press 'ESC' to quit
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()



# If this file is executed directly, run the function above
if __name__ == "__main__":

    #### Define Constants ####
    MARGIN_X, MARGIN_Y = 300, 50
    OFFSET_X, OFFSET_Y = 0, 0
    DETECTION_CONFIDENCE = 0.5
    TRACKING_CONFIDENCE = 0.5
    
    #### Setup OSC client ####
    ip = "127.0.0.1"  # Replace with the OSC server IP
    port = 8282       # Replace with the OSC server port
    osc_client = create_osc_client(ip, port)

    run_face_tracker(MARGIN_X, MARGIN_Y, OFFSET_X, OFFSET_Y, DETECTION_CONFIDENCE, TRACKING_CONFIDENCE, osc_client)