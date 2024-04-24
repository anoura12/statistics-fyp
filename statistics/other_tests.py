import pandas as pd
from scipy.stats import mannwhitneyu, wilcoxon, kruskal, friedmanchisquare

# Example data loading
# Assuming 'data' is your DataFrame
data = pd.read_csv('combined_scores.csv')
# Mann-Whitney U Test between Athena and Bob in Round 1
athena_round1 = data[(data['Cohort'] == 'Athena') & (data['Round'] == 'Round2')]['Points']
bob_round1 = data[(data['Cohort'] == 'Bob') & (data['Round'] == 'Round2')]['Points']
stat, p = mannwhitneyu(athena_round1, bob_round1)
print(f'Mann-Whitney U test between Athena and Bob in Round 2: U={stat}, p={p}')

# Wilcoxon Signed-Rank Test for Athena from Round 1 to Round 2
bob_round2 = data[(data['Cohort'] == 'Bob') & (data['Round'] == 'Round2')]['Points']
stat, p = wilcoxon(bob_round1, bob_round2)
print(f'Wilcoxon Signed-Rank Test for Bob from Round 1 to Round 2: stat={stat}, p={p}')
