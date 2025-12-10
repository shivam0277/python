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


#Basic groupby + count
#Count how many rows belong to each group:

df.groupby("City")["Age"].count()

#Counts the number of ages per city.
#Count for all columns:

df.groupby("City").count()

#groupby + sum
#Sum salary of each department:

df.groupby("Department")["Salary"].sum()


#Sum all numeric columns:

df.groupby("Department").sum()

#groupby + mean
#Get average age per city:

df.groupby("City")["Age"].mean()

#groupby on multiple columns
#Group by City and Gender:

df.groupby(["City", "Gender"])["Age"].mean()

#Using agg() for multiple aggregations
#Apply multiple functions at the same time:

df.groupby("City")["Age"].agg(["count", "sum", "mean"])

#Different aggregations for different columns:

df.groupby("City").agg({
    "Age": "mean",
    "Salary": "sum",
    "Name": "count"
})

#Naming the aggregated column
df.groupby("City")["Age"].agg(Average_Age="mean")


#Merging & Joining in Pandas
#Used to combine two DataFrames.

#Merge() — Most Common
#Works like SQL joins: inner, left, right, outer.

#Basic merge on a common column
result = pd.merge(df1, df2, on="ID")

#Left join
result = pd.merge(df1, df2, on="ID", how="left")

#Right join
result = pd.merge(df1, df2, on="ID", how="right")

#Outer join (union)
result = pd.merge(df1, df2, on="ID", how="outer")

#Inner join (intersection, default)
result = pd.merge(df1, df2, on="ID", how="inner")

#Merge on different column names
result = pd.merge(df1, df2, left_on="ID1", right_on="ID2")

#join() — Join on index
#Used when indexes are keys.

result = df1.join(df2, how="left")

#Join on columns after setting index:

df1.set_index("ID").join(df2.set_index("ID"))

#Concatenation (combining DataFrames vertically or horizontally)
#Row-wise concatenation (vertical)
result = pd.concat([df1, df2], axis=0)

#Column-wise concatenation (horizontal)
result = pd.concat([df1, df2], axis=1)

#Sorting by Multiple Columns
#Use sort_values().

#Sort by one column
df.sort_values("Age")

#Sort by multiple columns
df.sort_values(["City", "Age"])

#Sort with different orders per column
#sort by City ascending, Age descending:

df.sort_values(["City", "Age"], ascending=[True, False])

#Sort by index
df.sort_index()

#Basic usage
df["City"].value_counts()

#This returns:
# Unique city names
# Their counts
# Sorted in descending order (default)

# Example output:
# Delhi     10
# Mumbai     7
# Chennai    3


# Include missing values
# By default NaN is ignored.
# To count NaN as well:

df["City"].value_counts(dropna=False)

#Normalize (get percentages)
df["City"].value_counts(normalize=True)

# Example output:
# Delhi     0.50
# Mumbai    0.35
# Chennai   0.15

#Top N values
df["City"].value_counts().head(3)

#Sort results
#Sort ascending:

df["City"].value_counts().sort_values()

#Sort by index:

df["City"].value_counts().sort_index()

#Using value_counts() on the entire DataFrame
#Counts unique values for each column:

df.apply(pd.value_counts)


#Dropping Duplicates in Pandas
#Used to remove repeated rows from a DataFrame.

#Drop all duplicate rows
df.drop_duplicates()

#Removes any row that is an exact duplicate.
#Drop duplicates based on specific column(s)
#remove duplicates based on "Name"
df.drop_duplicates(subset="Name")

#based on multiple columns
df.drop_duplicates(subset=["Name", "City"])

#Keep the first or last occurrence
#Keep the first (default):
df.drop_duplicates(keep="first")

#Keep the last:
df.drop_duplicates(keep="last")

#Remove all duplicates (drop every repeated value):
df.drop_duplicates(keep=False)

#Drop duplicates in-place
#Modify the DataFrame directly:

df.drop_duplicates(inplace=True)

#Find duplicates instead of dropping
#Before dropping, you can check duplicates:

df[df.duplicated()]

#Check duplicates based on column:
df[df.duplicated("Name")]


