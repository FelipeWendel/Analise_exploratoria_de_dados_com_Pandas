import pandas as pd
import seaborn as sns

def load_titanic_data():
    df = sns.load_dataset('titanic')
    
    # Correção do aviso: atribuição direta em vez de inplace
    df['age'] = df['age'].fillna(df['age'].median())
    df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
    
    # Remoção de colunas com muitos nulos
    df.drop(columns=['deck', 'embark_town'], inplace=True)
    
    return df