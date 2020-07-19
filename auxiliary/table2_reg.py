import pandas as pd
import numpy as np
from statsmodels.discrete.discrete_model import Probit


#First regression table
def table2_reg(df_reg, disp_it):
    """Function to create the tables for the first probit models.
    
        Args:
        dataFrame containing the categorial variables as dummies and the interaction terms
        disp_it boolean value indicating whether information about iterations should be displayed
        
        Returns:
        -------
        A table containing the regression output of the first 4 model specifications.
    """
    #first model
    Y = df_reg['_oral']
    X = df_reg[['sales', 'd1970', 'dsalesX1970', '_Phys', 'd_PhysX1970', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970']] 
    X['int'] = np.repeat(1, len(Y))
    model1 = Probit(Y,X)
    probit_model1 = model1.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model1.summary()) #got same results as paper
     
        #compute margins (get_margeff)
    probit_margeff1 = probit_model1.get_margeff()
    #probit_margeff1.summary()
     

    #second model
    Y = df_reg['_oral']
    X = df_reg[['sales', 'd1970', 'dsalesX1970', '_Phys', 'd_PhysX1970', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970', 'any', 'anyX1970']]
    X['int'] = np.repeat(1, len(Y))
    model2 = Probit(Y,X)
    probit_model2 = model2.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model2.summary()) #got same results as paper
     
        #compute margins (get_margeff)
    probit_margeff2 = probit_model2.get_margeff()
    probit_margeff2.summary()
    
    #third model
    Y = df_reg['_oral']
    X = df_reg[['sales', 'd1970', 'dsalesX1970', '_Phys', 'd_PhysX1970', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970', 'any', 'anyX1970','d_agecat20', 'd_agecat25', 'd_agecat30', 'd_agecat35',\
                'd_agecat20X1970', 'd_agecat25X1970', 'd_agecat30X1970', 'd_agecat35X1970','_Catholic' ,'_CatholicX1970',\
                'd_ed_cat9', 'd_ed_cat12', 'd_ed_cat13', 'd_ed_cat16', 'd_ed_cat9X1970', 'd_ed_cat12X1970', 'd_ed_cat13X1970', \
                'd_ed_cat16X1970', 'd_hinccat1', 'd_hinccat2', 'd_hinccat3', 'd_hinccat4', 'd_hinccat1X1970', 'd_hinccat2X1970',
                'd_hinccat3X1970', 'd_hinccat4X1970']]
    X['int'] = np.repeat(1, len(Y))
    model3 = Probit(Y,X)
    probit_model3 = model3.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model3.summary()) 
     
        #compute margins (get_margeff)
    probit_margeff3 = probit_model3.get_margeff()
    #probit_margeff3.summary()
    
    #fourth model
    Y = df_reg['_oral']
    X = df_reg[['sales', 'd1970', 'dsalesX1970', '_Phys', 'd_PhysX1970', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970', 'any', 'anyX1970','d_agecat20', 'd_agecat25', 'd_agecat30', 'd_agecat35',\
                'd_agecat20X1970', 'd_agecat25X1970', 'd_agecat30X1970', 'd_agecat35X1970','_Catholic' ,'_CatholicX1970',\
                'd_ed_cat9', 'd_ed_cat12', 'd_ed_cat13', 'd_ed_cat16', 'd_ed_cat9X1970', 'd_ed_cat12X1970', 'd_ed_cat13X1970', \
                'd_ed_cat16X1970', 'd_hinccat1', 'd_hinccat2', 'd_hinccat3', 'd_hinccat4', 'd_hinccat1X1970', 'd_hinccat2X1970',
                'd_hinccat3X1970', 'd_hinccat4X1970', 'd_idealcat2', 'd_idealcat3', 'd_idealcat4', 'd_idealcat5', 'd_idealcat2X1970', \
                'd_idealcat3X1970', 'd_idealcat4X1970', 'd_idealcat5X1970']]
    X['int'] = np.repeat(1, len(Y))
    model4 = Probit(Y,X)
    probit_model4 = model4.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model4.summary()) 
     
        #compute margins (get_margeff)
    probit_margeff4 = probit_model4.get_margeff()
    #print(probit_margeff4.summary())

    table = pd.DataFrame({'(1)': [], '(2)': [], '(3)': [], '(4)': []})
    table[' '] = ['Sales ban', '','p-value', 'Sales ban x 1(1970)', ' ','p-value', 'Observations', 'Log Likelihood', \
                         'Additional Covariates', 'Legal Variables']    
    table = table.set_index(' ')
    table['(1)'] = [round(probit_margeff1.margeff[0],3), '({})'.format(round(probit_margeff1.margeff_se[0],3)), round(probit_margeff1.pvalues[0],3), round(probit_margeff1.margeff[2],3), \
                    '({})'.format(round(probit_margeff1.margeff_se[2],3)), round(probit_margeff1.pvalues[2],3), round(probit_margeff1.results.nobs,3), round(probit_margeff1.results.llf,3),\
                        'R','PX' ]
    table['(2)'] = [round(probit_margeff2.margeff[0],3), '({})'.format(round(probit_margeff2.margeff_se[0],3)), round(probit_margeff2.pvalues[0],3), round(probit_margeff2.margeff[2],3), \
                    '({})'.format(round(probit_margeff2.margeff_se[2],3)), round(probit_margeff2.pvalues[2],3), round(probit_margeff2.results.nobs,3), round(probit_margeff2.results.llf,3),\
                        'R','PX, AD' ]
    table['(3)'] = [round(probit_margeff3.margeff[0],3), '({})'.format(round(probit_margeff3.margeff_se[0],3)), round(probit_margeff3.pvalues[0],3), round(probit_margeff3.margeff[2],3), \
                    '({})'.format(round(probit_margeff3.margeff_se[2],3)), round(probit_margeff3.pvalues[2],3), round(probit_margeff3.results.nobs,3), round(probit_margeff3.results.llf,3),\
                        'R,A,C,E,I','PX, AD' ]
    table['(4)'] = [round(probit_margeff4.margeff[0],3), '({})'.format(round(probit_margeff4.margeff_se[0],3)), round(probit_margeff4.pvalues[0],3), round(probit_margeff4.margeff[2],3), \
                    '({})'.format(round(probit_margeff4.margeff_se[2],3)), round(probit_margeff4.pvalues[2],3), round(probit_margeff4.results.nobs,3), round(probit_margeff4.results.llf,3),\
                        'R,A,C,E,I','PX, AD, K' ]
    
    return table, model1, model2, model3, model4




