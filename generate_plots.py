from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import date

sns.set_theme(style="darkgrid")
plt.figure(figsize=(20, 10))
def ms_to_days(x): return x/(60*60*24)


df = pd.read_csv('table.csv')
df.set_index('id', inplace=True)
df = df.reindex(index=df.index[::-1])

df['diff_days'] = (df['arcland'] - df['arcdiff']).apply(ms_to_days)

df['arcdiff'] = df['arcdiff'].apply(date.fromtimestamp)
df['arcland'] = df['arcland'].apply(date.fromtimestamp)

df['month_year'] = df['arcdiff'].apply(lambda x: x.strftime('%b %Y'))

boxplot = sns.boxplot(
    x="month_year",
    y="diff_days",
    data=df,
    showfliers=False,
    palette="Set2"
)

boxplot.get_figure().savefig("boxplot.svg")
