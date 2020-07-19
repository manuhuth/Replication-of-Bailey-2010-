import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import statsmodels.api as sm
import warnings as wn



def gen_descriptive_table(df_adj):
    """Function to create the descriptive table
    
        Args:
        -------
        Data frame to create the data
        
        Returns:
        -------
        Three data frames containing the information for Table XX.
    """
    
    
    colnames = ['', '1955', '1965', '1970']#, '  ', 'Northeast', 'Midwest', 'South', 'West']
    rownames = ['Ever used contraception', '  Any method', '  _barrier', '  Birth control pill', '  Sterilization (including husband)', \
                'Respondent characteristics', '  White', '  Currently married', '  Catholic', '  Year of birth', 'Residence in', \
                '  Northeast', '  Midwest', '  South', '  West', 'Education', '  Fewer than 9 years', '  9 to 11 years',\
                '  12 years', '  13 to 15 years', '  16 years', 'Ideal number of children', '  Fewer than two', '  Two', \
                '  Three', '  Four', '  Five or more', '  Missing', 'Husband`s income (dollars)', '  0 - 4,500', '  4,501 - 6,500', \
                '  6,501 - 7699', '  7,700 - 11,999', '  >= 12,000', '  Missing', ' ', 'Total respondents']
    df_tab = pd.DataFrame(columns = colnames)
    df_tab[''] = rownames
    
    for t in [1955, 1965, 1970]:
        vec = []
        bin_att = ['placeholder', '_everuse_d', '_barrier', '_oral', '_sterilop', 'placeholder', '_White', '_Married', '_Catholic']
        for k in bin_att:
            if k == 'placeholder':
                vec.append(' ')
            else:
                prop = round(len( df_adj[k][ (df_adj[k] == 1) & (df_adj['year'] == t) ] ) / len( df_adj[k][ (df_adj['year'] == t) ].dropna() ), 3)
                vec.append(prop)
        vec.append(t - round(df_adj['_age'][ df_adj['year'] == t ].mean(),3) ) #average year of birth
        vec.append(' ') #respondend characteristics
        for k in range(1,5):
            prop = round(len( df_adj['_region'][ (df_adj['_region'] == k) & (df_adj['year'] == t) ] ) / len( df_adj['_region'][ (df_adj['year'] == t) ].dropna() ), 3)
            vec.append(prop)
        
        vec.append(' ')
        ed_att = [9, 12, 13, 16, 30]
        lag = 0
        for k in ed_att:
            prop = round(len( df_adj['_ed_cat'][ (df_adj['_ed_cat'] >= lag) & (df_adj['_ed_cat'] < k) & (df_adj['year'] == t) ] ) / len( df_adj['_ed_cat'][ (df_adj['year'] == t) ].dropna() ), 3)
            vec.append(prop)
            lag = k 
        
        vec.append(' ')    
        
        chil_att = [2, 3, 4, 5, 30]
        lag = 0
        for k in chil_att:
            prop = round(len( df_adj['_idealcat'][ (df_adj['_idealcat'] >= lag) & (df_adj['_idealcat'] < k) & (df_adj['year'] == t) ] ) / len( df_adj['_idealcat'][ (df_adj['year'] == t) ].dropna() ), 3)
            vec.append(prop)
            lag = k
            
        vec.append( df_adj['_idealcat'][ df_adj['year'] == t ].isna().sum() )

        vec.append(' ')
        
        hinc_att = [1,2,3,4,30]
        lag = 0
        for k in hinc_att:
            prop = round(len( df_adj['_hinccat'][ (df_adj['_hinccat'] >= lag) & (df_adj['_hinccat'] < k) & (df_adj['year'] == t) ] ) / len( df_adj['_hinccat'][ (df_adj['year'] == t) ].dropna() ), 3)
            vec.append(prop)
            lag = k    
        
        vec.append( df_adj['_hinccat'][ df_adj['year'] == t ].isna().sum() )
        vec.append(' ')
        
        vec.append( len( df_adj['year'][ (df_adj['year'] == t) ] ) )
        df_tab['{}'.format(t)] = vec
      
        
    '''   
    regions = ['Northeast', 'Midwest', 'South', 'West']    
    for r in range(1,5):
        vec = []
        bin_att = ['placeholder', '_everuse_d', '_barrier', '_oral', '_sterilop', 'placeholder', '_White', '_Married', '_Catholic']
        for k in bin_att:
            if k == 'placeholder':
                vec.append(' ')
            else:
                prop = round(len( df_adj[k][ (df_adj[k] == 1) & (df_adj['_region'] == r) ] ) / len( df_adj[k][ (df_adj['_region'] == r) ].dropna() ), 3)
                vec.append(prop)
        vec.append(round((df_adj['year'][df_adj['_region'] == r] - df_adj['_age'][ df_adj['_region'] == r ]).mean(),3) ) #average year of birth
        vec.append(' ') #respondend characteristics
        for k in range(1,5):
            prop = round(len( df_adj['_region'][ (df_adj['_region'] == k) & (df_adj['_region'] == r) ] ) / len( df_adj['_region'][ (df_adj['_region'] == r) ].dropna() ), 3)
            vec.append(prop)
        
        vec.append(' ')
        ed_att = [9, 12, 13, 16, 30]
        lag = 0
        for k in ed_att:
            prop = round(len( df_adj['_ed_cat'][ (df_adj['_ed_cat'] >= lag) & (df_adj['_ed_cat'] < k) & (df_adj['_region'] == r) ] ) / len( df_adj['_ed_cat'][ (df_adj['_region'] == r) ].dropna() ), 3)
            vec.append(prop)
            lag = k 
        
        vec.append(' ')    
        
        chil_att = [2, 3, 4, 5, 30]
        lag = 0
        for k in chil_att:
            prop = round(len( df_adj['_idealcat'][ (df_adj['_idealcat'] >= lag) & (df_adj['_idealcat'] < k) & (df_adj['_region'] == r) ] ) / len( df_adj['_idealcat'][ (df_adj['_region'] == r) ].dropna() ), 3)
            vec.append(prop)
            lag = k
            
        vec.append( df_adj['_idealcat'][ df_adj['_region'] == r ].isna().sum() )

        vec.append(' ')
        
        hinc_att = [1,2,3,4,30]
        lag = 0
        for k in hinc_att:
            prop = round(len( df_adj['_hinccat'][ (df_adj['_hinccat'] >= lag) & (df_adj['_hinccat'] < k) & (df_adj['_region'] == r) ] ) / len( df_adj['_hinccat'][ (df_adj['_region'] == r) ].dropna() ), 3)
            vec.append(prop)
            lag = k    
        
        vec.append( df_adj['_hinccat'][ df_adj['_region'] == r ].isna().sum() )
        vec.append(' ')
        
        vec.append( len( df_adj['_region'][ (df_adj['_region'] == r) ] ) )
        df_tab['{}'.format(regions[r-1])] = vec    
    df_tab['  '] = np.repeat(' | ', len(rownames))
    '''
    df_tab = df_tab.set_index('')
    
    return df_tab
    

