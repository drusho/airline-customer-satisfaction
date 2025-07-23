

## Airline Customer Satisfaction: A Data Engineering Project

This project showcases an end-to-end data engineering workflow, from data ingestion and cleaning to predictive modeling. The goal is to identify the key factors that contribute to airline customer satisfaction using a logistic regression model.

---
## Table of Contents
- [Airline Customer Satisfaction: A Data Engineering Project](#airline-customer-satisfaction-a-data-engineering-project)
- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Methodology](#methodology)
- [Results](#results)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Tech Stack \& Skills Demonstrated](#tech-stack--skills-demonstrated)

---
## Project Overview

In the highly competitive airline industry, customer satisfaction is a key differentiator. This project aims to answer the question: **"What factors contribute to positive airline customer satisfaction?"**

To address this, I developed a data pipeline and a predictive model to analyze customer feedback and identify significant drivers of satisfaction.

The key findings indicate that factors such as **check-in service, departure/arrival time convenience, and customer type** have a statistically significant impact on customer satisfaction.

## Data Source

The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/sjleshrac/airlines-customer-satisfaction) and provided by 'Invistico Airlines'. It contains 129,880 survey responses from airline customers, covering various aspects of their flight experience.

## Methodology

The project followed a structured data engineering and analysis process:

1. **Data Ingestion and Exploration**: The raw CSV data was ingested into a Pandas DataFrame. An initial exploratory data analysis (EDA) was conducted to understand the data's structure, identify missing values, and examine summary statistics.
    
2. **Data Cleaning and Preprocessing**:
    
    - **Missing Values**: Missing values in the `Arrival Delay in Minutes` column were imputed using the median due to the skewed distribution of the data.
    - **Outlier Treatment**: Outliers in continuous variables (`Flight Distance`, `Departure Delay in Minutes`, `Arrival Delay in Minutes`) were capped using the interquartile range (IQR) method.
    - **Data Transformation**: The categorical target variable `satisfaction` was converted to a binary format (1 for 'satisfied', 0 for 'dissatisfied'). Categorical features (`Customer Type`, `Type of Travel`, `Class`) were one-hot encoded.
        
3. **Feature Engineering and Selection**:
    
    - **Multicollinearity**: Variance Inflation Factor (VIF) was used to detect and remove features with high multicollinearity (VIF > 10).
    - **Backward Stepwise Elimination**: A logistic regression model was iteratively fitted, and features with p-values greater than 0.05 were removed to arrive at the final set of significant predictors.
        
4. **Modeling and Evaluation**:
    
    - A **logistic regression model** was trained on the cleaned and preprocessed data.
    - The data was split into an 80/20 training and testing set, and features were scaled using `RobustScaler`.
    - The model's performance was evaluated using a confusion matrix, accuracy score, and a classification report.
        

## Results

The final logistic regression model achieved an **accuracy of 70%**. The key predictors of customer satisfaction were:

- **Check-in service**
- **Departure/Arrival time convenience**
- **Age**
- **Arrival Delay in Minutes**
- **Departure Delay in Minutes**
- **Flight Distance**
- **Class**
- **Type of Travel**
- **Customer Type**
    

All predictors in the final model had a p-value of less than 0.05, leading to the rejection of the null hypothesis. This confirms a statistically significant relationship between these factors and customer satisfaction.

## Limitations

- The dataset lacks a specific timeframe, making it difficult to analyze temporal trends.
- The logistic regression model assumes a linear relationship between the predictors and the log-odds of the outcome, which may not fully capture the complexity of customer satisfaction.
    

## Future Work

- **Seasonal Analysis**: Analyze how customer satisfaction varies across different travel seasons.
- **Enriching the Dataset**: Incorporate external data, such as social media sentiment, to build a more comprehensive model.


---
## Tech Stack & Skills Demonstrated

-   **Data Engineering:** ETL, Data Ingestion, Data Cleaning, Data Preprocessing
-   **Statistical Analysis:** Exploratory Data Analysis (EDA), Feature Engineering, Multicollinearity Analysis (VIF), Backward Stepwise Elimination
-   **Predictive Modeling:** Logistic Regression, Model Evaluation (Accuracy, Precision, Recall, F1-Score)
-   **Programming & Libraries:**
    -   **Python:** Pandas, NumPy, Scikit-learn, Statsmodels
    -   **Visualization:** Matplotlib, Seaborn, Missingno