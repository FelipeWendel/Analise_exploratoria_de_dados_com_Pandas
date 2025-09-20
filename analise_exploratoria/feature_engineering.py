import pandas as pd

def engineer_features(df):
    df['grupo_familiar'] = df['sibsp'] + df['parch']
    df['faixa_tarifa'] = pd.cut(df['fare'], bins=[0, 20, 50, 100, 600],
                                labels=['Baixa', 'Média', 'Alta', 'Luxo'])
    if 'name' in df.columns:
        df['title'] = df['name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    return df