def gen_V(df_des):
    """Function to create the three panels from figure five.
    
        Args:
        -------
        Data frame to create the data
        
        Returns:
        -------
        Three data frames containing the information for plot V.
    """
    #A
    df_1965 = df_des[ df_des['year'] == 1965 ] #only use 1965 NFS
    quarters = np.arange(1960,1971, 0.25) # set up range for quarters from 1960 to 1965.25
    col_names = ['Northeast', 'Midwest','South', 'West']
    df_diffs_1965 = pd.DataFrame(columns = col_names)
    df_diffs = pd.DataFrame(columns = col_names)
    df_diffs_C = pd.DataFrame(columns = col_names)
    
    for r in range(1,5):
        lis_1965 = []
        lis = []
        lis_C = []
        for t in quarters:
            if t <= 1965.25:
                ban_1965 = len(df_1965['SnP'][ (df_1965['res_reg'] == r) & (df_1965['SnP'] == 1) & (df_1965['_yearfuse'] <= t) ]) / len( df_1965['SnP'][ (df_1965['res_reg'] == r) & (df_1965['SnP'] == 1)] )
                no_ban_1965 = len(df_1965['SnP'][ (df_1965['res_reg'] == r) & (df_1965['SnP'] == 0) & (df_1965['_yearfuse'] <= t) ]) / len( df_1965['SnP'][ (df_1965['res_reg'] == r) & (df_1965['SnP'] == 0)] )
                diff_1965 = ban_1965 - no_ban_1965 
            else: 
                diff_1965 = np.NaN
            lis_1965.append(diff_1965)
            
            ban = len(df_des['SnP'][ (df_des['res_reg'] == r) & (df_des['SnP'] == 1) & (df_des['_yearfuse'] <= t) ]) / len( df_des['SnP'][ (df_des['res_reg'] == r) & (df_des['SnP'] == 1)] )
            no_ban = len(df_des['SnP'][ (df_des['res_reg'] == r) & (df_des['SnP'] == 0) & (df_des['_yearfuse'] <= t) ]) / len( df_des['SnP'][ (df_des['res_reg'] == r) & (df_des['SnP'] == 0) ] )
            diff = ban - no_ban
            lis.append(diff)
            
            ban_C = len(df_des['SnP'][ (df_des['res_reg'] == r) & (df_des['SnP'] == 1) & (df_des['_yearfuse'] <= t) ]) / len( df_des['SnP'][ (df_des['res_reg'] == r) & (df_des['SnP'] == 1)  & (df_des['_yearfuse'] < 1971)] )
            no_ban_C = len(df_des['SnP'][ (df_des['res_reg'] == r) & (df_des['SnP'] == 0) & (df_des['_yearfuse'] <= t) ]) / len( df_des['SnP'][ (df_des['res_reg'] == r) & (df_des['SnP'] == 0) & (df_des['_yearfuse'] < 1971)] )
            diff_C = ban_C - no_ban_C
            lis_C.append(diff_C)   
            
        df_diffs_1965.loc[: , col_names[r-1] ] = lis_1965
        df_diffs.loc[: , col_names[r-1] ] = lis
        df_diffs_C.loc[: , col_names[r-1] ] = lis_C
 
    return df_diffs_1965, df_diffs, df_diffs_C
