"""
CSV Summary Statistics
---------------------
Reads a CSV file and prints basic statistics for numeric columns.

Steps for Beginners:
1. Import pandas for data analysis.
2. Read a CSV file using pandas.read_csv().
3. Use .describe() to get summary statistics.
4. Print the results.
"""

# 1. Import pandas
import pandas as pd

# 2. Read CSV file
def analyze_csv(filename):
    df = pd.read_csv(filename)
    # 3. Get summary statistics
    print(df.describe())

# 4. Main program
if __name__ == "__main__":
    file = input("Enter CSV filename: ")
    analyze_csv(file)
