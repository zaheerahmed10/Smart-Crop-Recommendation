# 🌱 Smart Crop Recommendation System

An intelligent Machine Learning-based web application that recommends the most suitable crop to grow based on soil nutrients and environmental conditions.

The system uses a trained **Random Forest Classifier** to analyze input values and predict the best crop for the given agricultural conditions.

## 🚀 Project Overview

Choosing the right crop is important for improving agricultural productivity. This project helps farmers and users make better crop selection decisions using Machine Learning.

Users enter soil and weather-related parameters, and the system predicts a suitable crop based on the trained ML model.

## ✨ Features

- 🌾 Crop recommendation using Machine Learning
- 🌱 Random Forest classification model
- 🧪 Soil nutrient analysis
- 🌡️ Temperature and humidity inputs
- 💧 Rainfall and soil pH consideration
- 💻 User-friendly web interface
- 📱 Responsive frontend design
- ⚡ Real-time crop prediction

## 🧠 Machine Learning Model

Several Machine Learning algorithms were explored during model development.

The **Random Forest Classifier** was selected as the final model, achieving approximately **99% accuracy** on the test dataset.

### Input Features

| Feature | Description |
|---|---|
| N | Nitrogen content in soil |
| P | Phosphorus content in soil |
| K | Potassium content in soil |
| Temperature | Temperature in Celsius |
| Humidity | Relative humidity |
| pH | Soil pH value |
| Rainfall | Rainfall in mm |

### Target

The model predicts the recommended crop based on the provided input features.

## 🛠️ Technologies Used

- Python
- Machine Learning
- Scikit-learn
- Random Forest Classifier
- Flask
- Pandas
- NumPy
- Joblib
- HTML
- CSS

## 📂 Project Structure

```text
Smart-Crop-Recommendation/
│
├── app.py
├── requirements.txt
│
├── models/
│   └── crop.pkl
│
└── templates/
    └── index.html
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/zaheerahmed10/Smart-Crop-Recommendation.git
```

### 2. Open the Project Folder

```bash
cd Smart-Crop-Recommendation
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

Enter the required agricultural values and click the prediction button to get a crop recommendation.

## 📊 Dataset

The project uses the Crop Recommendation Dataset by Atharva Ingle from Kaggle.

[Download Dataset – Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

## 🎯 Project Objective

The main objective of this project is to demonstrate how Machine Learning can be used in agriculture to support data-driven crop selection and smarter farming decisions.

## 👨‍💻 Author

**Zaheer Ahmed**

GitHub: [@zaheerahmed10](https://github.com/zaheerahmed10)

---

⭐ If you find this project useful, consider giving it a star on GitHub!
