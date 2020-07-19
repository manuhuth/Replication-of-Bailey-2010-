import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import statsmodels.api as sm
import warnings as wn



def gen_descriptive_ext(df, colors):
    """Function to create the descriptive table for extension
    
        Args:
        -------
        Data frame to create the data
        
        Returns:
        -------
        One plot containing seven subplots with the results grouped by age
    """
    

    years = range(1950,1981)
    agegroup = [2,3,4,5,6,7,0]
    regions = ['Northeast', 'Midwest', 'South', 'West']
    ages = ['15-19', '20-24', '25-29', '30-34', '35-39', '40-44', 'Pooled']
    
    fig, axs = plt.subplots(2,4, figsize =(15,7.3))
    axs = axs.ravel()
    p = 0
    for a in agegroup:
        for r in range(1,len(regions)+1):
            lis_t = []
            for t in years:
                #GFR in states with sales bans in year t, region r and agegroup a
                no_sb = df['_fert'][ (df['year'] == t) & (df['_region'] == r) & (df['sales'] == 0)  & ((df['_agegroup'] == a)) ].mean()
                #GFR in states without sales bans in year t, region r and agegroup a
                sb = df['_fert'][ (df['year'] == t) & (df['_region'] == r) & (df['sales'] == 1)  & ((df['_agegroup'] == a)) ].mean()
                diff = sb - no_sb
                lis_t.append(diff)
            if p == 0:
                axs[p].plot(years, lis_t, color = colors[r-1], label = '{}'.format(regions[r-1]))
            else:
                axs[p].plot(years, lis_t, color = colors[r-1])
            axs[p].set_title(ages[p])
        p = p + 1
        
    fig.delaxes(axs[7])
    #p = 7
    #for r in range(1,len(regions)+1):
    #    lis_t = []
    #    for t in years:
    #        #GFR in states with sales bans in year t, region r and agegroup a
    #        no_sb = df['_fert'][ (df['year'] == t) & (df['_region'] == r) & (df['sales'] == 1) ].mean()
    #        #GFR in states without sales bans in year t, region r
    #        sb = df['_fert'][ (df['year'] == t) & (df['_region'] == r) & (df['sales'] == 0) ].mean()
    #        diff = sb - no_sb
    #        lis_t.append(diff)
    #    axs[p].plot(years, lis_t, color = colors[r-1])
    #    axs[p].set_title('pooled ages')
    
    fig.legend(prop={'size': 9}, loc = 'center right');
    

def ext_common_trend_1(df, quarters, col_names):
    """Function to create the descriptive table for extension
    
        Args:
        -------
        Data frame to create the data
        
        Returns:
        -------
        One plot containing seven subplots with the results grouped by age
    """
    
    df_diffs = pd.DataFrame(columns = col_names)
    
    index = 0
    len_help = int(len(col_names)/2 + 1)
    for r in range(1, len_help):
        
        lis_sales = []
        lis_no_sales = []
        for t in quarters:
            if r <= 4:
                ban = len(df['SnP'][ (df['res_reg'] == r) & (df['SnP'] == 1) & (df['_yearfuse'] <= t) ]) / len( df['SnP'][ (df['res_reg'] == r) & (df['SnP'] == 1)] )
                no_ban = len(df['SnP'][ (df['res_reg'] == r) & (df['SnP'] == 0) & (df['_yearfuse'] <= t) ]) / len( df['SnP'][ (df['res_reg'] == r) & (df['SnP'] == 0)] )
                lis_sales.append(ban)
                lis_no_sales.append(no_ban)
            else:
                ban = len(df['SnP'][  (df['SnP'] == 1) & (df['_yearfuse'] <= t) ]) / len( df['SnP'][  (df['SnP'] == 1)] )
                no_ban = len(df['SnP'][(df['SnP'] == 0) & (df['_yearfuse'] <= t) ]) / len( df['SnP'][  (df['SnP'] == 0)] )
                lis_sales.append(ban)
                lis_no_sales.append(no_ban)
        df_diffs[col_names[index]] = lis_sales
        df_diffs[col_names[index + 1]] = lis_no_sales
        index = index + 2    

    return(df_diffs)

    #fig, axs = plt.subplots(1,5, figsize =(15,7.3))
    #axs = axs.ravel()
    #titles = ['Northeast', 'Midwest', 'South', 'West', 'Pooled']
    #p = 0
    #for k in range(0,5):
    #    if p == 0:
    #        axs[k].plot(quarters, df_diffs[col_names[p]], label = 'no sales bans')
    #        axs[k].plot(quarters, df_diffs[col_names[p+1]], label = 'with sales bans')
    #    else:
    #        axs[k].plot(quarters, df_diffs[col_names[p]])
    #        axs[k].plot(quarters, df_diffs[col_names[p+1]])            
    #    axs[k].set_title(titles[k])    
    #    p = p + 2
    #fig.legend(prop={'size': 9}, loc = 'center right');


def ext_common_trend_2(df, years, colnames):
    """Function to create the descriptive table for extension
    
        Args:
        -------
        Data frame to create the data
        
        Returns:
        -------
        One plot containing seven subplots with the results grouped by age
    """
        
    
    df_diffs = pd.DataFrame(columns = colnames)
    
    p = 0
    for r in range (1,6):
        list_sales = []
        list_no_sales = []
        for t in years:       
            if r <= 4:
                ban = df['_fert'][ (df['_region'] == r) & (df['sales'] == 1) & (df['year'] == t) ].mean()
                no_ban = df['_fert'][ (df['_region'] == r) & (df['sales'] == 0) & (df['year'] == t) ].mean()
            else:
                ban = df['_fert'][  (df['sales'] == 1) & (df['year'] == t) ].mean()
                no_ban = df['_fert'][(df['sales'] == 0) & (df['year'] == t) ].mean()
            
            list_sales.append(ban)
            list_no_sales.append(no_ban)
        df_diffs[colnames[p]] = list_sales
        df_diffs[colnames[p+1]] = list_no_sales
        p = p+2
        
    return(df_diffs)
        
        #fig, axs = plt.subplots(1,5, figsize =(15,7.3))
        #axs = axs.ravel()
        #titles = ['Northeast', 'Midwest', 'South', 'West', 'Pooled']
        #p = 0
        #for k in range(0,5):
        #    if p == 0:
        #        axs[k].plot(years, df_diffs[colnames[p]], label = 'with sales bans')
        #        axs[k].plot(years, df_diffs[colnames[p+1]], label = 'no sales bans')
        #    else:
        #        axs[k].plot(years, df_diffs[colnames[p]])
        #        axs[k].plot(years, df_diffs[colnames[p+1]])            
        #    axs[k].set_title(titles[k])    
        #    p = p + 2
        #fig.legend(prop={'size': 9}, loc = 'center right');