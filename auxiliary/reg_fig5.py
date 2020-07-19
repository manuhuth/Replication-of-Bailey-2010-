import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import statsmodels.api as sm
import warnings as wn



def gen_Fig4_A(df):
    """Function to create the plot from Figure 6 in Bailey (2010)
    
        Args:
        -------
        takes a data frame for which the results should be computed
        
        Returns:
        -------
        A figure containing the plot from Figure 6 in Bailey (2010)
    """
    wn.filterwarnings("ignore")

    #1. first regression
    #generate region dummy
    df_reg = df
    df_reg['dreg2'] = 0
    df_reg.loc[df_reg['_region'] == 2, 'dreg2'] = 1 
    df_reg['dreg3'] = 0
    df_reg.loc[df_reg['_region'] == 3, 'dreg3'] = 1
    df_reg['dreg4'] = 0
    df_reg.loc[df_reg['_region'] == 4, 'dreg4'] = 1 
    
    #generate year dummies, leave out 1950
    dyears = [] #initialize list for year dummies
    for i in range(1951, 1981):
        df_reg['d{}'.format(i)] = 0
        df_reg.loc[df_reg['year'] == i, 'd{}'.format(i)] = 1 
        dyears.append('d{}'.format(i))
    
    
    # dummies to create interaction terms with
    dummies = ['dreg2', 'dreg3', 'dreg4', '_Phys', 'sales']
    
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))
    
    df_reg0 = df_reg[ df_reg['_agegroup'] == 0] 
    #define independent and dependent variables
    Y = df_reg0['_fert']
    
    X = df_reg0[dummies + dyears + intte]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model1 = sm.OLS(WY,WX)
    reg1 = model1.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg1.summary()
    
    
    
    #2. second regression
    # dummies to create interaction terms with
    dummies = ['dreg2', 'dreg3', 'dreg4', '_Phys', 'sales', 'any']
    
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))
    
    df_reg0 = df_reg[ df_reg['_agegroup'] == 0] 
    #define independent and dependent variables
    Y = df_reg0['_fert']
    
    X = df_reg0[dummies + dyears + intte]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model2 = sm.OLS(WY,WX)
    reg2 = model2.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg2.summary()
    
    
    #3. third regression
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty']]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model3 = sm.OLS(WY,WX)
    reg3 = model3.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg3.summary()
    
    
    #create plot
    #create string list for interactions
    years = range(1951, 1981)
    int_string = []
    for k in years:
        int_string.append('salesXd{}'.format(k))
        
    coeff1 = reg1.params[int_string]
    conf1 = reg1.conf_int()
    conf_up1 = conf1[1][int_string]
    conf_low1 = conf1[0][int_string]
    
    coeff2 = reg2.params[int_string]
    conf2 = reg2.conf_int()
    conf_up2 = conf2[1][int_string]
    conf_low2 = conf2[0][int_string]
    
    coeff3 = reg3.params[int_string]
    conf3 = reg3.conf_int()
    conf_up3 = conf3[1][int_string]
    conf_low3 = conf3[0][int_string]
    
    plt.plot( years, coeff1, color = 'black',  label='Relative to states in same census region' )
    
    plt.ylim(-10,15)
    plt.plot(years, coeff2, color = 'red', label='Relative to states in same census region with advertising bans')
    plt.plot(years, coeff3,color = 'purple', label='Relative to states in same census region with advertising bans + covariates')
    l1 = plt.legend(bbox_to_anchor=(1.13,1),loc = 'lower right', prop={'size': 9})
    ax = plt.gca().add_artist(l1)
    plt.plot(years, conf_up1, color = 'black', linestyle = 'dashed')
    plt.plot(years, conf_low1, color = 'black', linestyle = 'dashed')
    
    plt.plot(years, conf_up2, color = 'red', linestyle = 'dashed')
    plt.plot(years, conf_low2, color = 'red', linestyle = 'dashed')
    
    plt.plot(years, conf_up3, color = 'purple', linestyle = 'dashed')
    plt.plot(years, conf_low3, color = 'purple', linestyle = 'dashed')
    v1 = plt.axvline(x=1965, ymin=-10, ymax=15, color = 'black', linestyle = 'dashed', label = 'Griswold decision')
    v2 = plt.axvline(x=1957, ymin=-10, ymax=15,color = 'black', linestyle = 'dotted', label = 'Envoid approved by FDA')
    plt.legend(handles = [v1,v2])
    plt.plot(years, np.repeat(0,len(years)), color = 'black', linewidth = 0.7)
    
    
    plt.ylabel('estimated interaction term')
    plt.xlabel('years')
    plt.show()


