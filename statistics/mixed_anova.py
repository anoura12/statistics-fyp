import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import mixedlm
from statsmodels.stats.anova import AnovaRM
from scipy.stats import shapiro, levene
from scipy import stats
import matplotlib.pyplot as plt

# Example data creation
# Replace this with your actual data loading method
data = pd.read_csv('combined_scores.csv')
data['Points'], best_lambda = stats.boxcox(data['Points'])
print(f"Best lambda for transformation: {best_lambda}")

# Check normality for each group
for cohort in data['Cohort'].unique():
    for round in data['Round'].unique():
        group_data = data[(data['Cohort'] == cohort) & (data['Round'] == round)]['Points']
        stat, p = shapiro(group_data)
        print(f'Normality for {cohort}, {round}: Statistics={stat}, p-value={p}')

# Check homogeneity of variances
round1 = data[data['Round'] == 'Round1']['Points']
round2 = data[data['Round'] == 'Round2']['Points']
stat, p = levene(round1, round2)
print(f'Levene’s Test for Homogeneity of variances: Statistics={stat}, p-value={p}')

# Mixed ANOVA
data['Student Name'] = data['Student Name'].apply(str)
model = mixedlm("Points ~ C(Round)*C(Cohort)", data, groups=data["Student Name"])
result = model.fit()
print(result.summary())

# Plotting data
pd.pivot_table(data, values='Points', index='Student Name', columns=['Cohort', 'Round']).plot(kind='bar')
plt.ylabel('Points')
plt.title('Point Distribution by Cohort and Round')
plt.show()
