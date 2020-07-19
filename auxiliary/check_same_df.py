import pandas as pd
import numpy as np



#chec if same data frame
true = pd.read_stata('data/temp556570.dta', convert_categoricals = False)    

def check_same_df(df, true):
    """Function to compare whether columns with the same name in two data frames are the same.
    
        Args:
        -------
        df(DataFrame): is the data frame which should be checked
        true(DataFrame): is the true data frame
        
        Returns:
        -------
        A value if every column that has the same name, has the same entries
    """
    
    true = true.sort_values(by=['int_num', 'year'])
    check = df.sort_values(by=['int_num', 'year'])
    length = len(check['_age'])
    true['so'] = range(0,length)
    check['so']= range(0,length)
    true = true.set_index(['so']) 
    check =  check.set_index(['so'])
    
    redcheck = check[check.columns.intersection(true.columns)]
    true = true[true.columns.intersection(redcheck.columns)]
    
    count = 0
    for col in true.columns.drop(labels=['statename']):
    #for col in ['__yobcat']:    
        #print(col)
        for i in range (1, length):
            if np.logical_not( (true[col][i] == redcheck[col][i]) | (np.isnan(true[col][i]) & np.isnan(redcheck[col][i])) ):
                #print(col, i)
                count = count + 1

    if count == 0 :   
        return print("The equinamed columns of the two data frames are the same.")
    else:
        return print("The equinamed columns of the two data frames are not the same.")            
                


