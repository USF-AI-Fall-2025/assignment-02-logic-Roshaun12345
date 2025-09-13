import pandas as pd

#Creates the DataInvestigator object class that uses panda data fram to read from  a given data set
class DataInvestigator:
    #Checks if a panda dataframe was given to the class.
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            #is_df is used to record if the input is a data frame in the other functions 
            self.is_df = False
            self.df = None
        else:
            self.is_df = True
            self.df = df

    #Checks for and displays the most frequent value in a given column from the data set if valid
    def baseline(self, col):
        if not self.is_df:
           return None
        
        try:
          col_data = self.df.iloc[:, col]
          mode_vals = col_data.mode()
          return mode_vals.iloc[0] if not mode_vals.empty else None
        except Exception:
           return None
          
    #Checks for and displays the correlation between 2 columns in the data set if valid
    def corr(self, col1, col2):
        if not self.is_df:
            return None
        
        try:
            col_data1 = self.df.iloc[:, col1]
            col_data2 = self.df.iloc[:, col2]
            return col_data1.corr(col_data2)
        except Exception:
            return None

    #Checks for and displays the most common value in the given column
    def zeroR(self, col):
        return self.baseline(col)

