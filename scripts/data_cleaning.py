import pandas as pd
import numpy as np


def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)


def impute_missing_values(df):
    """Imputes missing values in 'Arrival Delay in Minutes' with the median."""
    df_imputed = df.copy()
    df_imputed['Arrival Delay in Minutes'].fillna(
        df_imputed['Arrival Delay in Minutes'].median(), inplace=True)
    return df_imputed


def cap_outliers(df, column):
    """Caps outliers in a specified column using the IQR method."""
    df_capped = df.copy()
    q1 = df_capped[column].quantile(0.25)
    q3 = df_capped[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df_capped[column] = np.clip(df_capped[column], lower_bound, upper_bound)
    return df_capped


if __name__ == '__main__':
    raw_data_path = '../data/raw/Airline_customer_satisfaction.csv'
    processed_data_path = '../data/processed/cleaned_data.csv'

    df = load_data(raw_data_path)
    df = impute_missing_values(df)

    outlier_columns = ['Flight Distance',
                       'Departure Delay in Minutes', 'Arrival Delay in Minutes']
    for col in outlier_columns:
        df = cap_outliers(df, col)

    # ... add encoding steps here ...

    df.to_csv(processed_data_path, index=False)
