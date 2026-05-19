from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

# Load EfficientNet model
model = EfficientNetB0(weights='imagenet', include_top=False, pooling='avg')

# Load sofa image
img_path = "best_sofa.jpg"

img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)

# Expand dimensions
img_array = np.expand_dims(img_array, axis=0)

# Preprocess image
img_array = preprocess_input(img_array)

# Extract features
features = model.predict(img_array)

print("Feature Vector Shape:", features.shape)

print(features)