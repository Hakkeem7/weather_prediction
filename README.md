# Weather Prediction using Machine Learning:
### STREAMLIT : http://localhost:8501/
## Project Overview:
#### This project focuses on predicting weather conditions using Machine Learning algorithms. Multiple models were implemented and compared to evaluate their performance on the dataset.The primary goal is to identify the most accurate model for weather prediction.
##  Dataset Description:
#### The dataset contains meteorological features such as:
#### * Precip Type (encoded: rain = 1, snow = 2)
#### * Humidity
#### * Wind Speed (km/h)
#### * Wind Bearing (degrees)
#### * Visibility (km)
#### * Cloud Cover
#### * Pressure (millibars)
## Data Preprocessing:
#### The following preprocessing steps were performed:
### Removed irrelevant columns:
#### * Formatted Date
#### * Summary
#### * Temperature
#### * Apparent Temperature
#### * Daily Summary
### Converted categorical data:
#### 1.Precip Type encoded into numerical values
#### 2.Checked for missing values and cleaned the dataset 
## Models Used:
### 1. Logistic Regression:
#### * A linear model used for classification
#### * Performs well for linearly separable data 
### 2. K-Nearest Neighbors (KNN):
#### A distance-based algorithm
### Parameter used:
#### * n_neighbors = 10
## Model Performance
## Model
### 1.Logistic Regression:
#### *Performance(88%)
#### *Low Accuracy
### 2.KNN (k=10):
#### *High Accuracy(89%)
## Analysis:
#### Logistic Regression underperformed because the dataset is likely non-linear KNN performed better as it captures local patterns in data Choosing k = 10 helped balance bias and variance
## Implementation Steps:
#### 1.Load dataset
#### 2.Preprocess data (clean + encode)
#### 3.Split dataset into training and testing sets
#### 4.Train Logistic Regression model
#### 5.Train KNN model (k = 10)
#### 6.Compare model accuracies
## Technologies Used:
#### * Python
#### * Pandas
#### * NumPy
#### * Scikit-learn
