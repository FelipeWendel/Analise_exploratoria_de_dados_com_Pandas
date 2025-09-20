from scipy.stats import ttest_ind, f_oneway, spearmanr

def test_survival_by_sex(df):
    homens = df[df['sex'] == 'male']['survived']
    mulheres = df[df['sex'] == 'female']['survived']
    return ttest_ind(homens, mulheres)

def anova_idade_por_classe(df):
    grupos = [df[df['class'] == c]['age'] for c in df['class'].unique()]
    return f_oneway(*grupos)

def spearman_age_survival(df):
    return spearmanr(df['age'], df['survived'])