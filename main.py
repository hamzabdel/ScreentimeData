import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import layers, models

df = pd.read_csv('C:/Users/hamza/OneDrive/Desktop/GitHub Projects/Neural Network/DiabetesPrediction/diabetes_prediction_dataset.csv')

X = df.drop('Diabetes', axis=9)
y = df['Diabetes']
