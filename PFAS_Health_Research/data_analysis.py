# Load and prepare the data
import pandas as pd
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np
import statsmodels.api as sm

# Load dataset
dataset = pd.read_csv(r"C:\Users\idhan\Downloads\pfas_health_issues\data\merged_california_county_pfas_low_birth_weight.csv")

#ordinary least squares multiple linear regression model
columns = [
    'PFPA', 'PFHA', 'PFHPA', 'PFOA', 'PFNA', 'PFNDCA', 'PFUNDCA',
    'PFDOA', 'PFODA', 'PFBSA', 'PFHXSA', 'PFHPSA',
    'PFOS', 'PFNS', 'PFDSA', 'PFAS_total', '% Low Birth Weight'
]



# Load dataset


# Define PFAS and target
pfas_columns = [
    'PFPA', 'PFHA', 'PFHPA', 'PFOA', 'PFNA', 'PFNDCA', 'PFUNDCA',
    'PFDOA', 'PFODA', 'PFBSA', 'PFHXSA', 'PFHPSA',
    'PFOS', 'PFNS', 'PFDSA', 'PFAS_total'
]
y = dataset['% Low Birth Weight'].fillna(0)

# Collect metrics
metrics_results = []



models = {
    'Ridge': Ridge(),
    'Lasso': Lasso(),
    'ElasticNet': ElasticNet(),
    'Linear': LinearRegression(),
    'RandomForest': RandomForestRegressor(random_state=42)
}

for chem in pfas_columns:
    X = dataset[[chem]].fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        metrics_results.append({
            'PFAS': chem,
            'Model': name,
            'R2': r2,
            'MAE': mae,
            'MSE': mse,
            'RMSE': rmse
        })
# print(metrics_results)
metrics_df = pd.DataFrame(metrics_results)
metrics_df.to_csv("results.csv", index=False)