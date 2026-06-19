import pandas as pd

# Load Excel file
df = pd.read_excel("Dataset for Data Analytics (1).xlsx")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text columns
for col in df.select_dtypes(include='object'):
    df[col] = df[col].str.strip()

# Fill missing values
for col in df.select_dtypes(include='object'):
    df[col] = df[col].fillna("Unknown")

for col in df.select_dtypes(include=['int64', 'float64']):
    df[col] = df[col].fillna(df[col].mean())

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# Convert Date column to proper date format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Month"] = df["Date"].dt.month_name()

cols = df.columns.tolist()
cols.insert(cols.index("Date") + 1, cols.pop(cols.index("Month")))
df = df[cols]

df["Date"] = df["Date"].dt.strftime("%d-%m-%Y")

print(df.columns)

df.to_excel("Cleaned_Dataset_New.xlsx", index=False)


# Save cleaned dataset
df.to_excel("Cleaned_Dataset_New.xlsx", index=False)

print("\nDataset cleaned successfully!")
print("Saved as: Cleaned_Dataset_New.xlsx")