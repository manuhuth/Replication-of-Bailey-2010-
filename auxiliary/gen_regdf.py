import warnings as wn

def gen_regdf(df):
    """Function to create the relevant dummy variables and interaction terms for the probit models.
    
        Args:
        dataFrame containing the categorial variables
        
        Returns:
        -------
        A data frame containing the dummy variables and interaction terms needed for the regression
    """
    wn.filterwarnings("ignore")
    
    #general
    df['cstck_b465'] =  0
    df.loc[df['cstck'] < 1965, 'cstck_b465'] = 1 

    df_reg = df

    #generate region dummy
    df_reg['dreg2'] = 0
    df_reg.loc[df_reg['_region'] == 2, 'dreg2'] = 1 
    df_reg['dreg3'] = 0
    df_reg.loc[df_reg['_region'] == 3, 'dreg3'] = 1
    df_reg['dreg4'] = 0
    df_reg.loc[df_reg['_region'] == 4, 'dreg4'] = 1 
    
        #generate 1970 dummy
    df_reg['d1970'] = 0
    df_reg.loc[ df_reg['year'] == 1970, 'd1970'] = 1 
    
    df_reg['d1965'] = 0
    df_reg.loc[ df_reg['year'] == 1965, 'd1965'] = 1 
    
        #generate interaction terms
    df_reg['dsalesX1970'] = df_reg['sales']*df_reg['d1970']
    df_reg['d_PhysX1970'] = df_reg['_Phys']*df_reg['d1970']
    df_reg['dreg2X1970'] = df_reg['dreg2']*df_reg['d1970']
    df_reg['dreg3X1970'] = df_reg['dreg3']*df_reg['d1970']
    df_reg['dreg4X1970'] = df_reg['dreg4']*df_reg['d1970']
    df_reg['dsalesX1965'] = df_reg['sales']*df_reg['d1965']
    df_reg['d_PhysX1965'] = df_reg['_Phys']*df_reg['d1965']
    df_reg['dreg2X1965'] = df_reg['dreg2']*df_reg['d1965']
    df_reg['dreg3X1965'] = df_reg['dreg3']*df_reg['d1965']
    df_reg['dreg4X1965'] = df_reg['dreg4']*df_reg['d1965']
        #generate any interaction term
    df_reg['anyX1970'] = df_reg['any']*df_reg['d1970']
    df_reg['anyX1965'] = df_reg['any']*df_reg['d1965']
    
        #generate dummies for _agecat
    df_reg['d_agecat20'] = 0
    df_reg.loc[df_reg['_agecat'] == 20, 'd_agecat20'] = 1
    
    df_reg['d_agecat25'] = 0
    df_reg.loc[df_reg['_agecat'] == 25, 'd_agecat25'] = 1
    
    df_reg['d_agecat30'] = 0
    df_reg.loc[df_reg['_agecat'] == 30, 'd_agecat30'] = 1
    
    df_reg['d_agecat35'] = 0
    df_reg.loc[df_reg['_agecat'] == 35, 'd_agecat35'] = 1
    
        #generate interaction terms 1970 and d_agecatXX
    df_reg['d_agecat20X1970'] = df_reg['d_agecat20']*df_reg['d1970']
    df_reg['d_agecat25X1970'] = df_reg['d_agecat25']*df_reg['d1970']
    df_reg['d_agecat30X1970'] = df_reg['d_agecat30']*df_reg['d1970']
    df_reg['d_agecat35X1970'] = df_reg['d_agecat35']*df_reg['d1970']
    df_reg['d_agecat20X1965'] = df_reg['d_agecat20']*df_reg['d1965']
    df_reg['d_agecat25X1965'] = df_reg['d_agecat25']*df_reg['d1965']
    df_reg['d_agecat30X1965'] = df_reg['d_agecat30']*df_reg['d1965']
    df_reg['d_agecat35X1965'] = df_reg['d_agecat35']*df_reg['d1965']
    
    
        #generate interaction term _Catholic 
    df_reg['_CatholicX1970'] = df_reg['_Catholic']*df_reg['d1970']
    df_reg['_CatholicX1965'] = df_reg['_Catholic']*df_reg['d1965'] 
        #generate dummies _ed_cat
    df_reg['d_ed_cat9'] = 0
    df_reg.loc[df_reg['_ed_cat'] == 9, 'd_ed_cat9'] = 1
    
    df_reg['d_ed_cat12'] = 0
    df_reg.loc[df_reg['_ed_cat'] == 12, 'd_ed_cat12'] = 1
    
    df_reg['d_ed_cat13'] = 0
    df_reg.loc[df_reg['_ed_cat'] == 13, 'd_ed_cat13'] = 1
    
    df_reg['d_ed_cat16'] = 0
    df_reg.loc[df_reg['_ed_cat'] == 16, 'd_ed_cat16'] = 1
    
        #generate interaction terms d_ed_cat
    df_reg['d_ed_cat9X1970'] = df_reg['d_ed_cat9']*df_reg['d1970']
    df_reg['d_ed_cat12X1970'] = df_reg['d_ed_cat12']*df_reg['d1970']
    df_reg['d_ed_cat13X1970'] = df_reg['d_ed_cat13']*df_reg['d1970']
    df_reg['d_ed_cat16X1970'] = df_reg['d_ed_cat16']*df_reg['d1970']
    
    df_reg['d_ed_cat9X1965'] = df_reg['d_ed_cat9']*df_reg['d1965']
    df_reg['d_ed_cat12X1965'] = df_reg['d_ed_cat12']*df_reg['d1965']
    df_reg['d_ed_cat13X1965'] = df_reg['d_ed_cat13']*df_reg['d1965']
    df_reg['d_ed_cat16X1965'] = df_reg['d_ed_cat16']*df_reg['d1965']
    
        #generate dummies _hinccat
    df_reg['d_hinccat1'] = 0
    df_reg.loc[df_reg['_hinccat'] == 1, 'd_hinccat1'] = 1
    
    df_reg['d_hinccat2'] = 0
    df_reg.loc[df_reg['_hinccat'] == 2, 'd_hinccat2'] = 1
    
    df_reg['d_hinccat3'] = 0
    df_reg.loc[df_reg['_hinccat'] == 3, 'd_hinccat3'] = 1
    
    df_reg['d_hinccat4'] = 0
    df_reg.loc[df_reg['_hinccat'] == 4, 'd_hinccat4'] = 1
    
        #generate interaction terms d_hinccat
    df_reg['d_hinccat1X1970'] = df_reg['d_hinccat1']*df_reg['d1970']
    df_reg['d_hinccat2X1970'] = df_reg['d_hinccat2']*df_reg['d1970']
    df_reg['d_hinccat3X1970'] = df_reg['d_hinccat3']*df_reg['d1970']
    df_reg['d_hinccat4X1970'] = df_reg['d_hinccat4']*df_reg['d1970']
    
    df_reg['d_hinccat1X1965'] = df_reg['d_hinccat1']*df_reg['d1965']
    df_reg['d_hinccat2X1965'] = df_reg['d_hinccat2']*df_reg['d1965']
    df_reg['d_hinccat3X1965'] = df_reg['d_hinccat3']*df_reg['d1965']
    df_reg['d_hinccat4X1965'] = df_reg['d_hinccat4']*df_reg['d1965']
    
        #generate dummies _idealcat
    df_reg['d_idealcat2'] = 0
    df_reg.loc[df_reg['_idealcat'] == 2, 'd_idealcat2'] = 1
    
    df_reg['d_idealcat3'] = 0
    df_reg.loc[df_reg['_idealcat'] == 3, 'd_idealcat3'] = 1
    
    df_reg['d_idealcat4'] = 0
    df_reg.loc[df_reg['_idealcat'] == 4, 'd_idealcat4'] = 1
    
    df_reg['d_idealcat5'] = 0
    df_reg.loc[df_reg['_idealcat'] == 5, 'd_idealcat5'] = 1
    
        #generate interaction terms d_hinccat
    df_reg['d_idealcat2X1970'] = df_reg['d_idealcat2']*df_reg['d1970']
    df_reg['d_idealcat3X1970'] = df_reg['d_idealcat3']*df_reg['d1970']
    df_reg['d_idealcat4X1970'] = df_reg['d_idealcat4']*df_reg['d1970']
    df_reg['d_idealcat5X1970'] = df_reg['d_idealcat5']*df_reg['d1970']
    
    df_reg['d_idealcat2X1965'] = df_reg['d_idealcat2']*df_reg['d1965']
    df_reg['d_idealcat3X1965'] = df_reg['d_idealcat3']*df_reg['d1965']
    df_reg['d_idealcat4X1965'] = df_reg['d_idealcat4']*df_reg['d1965']
    df_reg['d_idealcat5X1965'] = df_reg['d_idealcat5']*df_reg['d1965']


    return df_reg