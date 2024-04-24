import pandas as pd

# Load the data from CSV files
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully:", file_path)
        return data
    except Exception as e:
        print("Error loading the data:", e)

# Calculate descriptive statistics
def calculate_statistics(data, column_name='Count'):
    stats = {
        'Mean': data[column_name].mean(),
        'Median': data[column_name].median(),
        'Standard Deviation': data[column_name].std(),
        'Variance': data[column_name].var(),
        'Minimum': data[column_name].min(),
        'Maximum': data[column_name].max(),
        'Total Sessions': data[column_name].count()
    }
    return stats

# Display the statistics in a table format (you can also use a library like tabulate for prettier output)
def display_table(stats_athena, stats_bob):
    print("\nDescriptive Statistics for Athena and Bob")
    print("Metric", "\t\t", "Athena", "\t\t", "Bob")
    for key in stats_athena.keys():
        print(f"{key}", "\t", f"{stats_athena[key]:.2f}", "\t\t", f"{stats_bob[key]:.2f}")

# Paths to the data files
path_athena = 'athena-doi.csv'
path_bob = 'bob-doi.csv'

# Load the datasets
data_athena = load_data(path_athena)
data_bob = load_data(path_bob)

# Calculate statistics
stats_athena = calculate_statistics(data_athena)
stats_bob = calculate_statistics(data_bob)

# Display the statistics
display_table(stats_athena, stats_bob)
