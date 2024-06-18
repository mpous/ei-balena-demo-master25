import cv2
from time import sleep
import requests
import os
#import numpy as np

# Start the webcam capture
print("Starting the capture-inference demo...")

i = 1  # iteration counter
ramp_frames = 30

try:
    camera_port = int(os.getenv('CAM_PORT', '0'))
except Exception as e:
    print("Invalid value for CAM_PORT. Using default 0.")
    camera_port = 0

try:
    sleep_time = int(os.getenv('SLEEP_TIME', '4'))
except Exception as e:
    print("Invalid value for SLEEP_TIME. Using default 4.")
    sleep_time = 4


def draw_bounding_boxes(frame, data):

    boxes = data['result']['bounding_boxes']

    for obj in boxes:
        label = obj['label']
        confidence = obj['value'] 

        x = int(obj['x'])
        y = int(obj['y'])
        w = int(obj['width'])
        h = int(obj['height'])

        top_left = (x, y)
        bottom_right = (x + w, y + h)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        label_with_conf = '{}: {:.2f}'.format(label, confidence)
        cv2.putText(frame, label_with_conf, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)
    return frame

def capture_image():
    try:
        cap = cv2.VideoCapture(camera_port)
    except Exception as e:
        print("Can't capture from webcam or no webcam - using sample images.")
        in_file = open("sample.jpg", "rb")
        data = in_file.read()
        return data
        
    # Give webcam time to initialize
    for j in range(ramp_frames):
        temp = cap.read()
    
    ret, frame = cap.read()
    if ret:
        # Convert the image to JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)

        # resize image
        resized = cv2.resize(ret, (160,160), interpolation = cv2.INTER_AREA)

        if ret:
            # Return the image as a bytes object
            cap.release()
            buffer_bytes = buffer.tobytes()
            # Save the image to accessible shared drive
            #cv2.imwrite("/app/storage/image{}.png".format(i), frame)
            cv2.imwrite("/app/storage/image.png", frame)
            #cv2.imwrite("/app/storage/image-box.png", frame)
            #return buffer_bytes
            return buffer_bytes, frame

    else:
        print('Failed to open default camera. Exiting...')
    cap.release()
    return None


while(True):
    # Capture the image in a loop, and infer using the EI Docker container API
    print("Trying to capture image {}...".format(i))
    image, frame = capture_image()
    if image is not None:
        # Send the image to the Docker container API for inferencing
        img = {'file': ('image.jpg', image)}
        try:
            r = requests.post('http://edge-impulse/api/image', files=img)
        except Exception as e:
            print("EI container not ready yet...")
        else:
            print("Response {}: {}".format(i, r.text))
             # If response is valid, draw bounding boxes
            if r.status_code == 200:
                data = r.json()  # Assuming JSON response contains bounding box data
                frame_with_boxes = draw_bounding_boxes(frame, data)
                # Save or display the image
                cv2.imwrite("/app/storage/image-box.png", frame_with_boxes)
            else:
                print("Failed to get valid response from inference API.")


    else:
        print("Failed to capture the image {}.".format(i))

    i = i + 1
    sleep(sleep_time)
