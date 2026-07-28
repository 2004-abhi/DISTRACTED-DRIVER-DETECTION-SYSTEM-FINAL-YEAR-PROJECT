import numpy as np
import tensorflow as tf
from keras.preprocessing import image
import cv2
from keras.models import load_model
import winsound
import os
import pymysql
from datetime import datetime

# Load pre-trained model
model = load_model('distracted_driver_bilstm_vgg16.h5')

# Define class labels
class_labels = {0: 'safe driving', 1: 'drinking', 2: 'reaching behind', 3: 'talking to passenger'}

# Create folder if it doesn't exist
save_folder = "unsafe_driving_images"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# MySQL Database Connection using pymysql
db = pymysql.connect(
    host="localhost",  # Change as per your database
    user="root",       # Change as per your username
    password="",       # Change as per your password
    database="distracted_drivers",  # Change as per your database name
    autocommit=True  # Ensures changes are committed without calling db.commit()
)
cursor = db.cursor()

# Ensure table exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS unsafe_driving_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        filename VARCHAR(255),
        timestamp DATETIME
    )
""")

def preprocess_image(img, target_size=(200, 200)):
    img = cv2.resize(img, target_size)  # Resize to target size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale
    return img_array

# Open webcam feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Preprocess the frame from webcam
    unseen_image = preprocess_image(frame)

    # Get predictions from the model
    predictions = model.predict(unseen_image)
    
    # Get the predicted class and its probability
    predicted_class = np.argmax(predictions, axis=1)[0]
    predicted_activity = class_labels[predicted_class]
    
    # Get the prediction confidence for the predicted class
    confidence = predictions[0][predicted_class] * 100  # Multiply by 100 to get percentage

    # Conditional display logic for 'reaching behind' and 'talking to passenger' only
    if predicted_activity in ['reaching behind', 'talking to passenger']:
        if confidence > 70:
            display_activity = predicted_activity
        else:
            display_activity = 'safe driving'  # If confidence is <= 70%, show 'safe driving'
    else:
        display_activity = predicted_activity  # For 'drinking' and 'safe driving', no threshold

    # If the activity is not 'safe driving', save image and log to database
    if display_activity != 'safe driving':
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms
        
        # Save the image
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{display_activity}_{timestamp}.jpg"
        filepath = os.path.join(save_folder, filename)
        cv2.imwrite(filepath, frame)
        
        # Insert into database
        cursor.execute("INSERT INTO unsafe_driving_logs (filename, timestamp) VALUES (%s, %s)", 
                       (filename, datetime.now()))

    # Display the predicted activity and confidence on the frame
    cv2.putText(frame, f'Predicted Activity: {display_activity}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(frame, f'Confidence: {confidence:.2f}%', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the camera feed with prediction
    cv2.imshow('Camera Feed', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
cursor.close()
db.close()
