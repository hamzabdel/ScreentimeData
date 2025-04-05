import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns

df = pd.read_csv('C:/Users/hamza/OneDrive/Desktop/GitHub Projects/Neural Network/DiabetesPrediction/diabetes_prediction_dataset.csv')

np_array = df.to_numpy()
