import pandas as pd 
file_path = r"C:\Users\idhan\Downloads\pfas_health_issues\data\2025 County Health Rankings Data - v3.xlsx"
excel_file = pd.ExcelFile(file_path)
df = excel_file.parse('Select Measure Data')
df.columns = df.iloc[0]
df = df[1:]
california_data = df[df['State']=='California']
cols = list(california_data.columns)
low_birth_weight = cols.index("% Low Birth Weight")
low_birth_weight_california_data = california_data.iloc[:, [
    california_data.columns.get_loc("FIPS"),
    california_data.columns.get_loc("County"),
    low_birth_weight,
    low_birth_weight +3
]]
low_birth_weight_california_data.columns = ["FIPS","County", "% Low Birth Weight", " Low Birth Weight National Z Score"]
low_birth_weight_california_data.to_csv("low_birth_weight_california_data.csv", index=False)