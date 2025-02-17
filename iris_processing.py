
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

#Load the dataset
df = pd.read_csv('data/Iris.csv')

# Identify the numeric columns (exclude the 'Species' column)
numeric_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

# Normalize the dataset (scale values between 0 and 1)
scaler_minmax = MinMaxScaler()
df_normalized = df.copy()
df_normalized[numeric_cols] = scaler_minmax.fit_transform(df[numeric_cols])

# Save the normalized dataset to a CSV file
df_normalized.to_csv('iris_normalized.csv', index=False)
print("Normalization completed. File saved as 'iris_normalized.csv'.")

# Standardize the dataset (mean = 0, standard deviation = 1)
scaler_standard = StandardScaler()
df_standardized = df.copy()
df_standardized[numeric_cols] = scaler_standard.fit_transform(df[numeric_cols])

# Save the standardized dataset to a CSV file
df_standardized.to_csv('iris_standardized.csv', index=False)
print("Standardization completed. File saved as 'iris_standardized.csv'.")
