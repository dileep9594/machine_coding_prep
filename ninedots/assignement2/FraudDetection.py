import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

class FraudDetectionModelBuilder:
    def __init__(self, data_frame):
        self.df = data_frame

    def select_features(self,df,features,target_features):
            """Select relevant features and target variable."""
            X = df[features]
            y = df[target_features]
            return X, y

    def build_preprocessor(self):
        features = ['creditLimit', 'availableMoney', 'transactionAmount', 'posEntryMode', 'posConditionCode',
                        'merchantCategoryCode', 'currentBalance', 'cardPresent', 'expirationDateKeyInMatch']
        target_features = 'isFraud'
        X,y = self.select_features(self.df,features,target_features)
        """Build the preprocessing pipeline."""
        numeric_features = X.select_dtypes(include=['float64']).columns
        categorical_features = X.select_dtypes(include=['object']).columns

        numeric_transformer = SimpleImputer(strategy='mean')
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        return ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

    def build_model(self):
        """Build a RandomForestClassifier pipeline."""
        preprocessor = self.build_preprocessor()
        return Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
        ])
    
    def train_model(self,model, X_train, y_train):
        """Train the model."""
        model.fit(X_train, y_train)
        return model


    def build_fraud_model(self,): 
        try:
            if self.df is not None:
                print("dileep--0")
                model = self.build_model()
                features = ['creditLimit', 'availableMoney', 'transactionAmount', 'posEntryMode', 'posConditionCode',
                        'merchantCategoryCode', 'currentBalance', 'cardPresent', 'expirationDateKeyInMatch']
                target_features = 'isFraud'
                X, y = self.select_features(self.df,features,target_features)
                print("dileep--1")
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                print("dileep--2")
                trained_model = self.train_model(model, X_train, y_train)
                # Make predictions on the test set
                y_pred = model.predict(X_test)
                # Evaluate the model
                accuracy = accuracy_score(y_test, y_pred)
                conf_matrix = confusion_matrix(y_test, y_pred)
                classification_rep = classification_report(y_test, y_pred)

                # Display evaluation metrics
                print(f"Accuracy: {accuracy:.4f}")
                print("\nConfusion Matrix:")
                print(conf_matrix)
                print("\nClassification Report:")
                print(classification_rep)
                
            else:
                raise Exception("Data not loaded.")
        except Exception as e:
            print(f"Error building fraud model: {str(e)}")

