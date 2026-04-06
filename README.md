# 🚀 Deep Learning Pipeline

## 📌 Overview

This project demonstrates a complete **Deep Learning pipeline** for image classification using Convolutional Neural Networks (CNN).

The pipeline follows a structured approach used in real-world deep learning systems, including data preprocessing, model building, training, evaluation, and deployment.

The final model is deployed using a **Streamlit web application**, allowing users to upload images and get real-time predictions.

---

## 🎯 Objective

The objective of this project is to:

- Build an end-to-end Deep Learning pipeline  
- Preprocess image data  
- Design and implement a CNN model  
- Train and evaluate the model  
- Improve model performance  
- Deploy the model using a web interface  

---

## 🧠 Deep Learning Pipeline


Problem Definition
↓
Data Collection
↓
Data Preprocessing
↓
Exploratory Data Analysis (EDA)
↓
Model Building (CNN)
↓
Model Training
↓
Model Evaluation
↓
Model Saving
↓
Deployment (Streamlit App)


---

## 📂 Project Structure


Deep-Learning-Project/

├── dataset/
│ ├── train/
│ └── test/

├── 01_load_dataset.py
├── 02_preprocessing.py
├── 03_visualization.py
├── 04_model_building.py
├── 05_model_training.py
├── 06_model_evaluation.py
├── 07_model_saving.py
├── app.py

├── model.h5
├── requirements.txt
└── README.md


---

## ⚙️ Pipeline Steps

### 1️⃣ Data Loading
- Load image dataset from directory  
- Identify classes  
- Count total images  

---

### 2️⃣ Data Preprocessing
- Resize images to fixed size (224x224)  
- Normalize pixel values (0–255 → 0–1)  
- Apply data augmentation  

---

### 3️⃣ Exploratory Data Analysis (EDA)
- Visualize sample images  
- Check class distribution  
- Understand dataset structure  

---

### 4️⃣ Model Building (CNN)
- Build Convolutional Neural Network  
- Use Conv2D, MaxPooling, Flatten layers  
- Add Dense layers for classification  

---

### 5️⃣ Model Training
- Train model using training dataset  
- Validate using test dataset  
- Monitor accuracy and loss  

---

### 6️⃣ Model Evaluation
- Analyze accuracy and loss curves  
- Detect overfitting or underfitting  
- Improve model performance  

---

### 7️⃣ Model Saving
- Save trained model using TensorFlow  
- Output file: `model.h5`  

---

### 8️⃣ Deployment
- Build Streamlit web application  
- Upload image as input  
- Predict image class  

---

## 🛠 Technologies Used

- Python  
- TensorFlow / Keras  
- NumPy  
- Matplotlib  
- Pillow (PIL)  
- Streamlit  

---

## 💻 Installation

Install required libraries:


pip install tensorflow numpy matplotlib pillow streamlit


---

## ▶️ Running the Pipeline

Run scripts in order:

```bash
python 01_load_dataset.py
python 02_preprocessing.py
python 03_visualization.py
python 04_model_building.py
python 05_model_training.py
python 06_model_evaluation.py
python 07_model_saving.py
▶️ Run Application
streamlit run app.py

Open in browser:

http://localhost:8501
``` id="dl-url-clean"

---

## 📊 Dataset

The project uses an image dataset structured as:


dataset/
├── train/
│ ├── class1/
│ └── class2/
├── test/
│ ├── class1/
│ └── class2/


Example:
- Cat  
- Dog  

---

## 🌍 Applications

- Image classification systems  
- Medical image analysis  
- Waste classification  
- Object detection systems  
- Face recognition  

---

## 🎓 Learning Outcomes

- End-to-end Deep Learning pipeline  
- CNN model development  
- Image preprocessing techniques  
- Model training and evaluation  
- Deployment using Streamlit  

---

## 👨‍💻 Author

Harsh Chauhan  
AI & Data Science Enthusiast
