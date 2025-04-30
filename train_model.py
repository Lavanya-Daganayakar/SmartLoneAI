import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# 1. Create dummy data
data = {
    'age': np.random.randint(21, 60, 100),
    'annual_income': np.random.randint(200000, 1500000, 100),
    'credit_cards': np.random.randint(0, 10, 100),
    'loans_taken': np.random.randint(0, 5, 100),
    'cibil_score': np.random.randint(300, 900, 100)
}

df = pd.DataFrame(data)

# 2. Separate features and target
X = df[['age', 'annual_income', 'credit_cards', 'loans_taken']]
y = df['cibil_score']

# 3. Train Model
model = RandomForestRegressor()
model.fit(X, y)

# 4. Save Model
pickle.dump(model, open('ai_model/cibil_model.pkl', 'wb'))

print("✅ Model trained and saved successfully!")
