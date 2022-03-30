# 
#
# A module to hold the tidy dataframe class.
# Used to help clean data and save in a tidy format.
# 
#
import pandas as pd

class Tidy_df():
    """A class for helping clean and return tidy dataframes"""
    
   
    def __init__(self):
        self.indices = None
        self.values = list()
        
    
    def set_indices(self, 
                    df: pd.DataFrame, 
                    col_locs: tuple, 
                    header_row: int) -> None:
        
        start, end = col_locs
        ind_df = df.iloc[header_row+1:,start:end+1]
        
        ind_df.columns = df.iloc[header_row,start:end+1]
        ind_df.reset_index(inplace=True, drop=True)
        self.indices = ind_df
        return None
 
    def set_values(self, df: pd.DataFrame, header_row: int, 
                   col_start: int, col_width: int, coverage_type: str) -> None:
        
        col_names = list(df.iloc[header_row+1,col_start:col_start + col_width])
        
        i = col_start
        
        
        
        while i < len(df.columns) - col_start:
            
            temp_df = df.iloc[header_row+2:, i:i+col_width]
            temp_df.columns = col_names
            
            temp_df.reset_index(inplace=True, drop=True)
            joined_df = pd.concat([self.indices, temp_df], axis=1)
            joined_df['year'] = df.iloc[header_row,i]
            joined_df['coverage_type'] = coverage_type.lower()
            
            self.values.append(joined_df)
            i += col_width
        return None

    def glue(self):
        tidier_df = pd.concat(self.values, ignore_index=True, axis=0)
        return tidier_df
