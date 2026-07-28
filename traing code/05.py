import numpy as np
# import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Dropout, Flatten, Bidirectional, LSTM, Reshape
from keras.applications import VGG16
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
# from sklearn.preprocessing import label_binarize

# Define the directory and classes
img_dir = 'train'
img_clss=['c0','c6','c7','c9']

# ImageDataGenerator for data augmentation and rescaling
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=50,  # Increased augmentation
    width_shift_range=0.3,
    height_shift_range=0.3,
    shear_range=0.3, 
    zoom_range=0.3,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2 ) # Use this to split data into training and validation sets


# Create the training data generator
train_generator = datagen.flow_from_directory(
    img_dir,
    target_size=(200, 200),
    batch_size=32,
    class_mode='categorical',
    subset='training')

# Create the validation data generator
validation_generator = datagen.flow_from_directory(
    img_dir,
    target_size=(200, 200),
    batch_size=32,
    class_mode='categorical',
    subset='validation')

# Pretrained VGG16 Model for Feature Extraction
vgg = VGG16(input_shape=(200, 200, 3), include_top=False, weights='imagenet')
vgg.trainable = False  # Freeze VGG16 layers

# Model creation
model = Sequential()
model.add(vgg)  # Add VGG16 as the base

# Flatten the VGG16 output
model.add(Flatten())

# Reshape for LSTM input
model.add(Reshape((1, -1)))  # Reshape to (timesteps, features)
# Bidirectional LSTM
model.add(Bidirectional(LSTM(256, return_sequences=False)))  # Increased LSTM units

# Fully connected layers
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))

# Output layer (for 4 classes)
model.add(Dense(4, activation='softmax'))

# Model summary
model.summary()

# Compile the model with Adamax optimizer
model.compile(optimizer=tf.keras.optimizers.Adamax(learning_rate=0.001), 
            loss='categorical_crossentropy', 
            metrics=['accuracy'])

# Callbacks for early stopping and learning rate reduction
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)

# Training the model using the generators
history = model.fit(train_generator, epochs=50, validation_data=validation_generator, validation_steps=validation_generator.samples // validation_generator.batch_size, callbacks=[early_stopping, lr_scheduler])

# Save the model
# model.save('distracted_driver333.h5')
