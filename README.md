# Age Detection App 🧠👶👴

A Deep Learning-based Age Prediction App using CNN and Streamlit.

## 🚀 Features
- Upload any human face image
- Predicts the person’s **age** (classification or regression)
- Simple UI built with Streamlit

## 🧠 Model
- Input shape: (100, 100, 3)
- CNN Architecture (Conv2D + MaxPooling2D + Dense)
- Trained on UTKFace dataset
- Accuracy: ~87% on validation data

## 📦 Dependencies

Install with:

bash
pip install -r requirements.txt
# 🧠 Age Detection Web App

This project is a deep learning-based age detection app that predicts the **approximate age group** of a person based on an uploaded face image. Built with **TensorFlow**, **Keras**, and **Streamlit**, it provides a clean UI to test real images using a trained CNN model.

---

## 📸 Demo

> Upload a face image, and the model will output a predicted age class and age range.

![demo](![app - Google Chrome 10-04-2025 11_51_42](https://github.com/user-attachments/assets/f6c71be8-aa88-4791-956e-38b491e13be0)
)

---

## 📂 Project Structure

age-detection-app/ ├── app.py # Streamlit application ├── model/ │ └── age_model.h5 # Trained CNN model ├── sample_images/ │ └── example1.jpg ├── requirements.txt # Python dependencies └── README.md # This file

yaml
Copy
Edit

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/age-detection-app.git
cd age-detection-app
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Start the Streamlit App
bash
Copy
Edit
streamlit run app.py
🔍 Model Details
Input Shape: (100, 100, 3)

Model Type: Convolutional Neural Network (CNN)

Dataset: UTKFace

Output: Age Class (0–10, 11–20, ..., 70+)

Accuracy: ~87% on validation set

🧪 Sample Age Classes
Class	Age Range
0	0 - 10
1	11 - 20
2	21 - 30
3	31 - 40
4	41 - 50
5	51 - 60
6	61 - 70
7	70+
✅ Requirements
nginx
Copy
Edit
streamlit
tensorflow
numpy
Pillow
Install with:

bash
Copy
Edit
pip install -r requirements.txt

📌 Note


## 📎 Resources & Downloads
- **GitHub Repository:** [GitHub Link](https://github.com/shwet369/Fine-tune-model/tree/https/github.com/shwet369/-_Data-science)

## 📜 License
This project is licensed under the **MIT License**.

## 🔗 Contact
- 📧 Email: [shwetabhoyar04@gmail.com](mailto:shwetabhoyar04@gmail.com)
- 🔗 LinkedIn: [Shweta Bhoyar](https://www.linkedin.com/in/shweta-bhoyar-datascience/)
- 💻 GitHub: [shwet369](https://github.com/shwet369)

---
🔥 **Explore Deep Learning Beyond Accuracy!** 🎭🚀
🙋‍♀️ About Me
Developed with ❤️ by Shwet
🔗 LinkedIn | 🌐 GitHub




