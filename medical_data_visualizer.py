import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# 1. Add overweight column
df['BMI'] = df['weight'] / ((df['height']/100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# 2. Normalize cholesterol and gluc
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    # 3. Melt DataFrame
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 4. Group and count
    df_cat = df_cat.value_counts().reset_index(name='total')

    # 5. Draw the catplot
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig

    return fig

def draw_heat_map():
    # 6. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 7. Calculate correlation matrix
    corr = df_heat.corr()

    # 8. Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 9. Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 10. Draw heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, square=True, linewidths=.5, cbar_kws={'shrink': .5})

    return fig
