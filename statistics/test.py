import pandas as pd
from scipy.stats import ttest_ind

def load_data(file_path):
    """Load data from a CSV file and return the 'Total' column."""
    data = pd.read_csv(file_path)
    return data['Total'].dropna()

def perform_ttest(data1, data2):
    """Perform Welch's t-test on two datasets and return the t-statistic and p-value."""
    t_stat, p_value = ttest_ind(data1, data2, equal_var=True)
    return t_stat, p_value

def main():
    # Paths to the datasets
    path_athena = 'athena.csv'
    path_bob = 'bob.csv'
    
    # Load data
    total_athena = load_data(path_athena)
    total_bob = load_data(path_bob)
    
    # Perform t-test
    t_stat, p_value = perform_ttest(total_athena, total_bob)
    
    # Print results
    print(f"T-Statistic: {t_stat}")
    print(f"P-Value: {p_value}")
    print("Athena v/s Bob - Critical Thinking Scores")
    if p_value < 0.05:
        
        print("We reject the null hypothesis. There is a significant difference between the groups.")
    else:
        print("We fail to reject the null hypothesis. There is no significant difference between the groups.")

if __name__ == "__main__":
    main()
