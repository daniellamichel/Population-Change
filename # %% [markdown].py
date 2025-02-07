# %% [markdown]
# ## INFO 348 Project: Population Change

# %%
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import pingouin as pg


# %%
population_df = pd.read_csv("population.csv")

# %%
#Statistical Associations
summary_stats = population_df[['Births', 'Deaths', 'Net International Migration']].describe()
print(summary_stats)

# %% [markdown]
# ### This Statistical association shows me that births and deaths have higher average values compared to migration, suggesting that natural population growth (births minus deaths) are higher contributors to overall population change.

# %%
# Temporal Analysis
population_df['Births Contribution'] = population_df['Births'].diff().fillna(0)
population_df['Deaths Contribution'] = population_df['Deaths'].diff().fillna(0)
population_df['Migration Contribution'] = population_df['Net International Migration'].diff().fillna(0)

# Visualize contributions over time
plt.figure(figsize=(12, 6))

plt.plot(population_df['Year'], population_df['Births Contribution'], label='Births Contribution')
plt.plot(population_df['Year'], population_df['Deaths Contribution'], label='Deaths Contribution')
plt.plot(population_df['Year'], population_df['Migration Contribution'], label='Migration Contribution')

plt.title('Contributions to Population Change Over Time')
plt.xlabel('Year')
plt.ylabel('Population Change')
plt.legend()
plt.show()

# %% [markdown]
# ### This temporal analysis visualization shows me that during the 1990s, births and deaths had a significant rise and fall, while migration stayed at 0. Similarly, in 2000, all three categories had a rise and fall, and again in 2010. Overall, migration seems to have been moving in an upward trend at the most constant rate in comparison to births and deaths. Migration was the most significant factor in population.

# %%
#Casual Hypothesis
correlation_births = pg.corr(population_df['Births'], population_df['Residual'])
correlation_deaths = pg.corr(population_df['Deaths'], population_df['Residual'])
correlation_migration = pg.corr(population_df['Net International Migration'], population_df['Residual'])
print("Correlation Result - Births and Population Change:")
print(correlation_births)
print("\nCorrelation Result - Deaths and Population Change:")
print(correlation_deaths)
print("\nCorrelation Result - Net International Migration and Population Change:")
print(correlation_migration)

# %% [markdown]
# ### This casual hypothesis tells me that the correlation analysis reveals significant (positive) correlations between population change and births (r = 0.140), deaths (r = 0.145), and migration (r = 0.124). In conclusion, all three correlations are highly significant and none is more or less significant than the other (or there is not a large enough gap between their influences to population).

# %% [markdown]
# ### In Conclusion: I believe that birth, death and migration play an equally significant role in population and changes. This is due to their statistical association determining births and deaths as greater contributors to population change, while temporal analysis determined migration as the greatest contributor. Thirdly, casual hypothesis determined that all three have are equally significant contributors to population. Finally, I can conclude that all three have an equally significant effect on population change. 

# %% [markdown]
# Note: Thank you for a great class, Professor, and I hope you have an amazing winter break and happy holidays! :)
