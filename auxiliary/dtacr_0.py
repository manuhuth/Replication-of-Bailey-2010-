import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels as sm
from statsmodels.discrete.discrete_model import Probit
import scipy.stats as ss

df_popms1 = pd.read_stata('C:/Users/Mhuth/Documents/microeconometrics-course-project-manuhuth/data/popmeasures80_rev.dta', convert_categoricals = False)
df_cov1 = pd.read_stata('C:/Users/Mhuth/Documents/microeconometrics-course-project-manuhuth/data/covariates80_rev.dta', convert_categoricals = False)

for i in range(2,8):
    df_cov1.loc[ df_cov1['_agegroup'] == (i+1)*5, '_agegroup' ] = i
    

df_nat5080_1 = pd.read_stata('C:/Users/Mhuth/Documents/microeconometrics-course-project-manuhuth/data/nat5080_1.dta', convert_categoricals = False)