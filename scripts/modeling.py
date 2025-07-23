import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def load_processed_data(file_path):
    """Loads the processed data."""
    return pd.read_csv(file_path)


def train_model(X, y):
    """Splits data, scales features, and trains a logistic regression model."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)

    return model, X_test_scaled, y_test


if __name__ == '__main__':
    processed_data_path = '../data/processed/cleaned_data.csv'
    df = load_processed_data(processed_data_path)

    # Define your final predictors and target variable
    predictors = [...]
    target = 'satisfaction'

    X = df[predictors]
    y = df[target]

    model, X_test_scaled, y_test = train_model(X, y)

    y_pred = model.predict(X_test_scaled)

    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