def gen_Fig4_B(df):
    """Function to create the plot from Figure 6 in Bailey (2010)
    
        Args:
        -------
        takes a data frame for which the results should be computed
        
        Returns:
        -------
        A figure containing the plot from Figure 6 in Bailey (2010)
    """
    wn.filterwarnings("ignore")
    

    #1. first regression
    #generate region dummy
    df_reg = df
    df_reg['dreg2'] = 0
    df_reg.loc[df_reg['_region'] == 2, 'dreg2'] = 1 
    df_reg['dreg3'] = 0
    df_reg.loc[df_reg['_region'] == 3, 'dreg3'] = 1
    df_reg['dreg4'] = 0
    df_reg.loc[df_reg['_region'] == 4, 'dreg4'] = 1 
    
    #generate year dummies, leave out 1950
    dyears = [] #initialize list for year dummies
    for i in range(1951, 1981):
        df_reg['d{}'.format(i)] = 0
        df_reg.loc[df_reg['year'] == i, 'd{}'.format(i)] = 1 
        dyears.append('d{}'.format(i))
    
    
    # dummies to create interaction terms with
    dummies = ['dreg2', 'dreg3', 'dreg4', '_Phys', 'sales']
    
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))
    
    statefix = []
    #create state fixed effects
    for s in df_reg['statefip'].unique()[1:]:
        df_reg['dstate{}'.format(s)] = 0
        df_reg.loc[df_reg['statefip'] == s, 'dstate{}'.format(s)] = 1    
        statefix.append('dstate{}'.format(s))
    
    df_reg0 = df_reg[ df_reg['_agegroup'] == 0] 
    #define independent and dependent variables
    Y = df_reg0['_fert']
    
    X = df_reg0[dummies + dyears + intte + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model1 = sm.OLS(WY,WX)
    reg1 = model1.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg1.summary()
    
    
    
    #2. second regression
    # dummies to create interaction terms with
    dummies = ['dreg2', 'dreg3', 'dreg4', '_Phys', 'sales', 'any']
    
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))
    
    df_reg0 = df_reg[ df_reg['_agegroup'] == 0] 
    #define independent and dependent variables
    Y = df_reg0['_fert']
    
    X = df_reg0[dummies + dyears + intte + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model2 = sm.OLS(WY,WX)
    reg2 = model2.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg2.summary()
    
    
    #3. third regression
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty']+ statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model3 = sm.OLS(WY,WX)
    reg3 = model3.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg3.summary()
    
    
    #create plot
    #create string list for interactions
    years = range(1951, 1981)
    int_string = []
    for k in years:
        int_string.append('salesXd{}'.format(k))
        
    coeff1 = reg1.params[int_string]
    conf1 = reg1.conf_int()
    conf_up1 = conf1[1][int_string]
    conf_low1 = conf1[0][int_string]
    
    coeff2 = reg2.params[int_string]
    conf2 = reg2.conf_int()
    conf_up2 = conf2[1][int_string]
    conf_low2 = conf2[0][int_string]
    
    coeff3 = reg3.params[int_string]
    conf3 = reg3.conf_int()
    conf_up3 = conf3[1][int_string]
    conf_low3 = conf3[0][int_string]
    
    plt.plot( years, coeff1, color = 'black',  label='Relative to states in same census region' )
    
    plt.ylim(-10,15)
    plt.plot(years, coeff2, color = 'red', label='Relative to states in same census region with advertising bans')
    plt.plot(years, coeff3,color = 'purple', label='Relative to states in same census region with advertising bans + covariates')
    l1 = plt.legend(bbox_to_anchor=(1.13,1),loc = 'lower right', prop={'size': 9})
    ax = plt.gca().add_artist(l1)
    plt.plot(years, conf_up1, color = 'black', linestyle = 'dashed')
    plt.plot(years, conf_low1, color = 'black', linestyle = 'dashed')
    
    plt.plot(years, conf_up2, color = 'red', linestyle = 'dashed')
    plt.plot(years, conf_low2, color = 'red', linestyle = 'dashed')
    
    plt.plot(years, conf_up3, color = 'purple', linestyle = 'dashed')
    plt.plot(years, conf_low3, color = 'purple', linestyle = 'dashed')
    v1 = plt.axvline(x=1965, ymin=-10, ymax=15, color = 'black', linestyle = 'dashed', label = 'Griswold decision')
    v2 = plt.axvline(x=1957, ymin=-10, ymax=15,color = 'black', linestyle = 'dotted', label = 'Envoid approved by FDA')
    plt.legend(handles = [v1,v2])
    plt.plot(years, np.repeat(0,len(years)), color = 'black', linewidth = 0.7)
    
    
    plt.ylabel('estimated interaction term')
    plt.xlabel('years')
    plt.show()

def gen_Fig4_C(df):
    """Function to create the plot from Figure 6 in Bailey (2010)
    
        Args:
        -------
        takes a data frame for which the results should be computed
        
        Returns:
        -------
        A figure containing the plot from Figure 6 in Bailey (2010)
    """
    df_reg = df
    
    #generate region dummy
    #df_reg = df
    df_reg['dreg1'] = 0
    df_reg.loc[df_reg['_region'] == 1, 'dreg1'] = 1
    df_reg['dreg2'] = 0
    df_reg.loc[df_reg['_region'] == 2, 'dreg2'] = 1 
    df_reg['dreg3'] = 0
    df_reg.loc[df_reg['_region'] == 3, 'dreg3'] = 1
    df_reg['dreg4'] = 0
    df_reg.loc[df_reg['_region'] == 4, 'dreg4'] = 1 
    
    #generate year dummies, leave out 1950
    dyears = [] #initialize list for year dummies
    for i in range(1951, 1981):
        df_reg['d{}'.format(i)] = 0
        df_reg.loc[df_reg['year'] == i, 'd{}'.format(i)] = 1 
        dyears.append('d{}'.format(i))
        
        
    statefix = []
    #create state fixed effects
    for s in df_reg['statefip'].unique()[1:]:
        df_reg['dstate{}'.format(s)] = 0
        df_reg.loc[df_reg['statefip'] == s, 'dstate{}'.format(s)] = 1    
        statefix.append('dstate{}'.format(s))
    
    #regression 1
    #create interaction terms
    dummies = ['dreg3', 'dreg4', '_Phys', 'sales', 'any']
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))

    
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 0) & (df_reg['_region'] != 1)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model1 = sm.OLS(WY,WX)
    reg1 = model1.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg1.summary()
    
    #regression 2
    #create interaction terms
    dummies = ['dreg3', 'dreg4', '_Phys', 'sales', 'any']
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))

    
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 0) & (df_reg['_region'] != 2)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model2 = sm.OLS(WY,WX)
    reg2 = model2.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg2.summary()
    
    #regression 3
    #create interaction terms
    dummies = ['dreg2', 'dreg4', '_Phys', 'sales', 'any']
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))

    
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 0) & (df_reg['_region'] != 3)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model3 = sm.OLS(WY,WX)
    reg3 = model3.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg3.summary()
    
    #regression 4
    #create interaction terms
    dummies = ['dreg2','dreg3', '_Phys', 'sales', 'any']
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))

    
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 0) & (df_reg['_region'] != 4)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model4 = sm.OLS(WY,WX)
    reg4 = model4.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg4.summary()
    
    #create plot
    #create string list for interactions
    years = range(1951, 1981)
    int_string = []
    for k in years:
        int_string.append('salesXd{}'.format(k))
        
    coeff1 = reg1.params[int_string]
    coeff2 = reg2.params[int_string]
    coeff3 = reg3.params[int_string]
    coeff4 = reg4.params[int_string]
    

    plt.plot( years, coeff1, color = 'brown',  label='Omit Northeast' )
    
    plt.ylim(-10,15)
    plt.plot(years, coeff2, color = 'red', label='Omit Midwest')
    plt.plot(years, coeff3,color = 'purple', label='Omit South')
    plt.plot(years, coeff4,color = 'orange', label='Omit West')
    l1 = plt.legend(bbox_to_anchor=(0.32,1),loc = 'lower right', prop={'size': 9})
    ax = plt.gca().add_artist(l1)

    v1 = plt.axvline(x=1965, ymin=-10, ymax=15, color = 'black', linestyle = 'dashed', label = 'Griswold decision')
    v2 = plt.axvline(x=1957, ymin=-10, ymax=15,color = 'black', linestyle = 'dotted', label = 'Envoid approved by FDA')
    plt.legend(handles = [v1,v2])
    plt.plot(years, np.repeat(0,len(years)), color = 'black', linewidth = 0.7)
    
    
    plt.ylabel('estimated interaction term')
    plt.xlabel('years')
    plt.show()
    
    
    
