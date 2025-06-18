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

low_birth_weight_california_data['County'] = low_birth_weight_california_data['County'].str.strip().str.upper()
low_birth_weight_california_data.to_csv("low_birth_weight_california_data.csv", index=False)


file_path= r"C:\Users\idhan\Downloads\pfas_health_issues\data\PFAS_CA_GW.csv"
pfas_df = pd.read_csv(file_path)
pfas_df = pfas_df[pfas_df["gm_gis_county"].notna()]

desired_columns = [
    'PFBTA', 'PFPA', 'PFHA', 'PFHPA', 'PFOA', 'PFNA', 'PFNDCA', 'PFUNDCA',
    'PFDOA', 'PFTRIDA', 'PFTEDA', 'PFHXDA', 'PFODA', '3:3FTCA', '5:3FTCA', '7:3FTCA',
    '4:2FTS', '6:2FTS', '8:2FTS', '10:2FTS', 'PFBSA', 'PFPES', 'PFHXSA', 'PFHPSA',
    'PFOS', 'PFNS', 'PFDSA', 'PFOSA', 'ETFOSE', 'ETFOSA', 'NETFOSAA', 'MEFOSE',
    'MEFOSA', 'NMEFOSAA', 'ADONA', 'HFPA-DA', '11ClPF3OUDS', '9ClPF3ONS',
    'PFAS_total', 'gm_well_id', 'gm_well_category', 'gm_gis_county', 'gm_dataset_name'
]

desired_cols = [col for col in pfas_df.columns if col in desired_columns]
filtered_pfas_df = pfas_df[desired_cols]

chemical_columns = [
    'PFBTA', 'PFPA', 'PFHA', 'PFHPA', 'PFOA', 'PFNA', 'PFNDCA', 'PFUNDCA',
    'PFDOA', 'PFTRIDA', 'PFTEDA', 'PFHXDA', 'PFODA', '3:3FTCA', '5:3FTCA', '7:3FTCA',
    '4:2FTS', '6:2FTS', '8:2FTS', '10:2FTS', 'PFBSA', 'PFPES', 'PFHXSA', 'PFHPSA',
    'PFOS', 'PFNS', 'PFDSA', 'PFOSA', 'ETFOSE', 'ETFOSA', 'NETFOSAA', 'MEFOSE',
    'MEFOSA', 'NMEFOSAA', 'ADONA', 'HFPA-DA', '11ClPF3OUDS', '9ClPF3ONS',
    'PFAS_total'
]

aggregate_pfas_df = filtered_pfas_df.groupby(['gm_gis_county','gm_well_category'])[chemical_columns].mean().reset_index()
aggregate_pfas_df.to_csv("california_aggregate_pfas_data.csv", index = False)
municipal_pfas = aggregate_pfas_df[aggregate_pfas_df["gm_well_category"]=="MUNICIPAL"]

merged_df = pd.merge(low_birth_weight_california_data, municipal_pfas, left_on="County", right_on = "gm_gis_county", how="inner")
merged_df.to_csv("merged_california_county_pfas_low_birth_weight.csv", index = False)