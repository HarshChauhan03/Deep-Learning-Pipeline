import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# -----------------------------
# 1️⃣ Define Paths
# -----------------------------
train_path = "dataset/train"
test_path = "dataset/test"

# -----------------------------
# 2️⃣ Image Preprocessing
# -----------------------------
train_datagen = ImageDataGenerator(
    rescale=1./255,          # Normalize pixels (0-255 → 0-1)
    shear_range=0.2,         # Data augmentation
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(
    rescale=1./255
)

# -----------------------------
# 3️⃣ Load Images
# -----------------------------
train_data = train_datagen.flow_from_directory(
    train_path,
    target_size=(224, 224),   # Resize images
    batch_size=32,
    class_mode='binary'       # binary classification
)

test_data = test_datagen.flow_from_directory(
    test_path,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)

# -----------------------------
# 4️⃣ Info
# -----------------------------
print("Classes:", train_data.class_indices)
print("Train Samples:", train_data.samples)
print("Test Samples:", test_data.samples)