def gen_Fig4_D(df):
    """Function to create the plot from Figure 6 in Bailey (2010)
    
        Args:
        -------
        takes a data frame for which the results should be computed
        
        Returns:
        -------
        A figure containing the plot from Figure 6 in Bailey (2010)
    """
    df_reg = df
    #generate region dummy
    #df_reg = df
    df_reg['dreg1'] = 0
    df_reg.loc[df_reg['_region'] == 1, 'dreg1'] = 1
    df_reg['dreg2'] = 0
    df_reg.loc[df_reg['_region'] == 2, 'dreg2'] = 1 
    df_reg['dreg3'] = 0
    df_reg.loc[df_reg['_region'] == 3, 'dreg3'] = 1
    df_reg['dreg4'] = 0
    df_reg.loc[df_reg['_region'] == 4, 'dreg4'] = 1 
    
    #generate year dummies, leave out 1950
    dyears = [] #initialize list for year dummies
    for i in range(1951, 1981):
        df_reg['d{}'.format(i)] = 0
        df_reg.loc[df_reg['year'] == i, 'd{}'.format(i)] = 1 
        dyears.append('d{}'.format(i))
        
        
    statefix = []
    #create state fixed effects
    for s in df_reg['statefip'].unique()[1:]:
        df_reg['dstate{}'.format(s)] = 0
        df_reg.loc[df_reg['statefip'] == s, 'dstate{}'.format(s)] = 1    
        statefix.append('dstate{}'.format(s))
    
   
    #create interaction terms
    dummies = ['dreg2', 'dreg3', 'dreg4', '_Phys', 'sales', 'any']
    intte = []
    #create interactions
    for dum in dummies:
        for dy in dyears:
            df_reg['{}X{}'.format(dum,dy)] = df_reg[dum]*df_reg[dy]
            intte.append('{}X{}'.format(dum,dy))

    #regression 1
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 2)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model1 = sm.OLS(WY,WX)
    reg1 = model1.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg1.summary()
    
    #regression 2
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 3)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model2 = sm.OLS(WY,WX)
    reg2 = model2.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg2.summary()
    
    #regression 3
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 4)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model3 = sm.OLS(WY,WX)
    reg3 = model3.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg3.summary()
    
     #regression 4
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 5)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model4 = sm.OLS(WY,WX)
    reg4 = model4.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg4.summary()
    
    #regression 5
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 6)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model5 = sm.OLS(WY,WX)
    reg5 = model5.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg5.summary()
    
    #regression 6
    #define variables and run regression
    df_reg0 = df_reg[ (df_reg['_agegroup'] == 7)] 
    
    Y = df_reg0['_fert']
    X = df_reg0[dummies + dyears + intte + ['_farm', '_curmar', '_Nonwhite', '_fb', '_higrade', '_inctot', '_poverty'] + statefix]
    X['const'] = np.repeat(1, len(Y))
    
    W = np.sqrt(np.diag(df_reg0['pop']))
    WY = np.dot(W,Y)
    WX = np.dot(W,X)
    WX = pd.DataFrame(WX, columns = X.columns)
    
    model6 = sm.OLS(WY,WX)
    reg6 = model6.fit(cov_type='cluster', cov_kwds={'groups': df_reg0['statefip']})
    reg6.summary()
    
    #create plot
    #create string list for interactions
    years = range(1951, 1981)
    int_string = []
    for k in years:
        int_string.append('salesXd{}'.format(k))
        
    coeff1 = reg1.params[int_string]
    coeff2 = reg2.params[int_string]
    coeff3 = reg3.params[int_string]
    coeff4 = reg4.params[int_string]
    coeff5 = reg5.params[int_string]
    coeff6 = reg6.params[int_string]    

    plt.plot( years, coeff1, color = 'red',  label='Ages 15 to 19' )
    
    plt.ylim(-10,20)
    plt.plot(years, coeff2, color = 'purple', label='Ages 20 to 24')
    plt.plot(years, coeff3,color = 'navy', label='Ages 25 to 29')
    plt.plot(years, coeff4,color = 'brown', label='Ages 30 to 34')
    plt.plot(years, coeff5,color = 'purple', label='Ages 35 to 39')
    plt.plot(years, coeff6,color = 'orange', label='Ages 40 to 44')
    l1 = plt.legend(bbox_to_anchor=(0.32,1),loc = 'lower right', prop={'size': 9})
    ax = plt.gca().add_artist(l1)

    v1 = plt.axvline(x=1965, ymin=-10, ymax=15, color = 'black', linestyle = 'dashed', label = 'Griswold decision')
    v2 = plt.axvline(x=1957, ymin=-10, ymax=15,color = 'black', linestyle = 'dotted', label = 'Envoid approved by FDA')
    plt.legend(handles = [v1,v2])
    plt.plot(years, np.repeat(0,len(years)), color = 'black', linewidth = 0.7)
    
    
    plt.ylabel('estimated interaction term')
    plt.xlabel('years')
    plt.show()
    