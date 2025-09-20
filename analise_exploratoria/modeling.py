from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
import pandas as pd

def train_model(df):
    df = pd.get_dummies(df[['survived', 'sex', 'class', 'age', 'embarked', 'grupo_familiar']], drop_first=True)
    X = df.drop('survived', axis=1)
    y = df['survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return model, accuracy_score(y_test, y_pred), roc_auc_score(y_test, y_pred)