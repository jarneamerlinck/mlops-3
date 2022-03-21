import pandas as pd

# Visualisations
def bar_plot(df: pd.DataFrame, feature: str, figsize=(10,3), legend=True):
    """Shows a barplot and table for the relationship between a categorical feature and our outcome variable

    Args:
        df (pd.DataFrame): training dataframe
        feature (str): feature of interest
        figsize (tuple, optional): size of figure. Defaults to (10,3).
        legend (bool, optional): show legend. Defaults to True.
    """
    survived = df[df['Survived'] == 1][feature].value_counts()
    dead = df[df['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived,dead],index=['Survived','dead'])
    print(df)
    df.plot(kind='barh',stacked=True, figsize=figsize, legend=legend)