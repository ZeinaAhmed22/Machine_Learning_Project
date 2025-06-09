# Cancer Survival Prediction – Machine Learning Project #

## Project Description ##
This project predicts the survival outcome of cancer patients using a machine learning model trained on a rich clinical and demographic dataset. It uses a Random Forest classifier trained on 29 features, and the final model is deployed as a web app using Streamlit.

## Dataset Overview ##
The dataset (from Kaggle) includes medical and lifestyle data for cancer patients such as:

- Tumor size
- Cancer stage
- Treatment type
- Smoking and alcohol history
- Genetic and family history
- Healthcare access and cost
- Comorbidities like diabetes, hypertension, heart disease
- Demographic data such as gender, age, and location

The target column is Survival Prediction, with two classes:
1. Survived (1)
2. Not Survived (0)

## Model Used ##
Algorithm: Random Forest Classifier
Features: 29 selected and encoded features
Preprocessing: MinMaxScaler
Evaluation Metrics: Accuracy, F1-score, AUC-ROC

## Web App (Streamlit) ##
Users can enter patient data into the web interface and get an instant survival prediction based on the trained model.

To launch the app locally:
```
streamlit run streamlit_app.py
```

## Project Structure ##
```
Cancer-Survival-Prediction/
│
├── Cleaned_Train.csv          # Final cleaned dataset used for training
├── Train.csv                  # Original training dataset from Kaggle
├── X_features.csv             # Features after preprocessing
├── y_target.csv               # Labels (Survival Prediction)
│
├── best_rf_model.pkl          # Saved trained model
├── scaler.pkl                 # Saved MinMaxScaler
│
├── Machine_Learning_Project_Zeina (3).ipynb  # Jupyter notebook with full ML pipeline
├── Machine_Learning_Report_Zeina             # Report of the project
├── streamlit_app.py           # Streamlit app for deployment
├── requirements.txt           # List of required Python packages
├── README.md                  # Project overview and instructions
└── streamlit/                 # (Optional folder for Streamlit assets or deployment)
```

## How to Run the Project ##
1. Clone the repo or download the files
2. (Optional) Create a virtual environment
3. Install requirements:
```
pip install -r requirements.txt
```
4. Run the Streamlit app:
```
streamlit run streamlit_app.py
```
## Video Drive Link ##
https://drive.google.com/drive/folders/1_FCVw1lKUrVcrIk3_PmTv_CH6uTThlCB?usp=sharing
