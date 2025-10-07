# InternPe-Breast-Cancer-Prediction-using-Machine-learning
A machine learning-based diagnostic system that predicts whether breast cancer is benign or malignant using clinical measurement data. This project helps in early detection and classification of breast cancer tumors.

## 📋 Project Overview

This project implements a Support Vector Machine (SVM) classifier to predict breast cancer diagnosis based on 30 clinical features extracted from digitized images of fine needle aspirate (FNA) of breast masses.

## 🎯 Features

- **Real-time Prediction**: Interactive web interface for instant diagnosis prediction
- **Clinical Feature Input**: 30 different clinical measurements via sliders
- **Model Evaluation**: Display of accuracy and classification metrics
- **User-friendly Interface**: Built with Streamlit for easy interaction
- **Medical-grade Analysis**: Based on widely recognized Wisconsin dataset

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Classification Algorithm**: Support Vector Machine (SVM)

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/breast-cancer-prediction.git
cd breast-cancer-prediction
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
streamlit run App5.py
```

## Project structure

Breast-Cancer-Prediction/
│
├── App5.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── assets/
│   └── images/           # Screenshots and demo images
└── data/
    └── (optional)        # Local dataset backup

    
💻 How to Use

1. Adjust Clinical Parameters: Use the sidebar sliders to input patient's clinical measurements
2. Get Prediction: The system automatically predicts diagnosis (Benign/Malignant)
3. View Model Performance: Check accuracy and classification metrics
4. Interpret Results: Understand the prediction confidence and model reliability

🤖 Machine Learning Model

· Algorithm: Support Vector Machine (SVC)
· Dataset: Wisconsin Breast Cancer Diagnostic dataset (569 instances)
· Training-Test Split: 80-20 split with random_state=42
· Target Encoding:
  · 0 = Benign (Non-cancerous)
  · 1 = Malignant (Cancerous)

📈 Model Performance

· Accuracy: Typically 90%+ on test data
· Precision & Recall: High scores for both classes
· Classification Report: Detailed performance metrics

🔬 Medical Significance

· Early Detection: Helps in identifying potential cancer cases
· Clinical Decision Support: Assists medical professionals in diagnosis
· Feature Importance: Highlights most significant clinical indicators
· Non-invasive: Based on FNA test results

⚠️ Important Disclaimer

This application is for educational and demonstration purposes only. It should NOT be used for actual medical diagnosis. Always consult qualified healthcare professionals for medical decisions.


📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author

Madiha Manzoor
