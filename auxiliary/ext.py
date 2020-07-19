import pandas as pd
import numpy as np



def sim_start_val1(models, df, cluster_by, meth ='newton', numb_it = '100', up_bound = 1, low_bound = -1):
    """Function to create different parameter values for random starting values of the models used in section 5.
    
        Args:
        models: list of models to evaluate the parameters for
        meth: optimization method, default is Newton-Raphson
        numb_it: number of draws
        up/low_bound: upper and lower bounds for random draw of starting values from a uniform distribution
        
        Returns:
        -------
        A data frame containing the results for both parameter
    """
    df_results = pd.DataFrame()
    model_num = 0
    for u in models:
        model_num = model_num + 1
        n_params = u.exog.shape[1]
        par_sales = []
        par_interact = []

        for v in range(0,numb_it):
            start = np.random.uniform(low_bound, up_bound, n_params)
            fit = u.fit(cov_type='cluster', cov_kwds={'groups': df[cluster_by]}, disp = False, start_params = start, method = meth)
            margins = fit.get_margeff()
            par_sales.append(margins.margeff[0])
            par_interact.append(margins.margeff[2]) 
        df_results['sales_model{}'.format(model_num)] = par_sales
        df_results['interact_1970_model{}'.format(model_num)] = par_interact
    return df_results


def sim_start_val2(models, df, cluster_by, meth ='newton', numb_it = '100', up_bound = 1, low_bound = -1):
    """Function to create different parameter values for random starting values of the models used in section 5.
    
        Args:
        models: list of models to evaluate the parameters for
        meth: optimization method, default is Newton-Raphson
        numb_it: number of draws
        up/low_bound: upper and lower bounds for random draw of starting values from a uniform distribution
        
        Returns:
        -------
        A data frame containing the results for the three parameter
    """
    df_results = pd.DataFrame()
    model_num = 0
    for u in models:
        model_num = model_num + 1
        n_params = u.exog.shape[1]
        par_sales = []
        par_interact_1970 = []
        par_interact_1965 = []

        for v in range(0,numb_it):
            start = np.random.uniform(low_bound, up_bound, n_params)
            fit = u.fit(cov_type='cluster', cov_kwds={'groups': df[cluster_by]}, disp = False, start_params = start, method = meth)
            margins = fit.get_margeff()
            par_sales.append(margins.margeff[0])
            par_interact_1970.append(margins.margeff[3]) 
            par_interact_1965.append(margins.margeff[4]) 
        df_results['sales_model{}'.format(model_num)] = par_sales
        df_results['interact_1970_model{}'.format(model_num)] = par_interact_1970
        df_results['interact_1965_model{}'.format(model_num)] = par_interact_1965
    return df_results