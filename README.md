# Horse Health Prediction using Machine Learning and Streamlit

## Introduction

This project aims to predict a horse's health using machine learning algorithms and deploying the model in a Streamlit web application. Horse health is crucial, and early detection of health issues can be life-saving. This application allows users to input various features related to the horse's condition and get predictions about its health status.

https://horsehealthprediction.streamlit.app/

## Features

- Machine Learning Models: We have trained several machine learning models using historical horse health data to make predictions about a horse's health status.
- Streamlit Web App: The project is deployed as a Streamlit web application, making it easy for users to interact with the model and get predictions.
- User-Friendly Interface: The web app provides a user-friendly interface for users to input relevant data and obtain health predictions.

## Machine Learning Algorithms

We have used a variety of machine-learning algorithms to predict horse health. Some of the algorithms include:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

The algorithm can be selected by the user in the web application for predictions.

## Data

The machine learning models are trained on a dataset containing information about various health-related parameters and conditions of horses. The dataset is included in this repository but it can be obtained from Kaggle.

## Getting Started

To run the project locally, follow these steps:

1. Clone this repository to your local machine:
git clone [https://github.com/perarulalan15/Horse-health-prediction.git](https://github.com/perarulalan15/Horse_health_prediction.git)

2. Install the required Python packages:
pip install -r requirements.txt

3. Run the Streamlit app:
streamlit run app.py

4. Access the web app in your browser at the provided URL (usually `http://localhost:8501`).

## Usage

1. Open the web application by running `streamlit run app.py`.
2. Input the relevant information about the horse's condition.
3. Click the "Predict" button for the health status prediction.

## Contributions

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to your fork: `git push origin feature-name`
5. Create a pull request to the main repository.

## Contact

If you have any questions or suggestions, feel free to contact us at [v.perarulalan15@gmail.com].
