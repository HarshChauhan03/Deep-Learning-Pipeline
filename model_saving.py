# Day 7 - Save Model

import tensorflow as tf

# Assume model is already trained
# If using separate file, reload model training first

model.save("model.h5")

print("✅ Model saved as model.h5")