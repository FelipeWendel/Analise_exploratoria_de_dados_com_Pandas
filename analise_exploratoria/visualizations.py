import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import os

# Pasta de exportação
EXPORT_DIR = "assets/plots"
os.makedirs(EXPORT_DIR, exist_ok=True)

# Mapa de calor de correlações
def plot_heatmap(df):
    corr = df.corr(numeric_only=True)
    fig = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.index),
        annotation_text=corr.round(2).values,
        colorscale='Viridis'
    )
    fig.write_image(f"{EXPORT_DIR}/heatmap.png")
    return fig

# Dispersão entre idade e tarifa
def plot_dispersion(df, idade_min, idade_max):
    df_filtrado = df[(df['age'] >= idade_min) & (df['age'] <= idade_max)]
    fig = px.scatter(df_filtrado, x='age', y='fare', color='survived',
                     title='Dispersão: Idade vs Tarifa',
                     labels={'age': 'Idade', 'fare': 'Tarifa'})
    fig.write_image(f"{EXPORT_DIR}/dispersao_idade_tarifa.png")
    return fig

# Pizza de sobrevivência por classe
def plot_pie_survival_by_class(df, classes_selecionadas):
    df_filtrado = df[df['class'].isin(classes_selecionadas)]
    df_grouped = df_filtrado.groupby('class')['survived'].mean().reset_index()
    fig = px.pie(df_grouped, names='class', values='survived',
                 title='Taxa de Sobrevivência por Classe',
                 color_discrete_sequence=px.colors.qualitative.Set3)
    fig.write_image(f"{EXPORT_DIR}/pizza_sobrevivencia_classe.png")
    return fig