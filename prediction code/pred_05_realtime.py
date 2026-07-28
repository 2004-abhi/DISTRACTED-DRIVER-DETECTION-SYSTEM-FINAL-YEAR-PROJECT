import numpy as np
import tensorflow as tf
from keras.preprocessing import image
import cv2
from keras.models import load_model


model = load_model('distracted_driver_bilstm_vgg16.h5')

# Define class labels
class_labels = {0: 'safe driving', 1: 'drinking', 2: 'reaching behind', 3: 'talking to passenger'}

def preprocess_image(img, target_size=(200, 200)):
    img = cv2.resize(img, target_size)  # Resize to target size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale
    return img_array


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    unseen_image = preprocess_image(frame)

    predictions = model.predict(unseen_image)
    predicted_class = np.argmax(predictions, axis=1)[0]
    predicted_activity = class_labels[predicted_class]

    cv2.putText(frame, f'Predicted Activity: {predicted_activity}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Camera Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
