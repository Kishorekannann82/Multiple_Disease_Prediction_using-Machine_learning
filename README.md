# Multiple Disease Prediction Web App 🏥

This is a Streamlit-based web application that can predict multiple diseases using trained Machine Learning models. The following diseases are supported:
- **Diabetes Prediction**
- **Heart Disease Prediction**
- **Kidney Disease Prediction**
- **Parkinson's Disease Detection**
- **Breast Cancer Prediction**
- **Liver Disease Prediction**

Live Demo: [Click Here to Try the App](https://multipledisease-prediction-using-machine-learning-kishorelytics.streamlit.app/)

---

## 🚀 Features
- User-friendly interface built with **Streamlit**
- Supports six different disease predictions
- Uses pre-trained ML models (`.pkl` files)
- Easy to extend or customize

---

## 🧑‍💻 Tech Stack
- **Python**
- **Streamlit**
- **scikit-learn** (for model training)
- **pickle** (for model loading)
- **streamlit-option-menu** (for sidebar navigation)

---

## 📂 Project Structure
├── saved_models/ # Contains all trained models (.pkl)
│ ├── diabetes.pkl
│ ├── heart.pkl
│ ├── kidney.pkl
│ ├── Parkinsons.pkl
│ ├── breast_cancer.pkl
│ └── liver.pkl
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

## 🔧 Setup Instructions

### 1. Clone the Repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create a Virtual Environment (Optional but Recommended):
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3. Install Dependencies:
pip install -r requirements.txt
4. Run the App Locally:
streamlit run app.py
✅ Requirements
All required packages are listed in requirements.txt. Some key packages:

streamlit

pandas

numpy

scikit-learn

streamlit-option-menu

🌐 Deployment (Streamlit Cloud)
Push your project to GitHub.

Login to Streamlit Cloud.

Connect your GitHub repo & deploy.

Ensure your .pkl models are inside the repo (Git LFS not needed for smaller models).

Done!

