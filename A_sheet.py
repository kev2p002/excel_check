import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'example.xlsx'

# Load the Excel file
excel_data = pd.ExcelFile(excel_file_path)

# List all sheet names to verify their order
sheet_names = excel_data.sheet_names
print("Sheet names:", sheet_names)

# Load data from each sheet into separate DataFrames by index
df_sheet1 = pd.read_excel(excel_file_path, sheet_name=0)
df_sheet2 = pd.read_excel(excel_file_path, sheet_name=1)

# Print the DataFrames to verify
print("DataFrame from first sheet:")
print(df_sheet1)

print("\nDataFrame from second sheet:")
print(df_sheet2)
