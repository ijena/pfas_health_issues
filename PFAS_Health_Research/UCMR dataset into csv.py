import pandas as pd

#convert UCMR-5 .txt file into a csv file
# df = pd.read_csv(r"C:\Users\idhan\Downloads\UCMR5_All.txt",encoding='ISO-8859-1', delimiter='\t',on_bad_lines='skip')

# df.to_csv(r"C:\Users\idhan\Downloads\pfas_health_issues\data\UMR-5DatasetCSV.csv", index=False)

#convert UCMR-3 .txt file into a csv file
df = pd.read_csv(r"C:\Users\idhan\Downloads\UCMR3_All.txt",encoding='ISO-8859-1', delimiter='\t',on_bad_lines='skip')

df.to_csv(r"C:\Users\idhan\Downloads\pfas_health_issues\data\UCMR-3DatasetCSV.csv", index=False)


