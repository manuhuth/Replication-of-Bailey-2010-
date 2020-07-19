import pandas as pd
import numpy as np


#read split data set. original data set was to large
df_5080_1 = pd.read_stata('C:/Users/Mhuth/Documents/microeconometrics-course-project-manuhuth/data/temp5080_1.dta', convert_categoricals = False)
df_5080_2 = pd.read_stata('C:/Users/Mhuth/Documents/microeconometrics-course-project-manuhuth/data/temp5080_2.dta', convert_categoricals = False)
df_5080_3 = pd.read_stata('C:/Users/Mhuth/Documents/microeconometrics-course-project-manuhuth/data/temp5080_3.dta', convert_categoricals = False)
df_5080_4 = pd.read_stata('C:/Users/Mhuth/Documents/microeconometrics-course-project-manuhuth/data/temp5080_4.dta', convert_categoricals = False)

df_5080 = df_5080_1.append(df_5080_2, ignore_index = True)
df_5080 = df_5080.append(df_5080_3, ignore_index = True)
df_5080 = df_5080.append(df_5080_4, ignore_index = True)
df_5080 = df_5080[(df_5080['sex'] == 2) & (df_5080['age'] >= 15) &(df_5080['age'] <= 44) ]

df_5080['wgt'] = df_5080['perwt']

df_5080['_agegroup'] = np.NaN
df_5080.loc[ (df_5080['age'] >= 15) & (df_5080['age'] <= 19), '_agegroup' ] = 2
df_5080.loc[ (df_5080['age'] >= 20) & (df_5080['age'] <= 24), '_agegroup' ] = 3
df_5080.loc[ (df_5080['age'] >= 25) & (df_5080['age'] <= 29), '_agegroup' ] = 4
df_5080.loc[ (df_5080['age'] >= 30) & (df_5080['age'] <= 34), '_agegroup' ] = 5
df_5080.loc[ (df_5080['age'] >= 35) & (df_5080['age'] <= 39), '_agegroup' ] = 6
df_5080.loc[ (df_5080['age'] >= 40) & (df_5080['age'] <= 44), '_agegroup' ] = 7

df_pop1544_all = df_5080.groupby(['statefip', 'year']).sum()
df_pop1544_all.reset_index( level=['statefip', 'year'] , inplace = True)
df_pop1544_all = df_pop1544_all[['statefip', 'year', 'wgt']]
df_pop1544_all['race'] = 0
df_pop1544_all['_agegroup'] = 0

df_pop1544_all_a = df_5080.groupby(['statefip', 'year', '_agegroup']).sum()
df_pop1544_all_a.reset_index( level=['statefip', 'year', '_agegroup'] , inplace = True)
df_pop1544_all_a = df_pop1544_all_a[['statefip', 'year','_agegroup', 'wgt']]
df_pop1544_all_a['race'] = 0

df_temp = df_pop1544_all.append(df_pop1544_all_a, ignore_index = True) 
df_temp = df_temp[ (df_temp['statefip'] != 15) & (df_temp['statefip'] != 2) & (df_temp['statefip'] != 99)]

lis = []
for y in range(95,99):
    df_h = df_temp[ df_temp['year'] == y ]
    y1 = (y-90)*10
    df_h.loc[ :, 'year' ] = y*10 + 1000
    df_h = df_h.rename( columns={ 'wgt': 'pop_{}'.format(y1) } )
    lis.append(df_h)
    
df_temp1 = df_temp[ df_temp['year'] == 95 ]
df_temp1['pop_60'] = np.NaN
df_temp1['pop_70'] = np.NaN
df_temp1['pop_80'] = np.NaN

for ageg in lis[0]['_agegroup'].unique():
    for statef in lis[0]['statefip'].unique():
        h = lis[1]['pop_60'][ (lis[1]['statefip'] == statef) & (lis[1]['_agegroup'] == ageg) ]
        df_temp1.loc[ (df_temp1['statefip'] == statef) & (df_temp1['_agegroup'] == ageg), 'pop_60' ] =  h[h.index[0]]
        
        h = lis[2]['pop_70'][ (lis[2]['statefip'] == statef) & (lis[2]['_agegroup'] == ageg) ]
        df_temp1.loc[ (df_temp1['statefip'] == statef) & (df_temp1['_agegroup'] == ageg), 'pop_70' ] =  h[h.index[0]]
       
        h = lis[3]['pop_80'][ (lis[3]['statefip'] == statef) & (lis[3]['_agegroup'] == ageg) ]
        df_temp1.loc[ (df_temp1['statefip'] == statef) & (df_temp1['_agegroup'] == ageg), 'pop_80' ] =  h[h.index[0]]

df_temp1 = df_temp1.rename(columns={'wgt': 'pop_50'})
df_temp1 = df_temp1.sort_values(by=['statefip', 'race', '_agegroup'])

df_temp2 = df_temp1
for y in range(95, 98):
    min = y*10-900
    max = min + 10
    
    i = min +1 
    for k in range(i, max + 1):
        df_temp2['pop_{}_'.format(k)] = ( (df_temp1['pop_{}'.format(max)] - df_temp1['pop_{}'.format(min)])/10)*(k-min) + df_temp1['pop_{}'.format(min)]

df_temp2 = df_temp2.rename( columns={ 'pop_50' : 'pop_50_' } )

dflist = []
for y in range(50,81):
    df_help = df_temp2[['pop_{}_'.format(y), 'statefip', 'race', '_agegroup']]
    df_help = df_help.rename( columns={ 'pop_{}_'.format(y) : 'pop' } )
    df_help = df_help.dropna()
    df_help['year'] = 1900 + y
    dflist.append(df_help)
    
df_popms80 = dflist[0]
for y in range( 1, len(dflist) ):
    #print(y)
    df_popms80 = df_popms80.append(dflist[y], ignore_index = True)

df_popms80['_flag'] = np.repeat('IPUMS', len(df_popms80['pop']))
df_popms6980 = pd.read_stata('C:/Users/Mhuth/Documents/microeconometrics-course-project-manuhuth/data/popmeasures_69_80_seers.dta', convert_categoricals = False) 
df_temp = df_popms80.append(df_popms6980,  ignore_index = True)
