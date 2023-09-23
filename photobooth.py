import cv2
import time
import numpy as np
from tkinter import Tk, Button
from threading import Thread

# Function to start the countdown
def start_countdown():
    global countdown_duration
    countdown_duration = 3

# Initialize the countdown duration
countdown_duration = -1

# Set the frame size
frame_width = 960
frame_height = 540

# Create a black frame with the specified size
frame_design = np.zeros((frame_height, frame_width, 3), dtype="uint8")

# Open the webcam
cap = cv2.VideoCapture(0)

# Create a Tkinter window
root = Tk()
root.title("Camera App")

# Add a button to start the countdown
start_button = Button(root, text="Start Countdown", command=start_countdown)
start_button.pack()

# Run the camera loop in a separate thread
def camera_loop():
    global countdown_duration
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (frame_width, frame_height))
        
        if countdown_duration > 0:
            cv2.putText(frame, str(countdown_duration), (frame_width // 2, frame_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5, cv2.LINE_AA)
            countdown_duration -= 1
            time.sleep(1)
        elif countdown_duration == 0:
            final_frame = cv2.addWeighted(frame, 1, frame_design, 1, 0)
            cv2.imshow('Captured Frame', final_frame)
            countdown_duration = -1

        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Start the camera loop thread
camera_thread = Thread(target=camera_loop)
camera_thread.start()

# Start the Tkinter main loop
root.mainloop()
