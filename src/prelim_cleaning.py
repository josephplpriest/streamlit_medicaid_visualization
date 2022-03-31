import pandas as pd
import numpy as np
from tidy import Tidy_df

def main():
    filename1 = "./data/raw/DSD_MCD_R21_DYT20_Web.xlsx"
    filename2 = "./data/raw/DSD_MCD_R17_DYT16_Web.xlsx"
    filename3 = "./data/raw/DSD_PTD_R21_DYT20_Web.xlsx"
    filename4 = "./data/raw/DSD_PTD_R17_DYT16_Web.xlsx"

    mcd_costs_20 = pd.read_excel(filename1, sheet_name=1, skiprows=1).iloc[:,:-2]
    mcd_costs_16 = pd.read_excel(filename2, sheet_name=1, skiprows=1).iloc[:,:-2]
    mcr_costs_20 = pd.read_excel(filename3, sheet_name=1, skiprows=1).iloc[:,:-2]
    mcr_costs_16 = pd.read_excel(filename4, sheet_name=1, skiprows=1).iloc[:,:-2]
        
    dataframe_dict = {"medicaid": [mcd_costs_16, mcd_costs_20], "medicare": [mcr_costs_16, mcr_costs_20]}

    tidy = Tidy_df()

    tidy.set_indices(mcd_costs_20, (0,2), 1)
    tidy.set_values(mcd_costs_20, 0, 3, 6, 'medicaid')
        
    tidy.set_indices(mcd_costs_16, (0,2), 1)
    tidy.set_values(mcd_costs_16, 0, 3, 5, 'medicaid')

    tidy.set_indices(mcr_costs_20, (0,2), 1)
    tidy.set_values(mcr_costs_20, 0, 3, 8, 'medicare')

    tidy.set_indices(mcr_costs_16, (0,2), 1)
    tidy.set_values(mcr_costs_16, 0, 3, 7, 'medicare')


    new_list = []
    cols_to_keep = ['Brand Name', 
                'Generic Name', 
                'Number of Manufacturers',
                'Total Spending', 
                'Total Dosage Units', 
                'Total Claims',
                'Average Spending Per Dosage Unit (Weighted)',
                'Average Spending Per Claim',
                'year', 
                'coverage_type']
    for df in tidy.values:
        if 'Average \nSpending Per Claim' in df.columns:
            df['Average Spending Per Claim'] = df['Average \nSpending Per Claim']
        
        new_list.append(df[cols_to_keep])
    
    tidy.values = new_list

    cleaned_df = tidy.glue()
    cleaned_df['year'] = cleaned_df['year'].apply(lambda x: int(x[-4:]))

    cleaned_df.replace('  ', np.nan, inplace=True)
    cleaned_df.replace(' ', np.nan, inplace=True)
    cleaned_df.replace('', np.nan, inplace=True)
    
    cleaned_df.to_csv("./data/clean/combined.csv", float_format='%.2f', na_rep='NULL')

    print("Data Cleaning Finished: Two files saved in data folder.")
    
    import druginfo  # save drug info to another CSV

if __name__ == "__main__":
    main()
