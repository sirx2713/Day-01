# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

# Load the MNIST dataset
print("Loading MNIST dataset...")
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, parser='auto')
print("Dataset loaded successfully!")

# Convert to numpy arrays and ensure proper data types
X = np.array(X, dtype=float)
y = np.array(y, dtype=int)

# Let's select a specific digit image (index 36000)
print("Selecting image at index 36000...")
myDigit = X[36000]

# MNIST images are flattened (784 pixels = 28x28)
# We need to reshape it back to 2D
myImage = myDigit.reshape(28, 28)

# Display the image
print("Displaying the digit image...")
plt.figure(figsize=(5, 5))
plt.imshow(myImage, cmap='binary', interpolation='nearest')
plt.axis("off")
plt.title(f"This is digit: {y[36000]}")
plt.show()

print("Done")