# What is apply()?
# apply() is used to apply a custom function to rows or columns of a DataFrame or to every element 
# of a Series.
# You use it when:
# You need a transformation more complex than built-in functions.
# You want row-wise or column-wise operations.
# You want to apply logic that depends on multiple columns.

# What is lambda?
# A lambda is an anonymous function written in a single line.

# Example:
lambda x: x * 2

#Using apply() with Series
#A Pandas Series is like a single column.

import pandas as pd

s = pd.Series([2, 3, 4, 5])

result = s.apply(lambda x: x**2)
print(result)

#Using apply() with DataFrame (column-wise)
df = pd.DataFrame({
    "name": ["shiva", "kiran", "mohan"]
})

df["name_upper"] = df["name"].apply(lambda x: x.upper())
print(df)

#Row-wise apply (axis=1)
#Use axis=1 to access multiple columns in a row.
df = pd.DataFrame({
    "first": ["Shivam", "Kiran"],
    "last": ["Kumar", "Rao"]
})

df["full_name"] = df.apply(lambda row: row["first"] + " " + row["last"], axis=1)
print(df)

#Complex function (not lambda)
#You can define a full function and pass it to apply().
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"

df["grade"] = df["score"].apply(get_grade)

#Using apply() on multiple columns with logic
# Example: Compute BMI
def bmi(row):
    return row["weight"] / (row["height"]**2)

df["bmi"] = df.apply(bmi, axis=1)

#When NOT to use apply()?
# apply() is slower than vectorized operations.
# Avoid using it when:
# You can use NumPy operations
# You can use .map(), .str, .dt
# You can use df["col"].replace()


#chunksize — Read CSV in small parts (streaming)
#chunksize lets you load 1 chunk at a time instead of the entire file into memory.

# Example: Read file in chunks of 100,000 rows
import pandas as pd

chunks = pd.read_csv("large.csv", chunksize=100000)

for chunk in chunks:
    print(chunk.shape)

# Use cases:
# Processing huge files (2GB, 5GB, 10GB)
# Computing aggregates without loading whole CSV
# Example: Sum a column over the entire file
total = 0
for chunk in pd.read_csv("large.csv", chunksize=100000):
    total += chunk["sales"].sum()

print(total)

#usecols — Read only required columns

# This reduces:
# Memory usage
# Load time
# CPU processing

#Example: Load only 3 columns from a CSV with 50 columns:
df = pd.read_csv(
    "large.csv",
    usecols=["id", "date", "price"]
)

# You can also pass column indices:
df = pd.read_csv("large.csv", usecols=[0, 3, 5])

#dtype optimization — Reduce memory drastically
#Assign smaller data types to reduce memory usage by 50–90%.

# Example: Optimize column types
dtypes = {
    "id": "int32",
    "age": "int8",
    "salary": "float32",
    "city": "category"
}

df = pd.read_csv("large.csv", dtype=dtypes)

# Best dtype choices:
# Data	Best dtype
# Small integers	int8, int16
# Medium integers	int32
# Decimal values	float32
# Repeated strings	category
# Yes/No	bool
#Example: Convert text columns to category after reading
df["state"] = df["state"].astype("category")

#Reading only required rows
#You can limit which data loads using:

#a) nrows — read first N rows
df = pd.read_csv("large.csv", nrows=50000)

#b) skiprows — skip unwanted rows
df = pd.read_csv("large.csv", skiprows=range(1, 1000000))
# This skips first 1M rows.


#c) Conditional loading (row filtering while reading)
# Best for files too large to load fully:

chunks = pd.read_csv("large.csv", chunksize=100000)

filtered = []

for chunk in chunks:
    part = chunk[chunk["status"] == "ACTIVE"]
    filtered.append(part)

df_filtered = pd.concat(filtered)

# Combining everything together
# A real-world optimized read:

chunksize = 200_000

col_types = {
    "user_id": "int32",
    "age": "int8",
    "gender": "category",
    "income": "float32"
}

use_columns = ["user_id", "age", "gender", "income"]

filtered_data = []

for chunk in pd.read_csv(
    "large.csv",
    chunksize=chunksize,
    usecols=use_columns,
    dtype=col_types
):
    chunk = chunk[chunk["age"] > 25]  # filter rows
    filtered_data.append(chunk)

df = pd.concat(filtered_data)

