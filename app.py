from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

# Initialize camera
cap = cv2.VideoCapture(0)

# Background subtractors (only KNN and MOG2)
subtractors = {
    "KNN": cv2.createBackgroundSubtractorKNN(detectShadows=True),
    "MOG2": cv2.createBackgroundSubtractorMOG2(detectShadows=True)
}

current_subtractor = "KNN"

def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Apply background subtraction
        fgmask = subtractors[current_subtractor].apply(frame)
        
        # Color the mask for better visualization
        fgmask_colored = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
        fgmask_colored[fgmask == 255] = [0, 255, 0]  # Green for foreground
        fgmask_colored[fgmask == 127] = [0, 0, 255]  # Red for shadows

        # Combine frames side by side
        combined = np.hstack((frame, fgmask_colored))

        # Encode frame
        ret, buffer = cv2.imencode('.jpg', combined)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_subtractor/<subtractor_name>')
def set_subtractor(subtractor_name):
    global current_subtractor
    if subtractor_name in subtractors:
        current_subtractor = subtractor_name
        return f"Switched to {subtractor_name}"
    return "Invalid subtractor"

if __name__ == '__main__':
    app.run(debug=True)
