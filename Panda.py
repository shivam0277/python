#PANDAS
# Pandas is an open-source Python library used for data manipulation, analysis and cleaning. It provides fast 
# and flexible tools to work with tabular data, similar to spreadsheets or SQL tables.

#A Series is a one-dimensional labeled array in Pandas.

import pandas as pd
# Creating a Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)

# Features:
# 1D data
# Has index + values
# Supports vectorized operations
# Can hold any data type


#A DataFrame is a two-dimensional labeled table (rows + columns).

import pandas as pd
data = {
    'Name': ['Shivam', 'Amit', 'Riya'],
    'Age': [22, 25, 23]
}

df = pd.DataFrame(data)
print(df)

# Features:
# 2D structure
# Columns can have different data types
# Has row index and column names
# Easy for data manipulation and analysis

df = pd.read_csv("data.csv")   # default: comma-separated
print(df.head())   


df.head()
# Shows the first 5 rows of the DataFrame.

# Why it’s useful
# Quickly checks if the data loaded correctly.
# Helps you preview the structure and values.
# Prevents printing the entire dataset (especially large files).

# Optional parameter
# df.head(10)   # Displays the first 10 rows


df.info()
# Displays summary information about the DataFrame.

# What it shows
# Total rows
# Column names
# Non-null counts (helps identify missing values)
# Data types (int64, float64, object, etc.)
#Memory usage

# Why it’s useful
# Checks data types before analysis.
# Identifies missing data.
# Good for understanding dataset structure.


df.describe()
# Generates statistical summary for numeric columns.

# What stats it shows
# count (number of non-null values)
# mean
# std (standard deviation)
# min
# 25%, 50%, 75% percentiles
# max

# Why it’s useful
# Gives a quick snapshot of data distribution.
# Helps detect outliers.
# Useful in data analysis & ML preprocessing.
# For all columns (including strings):
# df.describe(include='all')

# loc – Label-based selection
# loc selects rows and columns using labels (names).

# Selecting rows using loc
df.loc[5]        # row with index label 5
df.loc[2:6]      # rows from index 2 to 6 (inclusive)

# Selecting columns using loc
df.loc[:, "Age"]               # all rows, only Age column
df.loc[:, ["Name", "Age"]]     # multiple columns

# Selecting rows + columns
df.loc[0:3, ["Name", "Age"]]

# Meaning:
# Rows 0 to 3
# Only Name and Age columns

# When to use loc?
# When you want to use index labels
# When selecting by column names
# When slicing by label is inclusive


# iloc – Index/Position-based selection
# iloc selects rows and columns by integer position (like lists).

#Selecting rows using iloc
df.iloc[0]        # first row
df.iloc[0:5]      # rows from position 0 to 4

#Selecting columns using iloc
df.iloc[:, 1]       # second column
df.iloc[:, 0:3]     # first 3 columns

#Selecting rows + columns
df.iloc[0:3, 0:2]

# Meaning:
# First 3 rows
# First 2 columns

# When to use iloc?
# When you want to select using numbers/positions
# When the index is not meaningful
# When slicing is end-exclusive (0:3 → rows 0,1,2)


# Filtering Rows in Pandas
# You filter rows in a DataFrame using boolean conditions.

#Filtering based on one condition
df[df["Age"] > 20]

# Shows rows where Age is greater than 20.
df[df["City"] == "Delhi"]

#Rows where City equals "Delhi".

#Filtering with multiple conditions
# AND condition:
df[(df["Age"] > 20) & (df["City"] == "Delhi")]

# OR condition:
df[(df["Age"] > 20) | (df["Age"] < 15)]

# NOT condition:
df[~(df["City"] == "Delhi")]

#Filtering using isin()
# For matching multiple values:
df[df["City"].isin(["Delhi", "Mumbai"])]

#Opposite (not in):
df[~df["City"].isin(["Delhi", "Mumbai"])]

#Filtering using string methods
#Use .str for string matching:

# Contains:
df[df["Name"].str.contains("am")]
# Starts with:
df[df["Name"].str.startswith("S")]
# Case-insensitive:
df[df["Name"].str.contains("delhi", case=False)]

#Filtering using loc
#Same as above but using .loc:
df.loc[df["Age"] > 20, :]

# Filter and select only few columns:
df.loc[df["Age"] > 20, ["Name", "City"]]

#Filtering using query()
#A more readable SQL-like syntax:
df.query("Age > 20 and City == 'Delhi'")


#Adding New Columns
#You can add new columns to a DataFrame in multiple ways.

#Add a column with constant value
df["Country"] = "India"

#Add a column based on existing columns
df["Total"] = df["Math"] + df["Science"]

#Add a column using a condition
df["Status"] = df["Marks"] >= 40

#Add a column using apply()
df["Name_Length"] = df["Name"].apply(len)

#Add a column using assign()
df = df.assign(AgeGroup = df["Age"] // 10)

#Handling Missing Values (NaN)
#Missing values in Pandas appear as NaN.

#fillna() → Replace missing values
# Fill with a fixed value:
df.fillna(0)

# Fill a specific column:
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill with method:
# Forward fill:
df.fillna(method='ffill')

# Backward fill:
df.fillna(method='bfill')

#Fill with different values for different columns:
df.fillna({"Age": 0, "City": "Unknown"})

#dropna() → Remove missing values
#Drop any row containing NaN:
df.dropna()

#Drop rows only if all values are NaN:
df.dropna(how='all')

#Drop rows if specific columns contain NaN:
df.dropna(subset=["Age", "City"])

#Drop columns with NaN:
df.dropna(axis=1)