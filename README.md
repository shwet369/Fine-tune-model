# 🧠 Age Detection Web App

A Deep Learning-based Age Prediction App using CNN and Streamlit that classifies a person’s age group from a face image. It features a clean interface and a responsive model trained on the UTKFace dataset.

---

## 🚀 Features
- 📸 Upload any image of a human face
- ⚖️ Predicts approximate **age class** (0 - 70+)
- 🔧 Built-in preprocessing and normalization
- 📈 CNN model with ~87% validation accuracy
- 🌐 Interactive **Streamlit** Web UI

---

## 🧠 Model Overview
- **Architecture:** Conv2D ➟ MaxPooling ➟ Flatten ➟ Dense
- **Input shape:** (100, 100, 3)
- **Dataset:** UTKFace (real-world face images with age labels)
- **Prediction Type:** Age Classification
- **Output:** Class index + readable age range

---

## 🌎 Live Demo Screenshot
(![app - Google Chrome 10-04-2025 11_51_42](https://github.com/user-attachments/assets/f6c71be8-aa88-4791-956e-38b491e13be0)
))

---

## 📂 Project Structure
```bash
age-detection-app/
├── app.py                  # Streamlit frontend
├── model/
│   └── age_model.h5         # Trained Keras model
├── sample_images/
│   └── example1.jpg         # Demo image
├── requirements.txt        # Project dependencies
└── README.md
```

---

## 🚀 Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/shwet369/age-detection-app.git
cd age-detection-app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the App
```bash
streamlit run app.py
```

---

## 🧩 Age Classes Explained
| Class | Age Range |
|-------|------------|
| 0     | 0 - 10     |
| 1     | 11 - 20    |
| 2     | 21 - 30    |
| 3     | 31 - 40    |
| 4     | 41 - 50    |
| 5     | 51 - 60    |
| 6     | 61 - 70    |
| 7     | 70+        |

> 🔗 The model maps a continuous age to a bucketed age range.

---

## ✅ Requirements
```
streamlit
tensorflow
numpy
Pillow
```

Install via:
```bash
pip install -r requirements.txt
```

---

## 📁 Unique Highlights
- 🌈 Real-time age classification via webcam or uploaded images
- 📊 Age prediction confidence visualization (optional upgrade)
- 🎨 Built for easy customization – plug in your own dataset or tweak architecture
- 🔍 Easily adaptable to other facial attribute detection tasks (e.g., gender, emotion)

---

## 📋 Resources & Downloads
- **GitHub Repository:** [Age Detection Repo](https://github.com/shwet369/age-detection-app)
- **UTKFace Dataset:** [UTKFace on Kaggle](https://www.kaggle.com/datasets)

---

## 📝 License
This project is licensed under the **MIT License**.

---

## 🔗 Contact
- 📧 Email: [shwetabhoyar04@gmail.com](mailto:shwetabhoyar04@gmail.com)
- 👤 LinkedIn: [Shweta Bhoyar](https://www.linkedin.com/in/shweta-bhoyar-datascience/)
- 💻 GitHub: [shwet369](https://github.com/shwet369)

---

## 💥 Let the model guess your age – It might surprise you! 😎🌐

Developed with ❤️ by **Shwet**

---
