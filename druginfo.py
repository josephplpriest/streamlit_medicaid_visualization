# 
# 
# 
# 
# 
# 
import pandas as pd
filename1 = "data/DSD_PTD_R21_DYT20_Web.xlsx"
filename2 = "data/DSD_MCD_R21_DYT20_Web.xlsx"


drug_info_mcr = pd.read_excel(filename1, sheet_name=3, skiprows=4, header=0)

drug_info_mcd = pd.read_excel(filename2, sheet_name=3, skiprows=4, header=0)

drug_info_mcr.columns = ['Brand', 'Generic', 'Uses']
drug_info_mcd.columns = ['Brand', 'Generic', 'Uses']

combined_info = pd.concat([drug_info_mcd, drug_info_mcr])

combined_info['Brand'] = combined_info['Brand'].str.lower().apply(lambda x: x.replace('and', '&'))

cleaner = combined_info.drop_duplicates('Brand').reset_index(drop=True)

cleaner.to_csv("data/drug_info.csv")