#Second regression table
    
def table3_reg(df_reg, disp_it):
    """Function to create the tables for the second probit models.
    
        Args:
        dataFrame containing the categorial variables as dummies and the interaction terms
        
        Returns:
        -------
        A table containing the regression output of the 8 model specifications for the second table.
    """
    #1. _everuse_d as dependent variable 
    #first model
    Y = df_reg['_everuse_d']
    X = df_reg[['sales', 'd1970','d1965', 'dsalesX1970','dsalesX1965', '_Phys', 'd_PhysX1970', 'd_PhysX1965', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970', 'dreg2X1965', 'dreg3X1965', 'dreg4X1965']] 
    X['int'] = np.repeat(1, len(Y))
    model1 = Probit(Y,X)
    probit_model1 = model1.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model1.summary()) #got same results as paper
     
        #compute margins (get_margeff)
    probit_margeff1 = probit_model1.get_margeff()
    #probit_margeff1.summary()
     

    #second model
    Y = df_reg['_everuse_d']
    X = df_reg[['sales', 'd1970','d1965', 'dsalesX1970','dsalesX1965', '_Phys', 'd_PhysX1970', 'd_PhysX1965', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970', 'dreg2X1965', 'dreg3X1965', 'dreg4X1965', 'any', 'anyX1970', 'anyX1965']]
    X['int'] = np.repeat(1, len(Y))
    model2 = Probit(Y,X)
    probit_model2 = model2.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model2.summary()) #got same results as paper
     
        #compute margins (get_margeff)
    probit_margeff2 = probit_model2.get_margeff()
    probit_margeff2.summary()
    
    #third model
    Y = df_reg['_everuse_d']
    X = df_reg[['sales', 'd1970','d1965', 'dsalesX1970','dsalesX1965', '_Phys', 'd_PhysX1970', 'd_PhysX1965', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970','dreg2X1965', 'dreg3X1965', 'dreg4X1965', 'any', 'anyX1970',
                'anyX1965','d_agecat20', 'd_agecat25', 'd_agecat30', 'd_agecat35', 'd_agecat20X1970', \
                'd_agecat25X1970', 'd_agecat30X1970', 'd_agecat35X1970','d_agecat20X1965', 'd_agecat25X1965', \
                'd_agecat30X1965', 'd_agecat35X1965','_Catholic' ,'_CatholicX1970', '_CatholicX1965',\
                'd_ed_cat9', 'd_ed_cat12', 'd_ed_cat13', 'd_ed_cat16', 'd_ed_cat9X1970', 'd_ed_cat12X1970', \
                'd_ed_cat13X1970',  'd_ed_cat9X1965', 'd_ed_cat12X1965', 'd_ed_cat13X1965', \
                'd_ed_cat16X1970','d_ed_cat16X1965', 'd_hinccat1', 'd_hinccat2', 'd_hinccat3', 'd_hinccat4', \
                'd_hinccat1X1970', 'd_hinccat2X1970', \
                'd_hinccat3X1970', 'd_hinccat4X1970',  'd_hinccat1X1965', 'd_hinccat2X1965', 'd_hinccat3X1965', \
                'd_hinccat4X1965']]
    X['int'] = np.repeat(1, len(Y))
    model3 = Probit(Y,X)
    probit_model3 = model3.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model3.summary()) 
     
        #compute margins (get_margeff)
    probit_margeff3 = probit_model3.get_margeff()
    probit_margeff3.summary()
    
    #fourth model
    Y = df_reg['_everuse_d']
    X = df_reg[['sales', 'd1970','d1965', 'dsalesX1970','dsalesX1965', '_Phys', 'd_PhysX1970', 'd_PhysX1965', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970','dreg2X1965', 'dreg3X1965', 'dreg4X1965', 'any', 'anyX1970',
                'anyX1965','d_agecat20', 'd_agecat25', 'd_agecat30', 'd_agecat35', 'd_agecat20X1970', \
                'd_agecat25X1970', 'd_agecat30X1970', 'd_agecat35X1970','d_agecat20X1965', 'd_agecat25X1965', \
                'd_agecat30X1965', 'd_agecat35X1965','_Catholic' ,'_CatholicX1970', '_CatholicX1965',\
                'd_ed_cat9', 'd_ed_cat12', 'd_ed_cat13', 'd_ed_cat16', 'd_ed_cat9X1970', 'd_ed_cat12X1970', \
                'd_ed_cat13X1970',  'd_ed_cat9X1965', 'd_ed_cat12X1965', 'd_ed_cat13X1965', \
                'd_ed_cat16X1970','d_ed_cat16X1965', 'd_hinccat1', 'd_hinccat2', 'd_hinccat3', 'd_hinccat4', \
                'd_hinccat1X1970', 'd_hinccat2X1970', \
                'd_hinccat3X1970', 'd_hinccat4X1970',  'd_hinccat1X1965', 'd_hinccat2X1965', 'd_hinccat3X1965', \
                'd_hinccat4X1965', 'd_idealcat2', 'd_idealcat3', 'd_idealcat4', 'd_idealcat5', 'd_idealcat2X1970', \
                'd_idealcat3X1970', 'd_idealcat4X1970', 'd_idealcat5X1970', 'd_idealcat2X1965', \
                'd_idealcat3X1965', 'd_idealcat4X1965', 'd_idealcat5X1965']]
                
    X['int'] = np.repeat(1, len(Y))
    model4 = Probit(Y,X)
    probit_model4 = model4.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model4.summary()) 
     
        #compute margins (get_margeff)
    probit_margeff4 = probit_model4.get_margeff()
    probit_margeff4.summary()
    
    #store results
    model1_help = model1
    model2_help = model2
    model3_help = model3
    model4_help = model3
    
    
    #2. _barrier as dependent variable
    #first model
    Y = df_reg['_barrier']
    X = df_reg[['sales', 'd1970','d1965', 'dsalesX1970','dsalesX1965', '_Phys', 'd_PhysX1970', 'd_PhysX1965', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970', 'dreg2X1965', 'dreg3X1965', 'dreg4X1965']] 
    X['int'] = np.repeat(1, len(Y))
    model1 = Probit(Y,X)
    probit_model1 = model1.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model1.summary()) #got same results as paper
     
        #compute margins (get_margeff)
    probit_margeffb1 = probit_model1.get_margeff()
    probit_margeffb1.summary()
     

    #second model
    Y = df_reg['_barrier']
    X = df_reg[['sales', 'd1970','d1965', 'dsalesX1970','dsalesX1965', '_Phys', 'd_PhysX1970', 'd_PhysX1965', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970', 'dreg2X1965', 'dreg3X1965', 'dreg4X1965', 'any', 'anyX1970', 'anyX1965']]
    X['int'] = np.repeat(1, len(Y))
    model2 = Probit(Y,X)
    probit_model2 = model2.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model2.summary()) #got same results as paper
     
        #compute margins (get_margeff)
    probit_margeffb2 = probit_model2.get_margeff()
    probit_margeffb2.summary()
    
    #third model
    Y = df_reg['_barrier']
    X = df_reg[['sales', 'd1970','d1965', 'dsalesX1970','dsalesX1965', '_Phys', 'd_PhysX1970', 'd_PhysX1965', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970','dreg2X1965', 'dreg3X1965', 'dreg4X1965', 'any', 'anyX1970',
                'anyX1965','d_agecat20', 'd_agecat25', 'd_agecat30', 'd_agecat35', 'd_agecat20X1970', \
                'd_agecat25X1970', 'd_agecat30X1970', 'd_agecat35X1970','d_agecat20X1965', 'd_agecat25X1965', \
                'd_agecat30X1965', 'd_agecat35X1965','_Catholic' ,'_CatholicX1970', '_CatholicX1965',\
                'd_ed_cat9', 'd_ed_cat12', 'd_ed_cat13', 'd_ed_cat16', 'd_ed_cat9X1970', 'd_ed_cat12X1970', \
                'd_ed_cat13X1970',  'd_ed_cat9X1965', 'd_ed_cat12X1965', 'd_ed_cat13X1965', \
                'd_ed_cat16X1970','d_ed_cat16X1965', 'd_hinccat1', 'd_hinccat2', 'd_hinccat3', 'd_hinccat4', \
                'd_hinccat1X1970', 'd_hinccat2X1970', \
                'd_hinccat3X1970', 'd_hinccat4X1970',  'd_hinccat1X1965', 'd_hinccat2X1965', 'd_hinccat3X1965', \
                'd_hinccat4X1965']]
    X['int'] = np.repeat(1, len(Y))
    model3 = Probit(Y,X)
    probit_model3 = model3.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model3.summary()) 
     
        #compute margins (get_margeff)
    probit_margeffb3 = probit_model3.get_margeff()
    probit_margeffb3.summary()
    
    #fourth model
    Y = df_reg['_barrier']
    X = df_reg[['sales', 'd1970','d1965', 'dsalesX1970','dsalesX1965', '_Phys', 'd_PhysX1970', 'd_PhysX1965', 'dreg2', 'dreg3', 'dreg4', \
                'dreg2X1970', 'dreg3X1970', 'dreg4X1970','dreg2X1965', 'dreg3X1965', 'dreg4X1965', 'any', 'anyX1970',
                'anyX1965','d_agecat20', 'd_agecat25', 'd_agecat30', 'd_agecat35', 'd_agecat20X1970', \
                'd_agecat25X1970', 'd_agecat30X1970', 'd_agecat35X1970','d_agecat20X1965', 'd_agecat25X1965', \
                'd_agecat30X1965', 'd_agecat35X1965','_Catholic' ,'_CatholicX1970', '_CatholicX1965',\
                'd_ed_cat9', 'd_ed_cat12', 'd_ed_cat13', 'd_ed_cat16', 'd_ed_cat9X1970', 'd_ed_cat12X1970', \
                'd_ed_cat13X1970',  'd_ed_cat9X1965', 'd_ed_cat12X1965', 'd_ed_cat13X1965', \
                'd_ed_cat16X1970','d_ed_cat16X1965', 'd_hinccat1', 'd_hinccat2', 'd_hinccat3', 'd_hinccat4', \
                'd_hinccat1X1970', 'd_hinccat2X1970', \
                'd_hinccat3X1970', 'd_hinccat4X1970',  'd_hinccat1X1965', 'd_hinccat2X1965', 'd_hinccat3X1965', \
                'd_hinccat4X1965', 'd_idealcat2', 'd_idealcat3', 'd_idealcat4', 'd_idealcat5', 'd_idealcat2X1970', \
                'd_idealcat3X1970', 'd_idealcat4X1970', 'd_idealcat5X1970', 'd_idealcat2X1965', \
                'd_idealcat3X1965', 'd_idealcat4X1965', 'd_idealcat5X1965']]
                
    X['int'] = np.repeat(1, len(Y))
    model4 = Probit(Y,X)
    probit_model4 = model4.fit(cov_type='cluster', cov_kwds={'groups': df_reg['_region']}, disp = disp_it)
    #print(probit_model4.summary()) 
     
        #compute margins (get_margeff)
    probit_margeffb4 = probit_model4.get_margeff()
    probit_margeffb4.summary()


    #3. create table for output
    
    table = pd.DataFrame({'(1)': [], '(2)': [], '(3)': [], '(4)': []})
    table[' '] = ['Ever used Pill','Sales ban', '','p-value', 'Sales ban x 1(1965)', ' ','p-value', 'Sales ban x 1(1970)', ' ','p-value',\
                  'Obersvations', 'Log Likelihood', ' ', 'Ever used barrier', 'Sales ban', '','p-value', 'Sales ban x 1(1965)', ' ',\
                  'p-value', 'Sales ban x 1(1970)', ' ','p-value',\
                  'Obersvations', 'Log Likelihood', \
                  'Additional Covariates', 'Legal Variables']    
    table = table.set_index(' ')
    table['(1)'] = [' ', round(probit_margeff1.margeff[0],3), '({})'.format(round(probit_margeff1.margeff_se[0],3)),\
                    round(probit_margeff1.pvalues[0],3), round(probit_margeff1.margeff[4],3), \
                    '({})'.format(round(probit_margeff1.margeff_se[4],3)), round(probit_margeff1.pvalues[4],3),\
                    round(probit_margeff1.margeff[3],3), \
                    '({})'.format(round(probit_margeff1.margeff_se[3],3)), round(probit_margeff1.pvalues[3],3),\
                    round(probit_margeff1.results.nobs,3), round(probit_margeff1.results.llf,3),\
                    ' ', ' ', round(probit_margeffb1.margeff[0],3), '({})'.format(round(probit_margeffb1.margeff_se[0],3)),\
                    round(probit_margeffb1.pvalues[0],3), round(probit_margeffb1.margeff[4],3), \
                    '({})'.format(round(probit_margeffb1.margeff_se[4],3)), round(probit_margeffb1.pvalues[4],3),\
                    round(probit_margeffb1.margeff[3],3), '({})'.format(round(probit_margeffb1.margeff_se[3],3)),\
                    round(probit_margeffb1.pvalues[3],3), round(probit_margeffb1.results.nobs,3),\
                    round(probit_margeffb1.results.llf,3), 'R','PX']
        
    table['(2)'] = [' ', round(probit_margeff2.margeff[0],3), '({})'.format(round(probit_margeff2.margeff_se[0],3)),\
                    round(probit_margeff2.pvalues[0],3), round(probit_margeff2.margeff[4],3), \
                    '({})'.format(round(probit_margeff2.margeff_se[4],3)), round(probit_margeff2.pvalues[4],3),\
                    round(probit_margeff2.margeff[3],3), \
                    '({})'.format(round(probit_margeff2.margeff_se[3],3)), round(probit_margeff2.pvalues[3],3),\
                    round(probit_margeff2.results.nobs,3), round(probit_margeff2.results.llf,3),\
                    ' ', ' ', round(probit_margeffb2.margeff[0],3), '({})'.format(round(probit_margeffb2.margeff_se[0],3)),\
                    round(probit_margeffb2.pvalues[0],3), round(probit_margeffb2.margeff[4],3), \
                    '({})'.format(round(probit_margeffb2.margeff_se[4],3)), round(probit_margeffb2.pvalues[4],3),\
                    round(probit_margeffb2.margeff[3],3), '({})'.format(round(probit_margeffb2.margeff_se[3],3)),\
                    round(probit_margeffb2.pvalues[3],3), round(probit_margeffb2.results.nobs,3),\
                    round(probit_margeffb2.results.llf,3), \
                    'R','PX, AD' ]
        
    table['(3)'] = [' ', round(probit_margeff3.margeff[0],3), '({})'.format(round(probit_margeff3.margeff_se[0],3)),\
                    round(probit_margeff3.pvalues[0],3), round(probit_margeff3.margeff[4],3), \
                    '({})'.format(round(probit_margeff3.margeff_se[4],3)), round(probit_margeff3.pvalues[4],3),\
                    round(probit_margeff3.margeff[3],3), \
                    '({})'.format(round(probit_margeff3.margeff_se[3],3)), round(probit_margeff3.pvalues[3],3),\
                    round(probit_margeff3.results.nobs,3), round(probit_margeff3.results.llf,3),\
                    ' ', ' ', round(probit_margeffb3.margeff[0],3), '({})'.format(round(probit_margeffb3.margeff_se[0],3)),\
                    round(probit_margeffb3.pvalues[0],3), round(probit_margeffb3.margeff[4],3), \
                    '({})'.format(round(probit_margeffb3.margeff_se[4],3)), round(probit_margeffb3.pvalues[4],3),\
                    round(probit_margeffb3.margeff[3],3), '({})'.format(round(probit_margeffb3.margeff_se[3],3)),\
                    round(probit_margeffb3.pvalues[3],3), round(probit_margeffb3.results.nobs,3),\
                    round(probit_margeffb3.results.llf,3),
                    'R,A,C,E,I','PX, AD' ]
        
    table['(4)'] = [' ', round(probit_margeff4.margeff[0],3), '({})'.format(round(probit_margeff4.margeff_se[0],3)),\
                    round(probit_margeff4.pvalues[0],3), round(probit_margeff4.margeff[4],3), \
                    '({})'.format(round(probit_margeff4.margeff_se[4],3)), round(probit_margeff4.pvalues[4],3),\
                    round(probit_margeff4.margeff[3],3), \
                    '({})'.format(round(probit_margeff4.margeff_se[3],3)), round(probit_margeff4.pvalues[3],3),\
                    round(probit_margeff4.results.nobs,3), round(probit_margeff4.results.llf,3),\
                    ' ', ' ', round(probit_margeffb4.margeff[0],3), '({})'.format(round(probit_margeffb4.margeff_se[0],3)),\
                    round(probit_margeffb4.pvalues[0],3), round(probit_margeffb4.margeff[4],3), \
                    '({})'.format(round(probit_margeffb4.margeff_se[4],3)), round(probit_margeffb4.pvalues[4],3),\
                    round(probit_margeffb4.margeff[3],3), '({})'.format(round(probit_margeffb4.margeff_se[3],3)),\
                    round(probit_margeffb4.pvalues[3],3), round(probit_margeffb4.results.nobs,3),\
                    round(probit_margeffb4.results.llf,3),
                    'R,A,C,E,I','PX, AD, K' ]

    
    return table, model1, model2, model3, model4, model1_help, model2_help, model3_help, model4_help
        
    
    
    
    
    
    