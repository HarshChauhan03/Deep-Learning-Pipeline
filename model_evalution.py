import matplotlib.pyplot as plt
import tensorflow as tf

# -----------------------------
# 1️⃣ Load Model + History
# -----------------------------
# NOTE: history object Day 5 se use hoga
# (Is code ko same file me run karo ya save history)

# Example: assume 'history' exists

# -----------------------------
# 2️⃣ Plot Accuracy
# -----------------------------
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# -----------------------------
# 3️⃣ Plot Loss
# -----------------------------
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title('Model Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()