import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 1000

# Possible values
genders = ['Male', 'Female']
married = ['Yes', 'No']
dependents = ['0', '1', '2', '3+']
education = ['Graduate', 'Not Graduate']
self_employed = ['Yes', 'No']
property_area = ['Urban', 'Rural', 'Semiurban']
car_models = ['Sedan', 'Hatchback', 'SUV', 'Convertible', 'Coupe', 'Van', 'Truck']

# Function to randomly generate loan approval based on heuristic
def approve_loan(row):
    if row['Credit_History'] == 1 and row['LoanAmount'] < 2500000 and row['ApplicantIncome'] > 30000:
        return 'Y'
    elif row['LoanAmount'] < 1500000 and row['Credit_History'] == 1:
        return 'Y'
    else:
        return 'N'

# Generate the data
df = pd.DataFrame({
    'Gender': np.random.choice(genders, n_samples),
    'Married': np.random.choice(married, n_samples),
    'Dependents': np.random.choice(dependents, n_samples),
    'Education': np.random.choice(education, n_samples),
    'Self_Employed': np.random.choice(self_employed, n_samples),
    'ApplicantIncome': np.random.randint(10000, 100000, n_samples),
    'CoapplicantIncome': np.random.randint(0, 50000, n_samples),
    'LoanAmount': np.random.randint(500000, 3000000, n_samples),
    'Loan_Amount_Term': np.random.choice([60, 120, 180, 240, 300, 360], n_samples),
    'Credit_History': np.random.choice([1, 0], n_samples, p=[0.8, 0.2]),
    'Property_Area': np.random.choice(property_area, n_samples),
    'Car_Model': np.random.choice(car_models, n_samples),
    'Car_Price': np.random.randint(500000, 4000000, n_samples),
})

# Add Target variable
df['Loan_Status'] = df.apply(approve_loan, axis=1)

# Save to CSV
df.to_csv('synthetic_car_loan_data.csv', index=False)
print("Synthetic dataset saved as 'synthetic_car_loan_data.csv'")
