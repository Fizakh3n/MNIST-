# -*- coding: utf-8 -*-

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

"""# Loading the Dataset"""

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(f"Training data shape: {X_train.shape}, Labels shape: {y_train.shape}")
print(f"Training data shape: {X_test.shape}, Labels shape: {y_test.shape}")

""" # Visualize some samples from the training data"""

fig, axes = plt.subplots(1, 5, figsize=(10, 5))
for i in range(5):
    axes[i].imshow(X_train[i], cmap='gray')
    axes[i].set_title(f"Label: {y_train[i]}")
    axes[i].axis('off')
plt.show()

"""# Manually flatten the images from (28,28) to (784,)"""

X_train_flattened = X_train.reshape(X_train.shape[0], 28 * 28).astype('float32')
X_test_flattened = X_test.reshape(X_test.shape[0], 28 * 28).astype('float32')

"""# Normalize pixel values to be between 0 and 1"""

X_train_flattened /= 255.0
X_test_flattened /= 255.0

"""# Convert labels to **one-hot encoding**"""

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

"""# Build the model without a hidden layer"""

model = Sequential([
    Dense(10, activation='softmax', input_shape=(784,))  # Output layer with 10 neurons for 10 classes
])

"""#  Compile the model"""

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

"""# Train the **model**"""

model.fit(X_train_flattened, y_train, epochs=5, batch_size=32, validation_split=0.2)

"""# Evaluate the model on the test set"""

test_loss, test_accuracy = model.evaluate(X_test_flattened, y_test, verbose=2)
print(f"Test Loss: {test_loss}, Test Accuracy: {test_accuracy}")

""" # Make predictions on some test samples"""

predictions = np.argmax(model.predict(X_test_flattened[:5]), axis=1)

print("Predicted labels:", predictions)
print("Actual labels:", np.argmax(y_test[:5], axis=1))

"""# Visualising it"""

fig, axes = plt.subplots(1, 5, figsize=(10, 5))
for i in range(5):
    axes[i].imshow(X_test[i], cmap='gray')
    axes[i].set_title(f"Pred: {predictions[i]}, Actual: {np.argmax(y_test[i])}")
    axes[i].axis('off')
plt.show()

"""# Model with One Hidden Layer and Keras Flatten Layer"""

from tensorflow.keras.layers import Flatten

model = Sequential([
    Flatten(input_shape=(28, 28)),  # Flattening the input using Keras' built-in Flatten layer
    Dense(128, activation='relu'),  # Hidden layer with ReLU activation
    Dense(10, activation='softmax')  # Output layer with softmax for 10 classes
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)
print(f"Test Loss: {test_loss}, Test Accuracy: {test_accuracy}")

predictions = np.argmax(model.predict(X_test[:5]), axis=1)

print("Predicted labels:", predictions)
print("Actual labels:", np.argmax(y_test[:5], axis=1))

fig, axes = plt.subplots(1, 5, figsize=(10, 5))
for i in range(5):
    axes[i].imshow(X_test[i], cmap='gray')
    axes[i].set_title(f"Pred: {predictions[i]}, Actual: {np.argmax(y_test[i])}")
    axes[i].axis('off')
plt.show()

"""# THANK YOU !!"""

