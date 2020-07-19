import pandas as pd
import numpy as np
import warnings as wn



def gen_var(agegroup_type_Bailey = True):
    """Function to create the relevant categorials from scratch.
    
        Args:
        -------
        
        Returns:
        -------
        A data frame containing the variables needed for the analysis.
    """
    wn.filterwarnings("ignore")
    #1. 1955 GAF
    #Read dta file 1955 GAF
    
    df_55 = pd.read_stata('data/gaf55_1.dta', convert_categoricals = False)
    
    #generate dummy: 1 if fertile and 0 if not
    df_55['_fecund'] = 0
    df_55.loc[ (df_55['fec_code'] == 4) | (df_55['fec_code'] == 5), '_fecund' ] = 1
    
    #generate dummy if ever used method of contraception
    df_55['_everuse'] = 0
    df_55.loc[ (df_55['meth_everuse'] == 1), '_everuse' ] = 1
    
    #generate dummy if ever used method of contraception or as douche
    df_55['_everuse_d'] = 0
    df_55.loc[(df_55['meth_everuse'] == 1) | (df_55['meth_everuse'] == 2), '_everuse_d'] = 1
    
    #generate dummy if ever used condom or diaphragma
    df_55['_barrier'] = 0
    df_55.loc[ (df_55['con_use'] == 1) | (df_55['dia_use'] == 1), '_barrier'] = 1
    
    #generate dummy whether either condom, diaphragma, helly, vagsupp, foamtab,
    #tampon or any other method was ever used
    df_55['_supplies'] = 0
    df_55.loc[ (df_55['con_use']==1)|(df_55['dia_use']==1)|(df_55['jelly_use']==1)|(df_55['vagsupp_use']==1) \
                    |(df_55['foamtab_use']==1)|(df_55['tampon_use']==1)|(df_55['othmeth_use']==1), '_supplies'] = 1
    
    #generate dummy, if ever used oral contraception (not possible in 1955)
    df_55['_oral'] = 0   
    
    #generate dummy wgt
    df_55['wgt'] = 1 
    
    #generate year
    df_55['year'] = 1955
    
    
    #2. 1965 NFS
        #read .dta file 1965 NFS
    df_65 = pd.read_stata('data/nfs65_1.dta', convert_categoricals = False)
    
        #generate dummy for fertility, one means fertile
    df_65['_fecund'] = 0
    df_65.loc[ (df_65['fecund'] == 8), '_fecund'] = 1
    
        #generate dummy if ever used method of contraception or as douche
    df_65['_everuse_d'] = 0
    df_65.loc[(df_65['preg1_meth1_4'] == 1) | (df_65['preg1_meth1_5'] == 1)\
                       | (df_65['preg1_meth1_6'] == 1) | (df_65['preg1_meth1_7']==1) \
                       | (df_65['preg1_meth1_8']==1)   |(df_65['preg1_meth1_12']==1) | (df_65['preg1_meth1_9']==1) \
                       | (df_65['preg1_meth1_10']==1) | (df_65['preg1_meth1_11']==1) |(df_65['preg1_meth1_13']==1) \
                       | (df_65['preg1_meth1_14']==1)|(df_65['preg1_meth1_15']==1) | (df_65['preg1_meth1_16']==1), '_everuse_d'] = 1
    
        #generate dummy whether a contraception method was used before the first pregnancy
    df_65['_everuse2_mjb'] = 0
    df_65.loc[df_65['preg1_meth1_3'] == 0, '_everuse2_mjb'] = 1 #1 if not used before first pregnancy
    df_65.loc[df_65['preg1_meth1_2'] == 1, '_everuse2_mjb'] = np.NaN # no answer to question of contraception used before first pregnancy
    
        #generate dummy if ever used method of contraception (exclusive douche)
    df_65['_everuse3_mjb'] = df_65['_everuse_d']
    df_65.loc[ (df_65['preg1_meth1_13']==1) &  (df_65['preg1_meth1_1']==0) & (df_65['preg1_meth1_2']==0) \
                           & (df_65['preg1_meth1_3']==0) & (df_65['preg1_meth1_4']==0) & (df_65['preg1_meth1_5']==0) \
                            & (df_65['preg1_meth1_6']==0) & (df_65['preg1_meth1_7']==0) & (df_65['preg1_meth1_8']==0) \
                        & (df_65['preg1_meth1_9']==0) & (df_65['preg1_meth1_10']==0) & (df_65['preg1_meth1_11']==0) \
                        & (df_65['preg1_meth1_12']==0) & (df_65['preg1_meth1_14']==0) & (df_65['preg1_meth1_15']==0) \
                           & (df_65['preg1_meth1_16'] == 0), '_everuse3_mjb' ] = 0
    
        #genrate dummy if a barrier method (condom, diaphragma) was ever used
    df_65['_barrier'] = 0
    df_65.loc[ (df_65['preg1_meth1_5'] == 1) | (df_65['preg1_meth1_7'] == 1), '_barrier' ] = 1
    
        #generate dummy if any supply methods were ever used (condoms, diaphragma, pill, jelly, foam, douche, IUD, Sponge )
    df_65['_supplies'] = 0
    df_65.loc[ (df_65['preg1_meth1_5'] == 1) | (df_65['preg1_meth1_7'] == 1)|(df_65['preg1_meth1_8'] == 1) \
                       | (df_65['preg1_meth1_9'] == 1) |  (df_65['preg1_meth1_10'] == 1) | (df_65['preg1_meth1_11']==1) \
                       | (df_65['preg1_meth1_13']==1)   |(df_65['preg1_meth1_14']==1) | (df_65['preg1_meth1_16']==1), '_supplies' ] = 1   
    
        #generate dummy if oral contraception was used (pill)
    df_65['_oral'] = 0
    df_65.loc[ df_65['preg1_meth1_8'] == 1, '_oral' ] = 1
    
    
    #repeat this for any different A-types of pregi_meth1_j
    for i in range(0,21):
        df_65.loc[ (df_65['preg{}_meth1_4'.format(i)] == 1) | (df_65['preg{}_meth1_5'.format(i)] == 1) \
                       | (df_65['preg{}_meth1_6'.format(i)] == 1) | (df_65['preg{}_meth1_7'.format(i)]==1) \
                       | (df_65['preg{}_meth1_8'.format(i)]==1)   |(df_65['preg{}_meth1_12'.format(i)]==1) | (df_65['preg{}_meth1_9'.format(i)]==1) \
                       | (df_65['preg{}_meth1_10'.format(i)]==1) | (df_65['preg{}_meth1_11'.format(i)]==1) |(df_65['preg{}_meth1_13'.format(i)]==1) \
                       | (df_65['preg{}_meth1_14'.format(i)]==1)|(df_65['preg{}_meth1_15'.format(i)]==1) | (df_65['preg{}_meth1_16'.format(i)]==1), '_everuse_d'] = 1
        
        df_65.loc[df_65['preg{}_meth1_3'.format(i)] == 0, '_everuse2_mjb'] = 1    
        
        df_65['_everuse3_mjb'] = df_65 ['_everuse_d']   
        df_65.loc[ (df_65['preg{}_meth1_13'.format(i)]==1) &  (df_65['preg{}_meth1_1'.format(i)]==0) & (df_65['preg{}_meth1_2'.format(i)]==0) \
                       & (df_65['preg{}_meth1_3'.format(i)]==0) & (df_65['preg{}_meth1_4'.format(i)]==0) & (df_65['preg{}_meth1_5'.format(i)]==0) \
                       & (df_65['preg{}_meth1_6'.format(i)]==0) & (df_65['preg{}_meth1_7'.format(i)]==0) & (df_65['preg{}_meth1_8'.format(i)]==0) \
                       & (df_65['preg{}_meth1_9'.format(i)]==0) & (df_65['preg{}_meth1_10'.format(i)]==0) & (df_65['preg{}_meth1_11'.format(i)]==0) \
                       & (df_65['preg{}_meth1_12'.format(i)]==0) & (df_65['preg{}_meth1_14'.format(i)]==0) & (df_65['preg{}_meth1_15'.format(i)]==0) \
                       & (df_65['preg{}_meth1_16'.format(i)] == 0), '_everuse3_mjb' ] = 0   
    
        df_65.loc[ (df_65['preg{}_meth1_5'.format(i)] == 1) | (df_65['preg{}_meth1_7'.format(i)] == 1), '_barrier' ] = 1
    
        df_65.loc[ (df_65['preg{}_meth1_5'.format(i)] == 1) | (df_65['preg{}_meth1_7'.format(i)] == 1)|(df_65['preg{}_meth1_8'.format(i)] == 1) \
                       | (df_65['preg{}_meth1_9'.format(i)] == 1) |  (df_65['preg{}_meth1_10'.format(i)] == 1) | (df_65['preg{}_meth1_11'.format(i)]==1) \
                       | (df_65['preg{}_meth1_13'.format(i)]==1)   |(df_65['preg{}_meth1_14'.format(i)]==1) | (df_65['preg{}_meth1_16'.format(i)]==1), '_supplies' ] = 1 
    
        df_65.loc[ df_65['preg{}_meth1_8'.format(i)] == 1, '_oral' ] = 1
        #print(i)     
    
    
    df_65 = df_65[['_barrier', '_supplies', 'preg0_coitfr', '_oral', '_fecund', '_everuse_d','_everuse2_mjb','_everuse3_mjb', \
                'H_emp_inc65', 'fam_idealch', 'att_idealch', 'res_popdens', 'res_reg', 'statefip', 'statename', 'int_num', 'per_race', \
                '_age', 'ed_higrade', 'rel_pref', 'dob', 'fec_sterilop1', 'wgt', 'ch_totlb']]
    df_65['year'] = 1965
    
    
    #3. 1970 NFS
        #read .dta file 1970 NFS
    df_70 = pd.read_stata('data/nfs70_1.dta', convert_categoricals = False)
    
        #generate dummy if ever used method of contraception or as douche
    df_70['_everuse_d'] = 0
    df_70.loc[ (df_70['preg1_meth_any'] == 1) | (df_70['dia_everuse'] == 1) | (df_70['iud_everuse'] == 1) \
                        | (df_70['_bcp_everuse'] == 1), '_everuse_d'] = 1
    
        #genrate dummy if a barrier method (condom, diaphragma) was ever used
    df_70['_barrier'] = 0
    df_70.loc[ (df_70['preg1_meth_1'] == 3) | (df_70['preg1_meth_1'] == 5) | (df_70['dia_everuse'] == 1), '_barrier'  ] = 1
    
        #generate dummy if any supply methods were ever used (condoms, diaphragma, pill, jelly, foam, douche, IUD, Sponge )
    df_70['_supplies'] = 0
    df_70.loc[ (df_70['preg1_meth_1'] == 3) | (df_70['preg1_meth_1'] == 5) | (df_70['preg1_meth_1'] == 6)   \
                       | (df_70['preg1_meth_1'] == 7) | (df_70['preg1_meth_1'] == 8) | (df_70['preg1_meth_1'] == 9) \
                       | (df_70['preg1_meth_1'] == 10) | (df_70['preg1_meth_1'] == 11) | (df_70['preg1_meth_1'] == 13) \
                       | (df_70['dia_everuse'] == 1) | (df_70['iud_everuse'] == 1) | (df_70['_bcp_everuse'] == 1), '_supplies'] = 1
    
        #generate dummy if oral contraception was used (pill)
    df_70['_oral'] = 0
    df_70.loc[ (df_70['preg1_meth_1'] == 6) | (df_70['_bcp_everuse'] == 1), '_oral' ] = 1
    
        # rename variable to make it suitable for loop
    df_70 = df_70.rename(columns={'preg0_meth': 'preg0_meth_1'})
    #df_70['preg0_meth_1'] = df_70['preg0_meth']
    
    for i in range(0,20):
        
        if i == 0 :
          j = 1
          df_70.loc[ df_70['preg0_meth1'] == 1, '_everuse_d' ] = 1  
          df_70.loc[ (df_70['preg0_meth_{}'.format(j)] == 3) | (df_70['preg0_meth_{}'.format(j)] == 5), '_barrier'] = 1
          df_70.loc[ (df_70['preg0_meth_{}'.format(j)] == 3) | (df_70['preg0_meth_{}'.format(j)] == 5) | (df_70['preg0_meth_{}'.format(j)] == 6)   \
                       | (df_70['preg0_meth_{}'.format(j)] == 7) | (df_70['preg0_meth_{}'.format(j)] == 8) | (df_70['preg0_meth_{}'.format(j)] == 9) \
                       | (df_70['preg0_meth_{}'.format(j)] == 10) | (df_70['preg0_meth_{}'.format(j)] == 11) | (df_70['preg0_meth_{}'.format(j)] == 13), '_supplies' ] = 1
          
          df_70.loc[ (df_70['preg0_meth_{}'.format(j)] == 6), '_oral' ] = 1
        else:
         df_70.loc[ (df_70['preg{}_meth_any'.format(i)] == 1), '_everuse_d' ] = 1  
        
         for j in range(1,7):
              df_70.loc[ (df_70['preg{}_meth_{}'.format(i,j)] == 3) | (df_70['preg{}_meth_{}'.format(i,j)] == 5), '_barrier'] = 1
              df_70.loc[ (df_70['preg{}_meth_{}'.format(i,j)] == 3) | (df_70['preg{}_meth_{}'.format(i,j)] == 5) | (df_70['preg{}_meth_{}'.format(i,j)] == 6)   \
                       | (df_70['preg{}_meth_{}'.format(i,j)] == 7) | (df_70['preg{}_meth_{}'.format(i,j)] == 8) | (df_70['preg{}_meth_{}'.format(i,j)] == 9) \
                       | (df_70['preg{}_meth_{}'.format(i,j)] == 10) | (df_70['preg{}_meth_{}'.format(i,j)] == 11) | (df_70['preg{}_meth_{}'.format(i,j)] == 13), '_supplies' ] = 1
              df_70.loc[df_70['preg{}_meth_{}'.format(i,j)] == 6, '_oral'] = 1
        #print(i)
         
    
    df_70 = df_70[['_barrier', '_supplies', '_oral', 'preg0_coitfr', '_everuse_d', 'H_emp_inc70', 'fam_idealch', 'att_idealch', 
                   'statefip', 'statename', 'int_LAN', 'int_LAN_size', 'int_LAN_region', 'int_num', 'per_race', 'wgt', '_age',
                   'mar_stat', 'ed_total', 'rel_pref', 'dob', 'fec_sterilop1', 'ch_totlb' ]]    
         
    df_70['year'] = 1970    
         
    
        #append data frames
    df = df_55
    df = df.append(df_65, ignore_index = True) 
    df = df.append(df_70, ignore_index = True)
    
    
    #4. Harmonize definitions of sample variables 
        #Race
    df['_White'] = 0
    df.loc[df['year'] == 1955, '_White'] = 1 
    df.loc[(df['year'] == 1965) & (df['per_race'] == 1), '_White'] = 1 
    df.loc[(df['year'] == 1970) & (df['per_race'] == 2), '_White'] = 1
    
    
        #Marital Status
    df['_Married'] = 0
    df.loc[(df['year'] == 1955) | (df['year'] == 1965), '_Married'] = 1
    df.loc[(df['year'] == 1970) & (df['mar_stat'] == 1), '_Married'] = 1
    
    
        #Education
    df['_ed_cat'] = np.NaN 
    lis = [0,9,12,13,16,18] 
    df.loc[(df['year'] == 1965) & (df['ed_higrade'] == 0), '_ed_cat'] = 0
    
    for i in range(1,len(lis)):
        #print(i)
        df.loc[ (df['year'] == 1965) & ( lis[i-1] <= df['ed_higrade'] ) & (df['ed_higrade'] < lis[i]), '_ed_cat' ] = lis[i-1]
        df.loc[ (df['ed_total'] == i), 'ed_total'] = lis[i-1]
    
    df.loc[ (df['year'] == 1970), '_ed_cat'] = df['ed_total']
    df.loc[  (df['ed'] <= 4) & (df['ed'] >= 1), 'ed'] = 0
    df.loc[  (df['ed'] == 8) | (df['ed'] == 9),'ed'] = 16
    df.loc[  (df['ed'] == 5), 'ed'] = 9
    df.loc[  (df['ed'] == 6), 'ed'] = 12
    df.loc[  (df['ed'] == 7), 'ed'] = 13
    df.loc[  (df['year'] == 1955), '_ed_cat'] = df['ed']    
    
        #Catholic
    df['_Catholic'] = 0
    df.loc[ ((df['year'] == 1955) & (df['rel_pref'] == 10)) | ((df['year'] == 1965) & (df['rel_pref'] == 21)) | \
                    ((df['year'] == 1970) & (df['rel_pref'] == 21)), '_Catholic'] = 1
        
        #Birth Cohort
    df['_yob'] = np.NaN    
    lis = range(0,870,12)
    for i in lis:
      df.loc[ ((df['year'] == 1970) | (df['year'] == 1965)) & (df['dob'] >=  i) & (df['dob'] <  i + 12), '_yob'] = i /12 + 1900
        
    df.loc[ ((df['year'] == 1970) | (df['year'] == 1965)) & (df['dob'] >  900), '_yob'] = df['dob'] + 1000   
    df.loc[ (df['year'] == 1955), '_yob' ] = df['dob_y'] + 1900     
    
    df['_yobcat'] = np.NaN  
    lis = range(1910,1960, 5)
    for i in lis:
      df.loc[  (df['_yob'] >=  i) & (df['_yob'] <  i + 5), '_yobcat'] = i  
        
        #age    
    df['_age'] = np.NaN
    df['_age'] = df['year'] - df['_yob']
    df['_agecat'] = np.NaN
    lis = range(15,60,5)    
    for i in lis:
      df.loc[  (df['_age'] >=  i) & (df['_age'] <  i + 5), '_agecat'] = i  
        
       #Surgically sterilized 
    df['_sterilop'] = 0
    df.loc[  (df['year'] == 1955) & (df['fec_ster1'] !=  0) & (df['fec_ster1'] !=  6), '_sterilop'  ] = 1 
    df.loc[  (df['year'] == 1965) & (df['fec_sterilop1'] ==  1), '_sterilop'  ] = 1  
    df.loc[ (df['year'] == 1970) & (df['fec_sterilop1'] ==  1), '_sterilop'  ] = 1  
    
        
       #ideal number of children for american family
    df['_att_idealch'] = np.NaN #create variable to standardize variables.
    df.loc[(df['att_idealch'] < 99) & (df['year'] == 1955), '_att_idealch'] = df['att_idealch']/10    
    df.loc[ (df['att_idealch'] > 90) & (df['att_idealch'] <= 130) & (df['year'] == 1965), 'att_idealch' ] = 90 #fix coding bug 
    df.loc[ ((df['att_idealch'] <= 90) & (df['year'] == 1965)) \
                       | ((df['att_idealch'] < 96) & (df['year'] == 1970)), '_att_idealch'] = df['att_idealch']/10  
    
    df['_idealcat'] = np.NaN  
    lis = [0,2,3,4,5,10,1000] #1000 can be an arbitrary high value. Just to make loop suitable
    for i in range(0, (len(lis)-1)):
        #print(i)
        df.loc[ (lis[i] <= df['_att_idealch']) & (df['_att_idealch'] < lis[i+1]), '_idealcat'  ] = lis[i]
    
        #Husbands income
    df['h_empinc65'] = np.NaN
    df.loc[ (df['year'] == 1965), 'h_empinc65' ] = df['H_emp_inc65'] 
    df.loc[ (df['h_empinc65'] != 0) & (df['h_empinc65'] < 10), 'h_empinc65' ] = df['h_empinc65']*1000+500 
    df.loc[(df['h_empinc65'] == 10), 'h_empinc65' ] = 11000
    df.loc[(df['h_empinc65'] == 20), 'h_empinc65' ] = 13500
    df.loc[ (df['h_empinc65'] == 30), 'h_empinc65' ] = 21000
    df.loc[(df['h_empinc65'] == 88) | (df['h_empinc65'] == 99), 'h_empinc65' ] = np.NaN
    
    df['h_empinc70'] = np.NaN
    df.loc[(df['year'] == 1970), 'h_empinc70' ] = df['H_emp_inc70'] 
    df.loc[ (df['h_empinc70'] != 0) & (df['h_empinc70'] < 10), 'h_empinc70' ] = df['h_empinc70']*1000+500 
    df.loc[ (df['h_empinc70'] == 10), 'h_empinc70' ] = 12000
    df.loc[ (df['h_empinc70'] == 11), 'h_empinc70' ] = 13500
    df.loc[ (df['h_empinc70'] == 12), 'h_empinc70' ] = 21000
    df.loc[ (df['h_empinc70'] == 88) | (df['h_empinc70'] == 99), 'h_empinc70' ] = np.NaN
    
    df['h_empinc55'] = np.NaN
    df.loc[ (df['year'] == 1955), 'h_empinc55' ] = df['h_emp_inc'] 
    df.loc[ (df['h_empinc55'] != 0) & (df['h_empinc55'] < 9), 'h_empinc55' ] = (df['h_empinc55']-1)*1000+500 
    df.loc[ (df['h_empinc55'] == 9), 'h_empinc55' ] = 9000
    df.loc[ (df['h_empinc55'] == 10), 'h_empinc55' ] = 14000
    df.loc[ (df['h_empinc55'] == 88) | (df['h_empinc55'] == 99), 'h_empinc55' ] = np.NaN
    
    df['_h_empinc'] = np.NaN
    df.loc[(df['year'] == 1955), '_h_empinc'] = (36.7/26.9)*df['h_empinc55'] #in 1969 US Dollar
    df.loc[(df['year'] == 1965), '_h_empinc'] = (36.7/31)*df['h_empinc65'] #in 1969 US Dollar
    df.loc[(df['year'] == 1970), '_h_empinc'] = df['h_empinc70'] #in 1969 US Dollar
    
    df['_hinccat'] = np.NaN
    df.loc[(0 <=df['_h_empinc']) & (df['_h_empinc'] <= 4500), '_hinccat'] = 0
    df.loc[(4500 < df['_h_empinc']) & (df['_h_empinc'] <= 6500), '_hinccat'] = 1
    df.loc[(6500 < df['_h_empinc']) & (df['_h_empinc'] <= 8400), '_hinccat'] = 2
    df.loc[ (8400 < df['_h_empinc']) & (df['_h_empinc'] <= 12000), '_hinccat'] = 3
    df.loc[(12000 <= df['_h_empinc']) & (df['_h_empinc'] <= 25000), '_hinccat'] = 4
    
        #Attitudes on family planning
    df['_approvefp55'] = np.NaN
    df.loc[(df['year'] == 1955), '_approvefp55'] = 0
    df.loc[(df['year'] == 1955) & (df['att_famplan'] <= 2), '_approvefp55' ] = 1
    
        #Region
    df.loc[( (df['int_LAN_region'] == 1) | (df['int_LAN_region'] == 2) ) & (df['year'] == 1970), 'res_reg' ] = 1
    df.loc[( (df['int_LAN_region'] == 3) | (df['int_LAN_region'] == 4) ) & (df['year'] == 1970), 'res_reg' ] = 2
    df.loc[( (df['int_LAN_region'] == 5) | (df['int_LAN_region'] == 6) | (df['int_LAN_region'] == 7) ) & (df['year'] == 1970), 'res_reg' ] = 3
    df.loc[( (df['int_LAN_region'] == 8) | (df['int_LAN_region'] == 9) ) & (df['year'] == 1970), 'res_reg' ] = 4
    df.loc[(df['int_LAN'] >= 54002) & (df['int_LAN'] <= 54013)  & (df['year'] == 1970), 'res_reg' ] = 1
    df.loc[ (df['statefip'] == 11) & (df['year'] == 1970), 'res_reg' ] = 3
    df.loc[ (df['year'] == 1955), 'res_reg' ] = df['_region']
    df = df.drop(columns=['_region'])
    df = df.rename(columns={'res_reg': '_region'}) #see codebokkNFS65 
    
        #Live births
    df.loc[ df['ch_totlb'] > 12, 'ch_totlb' ] = 12
    
        #coital frequency
    df['_coit_freq'] = np.NaN
    df.loc[df['preg0_coitfr'] < 98, '_coit_freq'] = df['preg0_coitfr']
    
    
    
    #5. Merge to Statenames sice some states have the name with a space ' ' in th beginning
    sn = pd.read_stata('data/temp.dta', convert_categoricals = False)
    lis = sn['statefip']
    for i in lis:
        L = len(df['statename'][df['statefip'] == i]) 
        df['statename'][ df['statefip'] == i] = np.repeat(sn['statename'][ sn['statefip'] == i], L)
        #df.loc[ df['statefip'] == i, 'statename'] = np.repeat(sn['statename'][ sn['statefip'] == i], L)
        
    #6. Merge to Griswold Laws
    gl = pd.read_stata('data/griswoldlaws5.dta', convert_categoricals = False)    
    
    df = df[df.statefip != 11] #delete columbia
    df['sales'] = np.NaN
    df['any'] = np.NaN
    df['_Phys'] = np.NaN
    df['cstck'] = np.NaN
    df['_Phy_LB'] = np.NaN
    
    lis = gl['statefip']
    indexcol = ['sales', 'any', '_Phys', 'cstck', '_Phy_LB']
    for column in indexcol:
        #print(column)
        for i in lis:
            L = len(df[column][df['statefip'] == i]) 
            df[column][df['statefip'] == i] = np.repeat(gl[column][ gl['statefip'] == i], L)
            
    df['__yobcat'] = np.NaN
    if agegroup_type_Bailey is True:
        lis = range(1910,1950,20)
    else:
        lis = range(1910,1960,20)
    
    for i in lis:
        #print(i)
        df.loc[ (df['_yobcat'] >=  i) & (df['_yobcat'] <  i + 20), '__yobcat'] = i  #maybe error in stata code (values above 1950 are set as missing)
    
    return df 

