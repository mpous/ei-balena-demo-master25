import cv2
from time import sleep
import requests

# Start the webcam capture
print("Starting the capture-inference demo...")
i = 1
ramp_frames = 30
camera_port = 0

def capture_image():
    cap = cv2.VideoCapture(camera_port)
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
            # if first iteration, save the image locally just to have
            if i == 1:
                cv2.imwrite("/app/storage/image.png", frame)
            return buffer_bytes

    else:
        print('Failed to open default camera. Exiting...')
    cap.release()
    return None


while(True):
    # Capture the image in a loop, and infer using the EI Docker container API
    print("Trying to capture image {}...".format(i))
    image = capture_image()
    if image is not None:
        # Send the image to the Docker container API for inferencing
        img = {'file': ('image.jpg', image)}
        r = requests.post('http://edge-impulse/api/image', files=img)
        print("Response {}: {}".format(i, r.text))
    else:
        print("Failed to capture the image {}.".format(i))

    i = i + 1
    sleep(4)
