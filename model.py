import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
import joblib

# Load your data (adjust paths as needed)
train_data = pd.read_csv("UNSW_NB15_training-set.csv")
test_data = pd.read_csv("UNSW_NB15_testing-set.csv")

# Split features and labels
X_train = train_data.drop(columns=['label'])
y_train = train_data['label']
X_test = test_data.drop(columns=['label'])
y_test = test_data['label']

# Preprocessing steps
categorical_features = X_train.select_dtypes(include=['object']).columns
numeric_features = X_train.select_dtypes(include=['int64', 'float64']).columns

# Define categorical and numeric transformers
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Create a column transformer with both transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features),
        ('num', numeric_transformer, numeric_features)
    ])

# Create a pipeline with the preprocessor and the classifier
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', GradientBoostingClassifier())])

# Fit the model to the training data
pipeline.fit(X_train, y_train)

# Save the trained pipeline to a file
joblib.dump(pipeline, "gbm_pipeline.pkl")

# Load the trained pipeline from the file
loaded_pipeline = joblib.load("gbm_pipeline.pkl")

# Predict on the test data
predictions = loaded_pipeline.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

# Function to simulate firewall decisions
def simulate_firewall(predictions):
    decisions = ['Block' if pred == 1 else 'Allow' for pred in predictions]
    return decisions

# Simulate firewall decisions based on the model's predictions
firewall_decisions = simulate_firewall(predictions)
print("Firewall Decisions Sample:", firewall_decisions[:10])
