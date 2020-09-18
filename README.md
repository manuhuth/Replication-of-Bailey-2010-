The project was part of the 2020 iteration of the Microeconometrics course (Matser of Science in Economics at the University of Bonn) taught by [Philipp Eisenhauer](https://github.com/peisenha).

# Student project: Replication of Bailey (2010)

This repository contains my replication approach of the results of 
> Bailey (2010). “Momma’s Got the Pill”: How Anthony Comstock and Griswold v. Connecticut Shaped US Childbearing. *American Economic Review*, 100:1, 98–129.

The following badges allow easy access to the project's notebook

[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/HumanCapitalAnalysis/microeconometrics-course-project-manuhuth/blob/master/replication-notebook.ipynb)

<a href="https://mybinder.org/v2/gh/HumanCapitalAnalysis/microeconometrics-course-project-manuhuth/master?filepath=replication-notebook.ipynb"
    target="_parent">
    <img align="center"
       src="https://mybinder.org/badge_logo.svg"
       width="109" height="20">
</a>

## Continous integration with Travis CI to ensure Reproducibility
I have integrated a continous integration service with Travis CI. It can be found here [![Build Status](https://travis-ci.org/HumanCapitalAnalysis/microeconometrics-course-project-manuhuth.svg?branch=master)](https://travis-ci.org/HumanCapitalAnalysis/microeconometrics-course-project-manuhuth)

## Replication of Bailey (2010)
In Bailey's [(2010)](https://pubs.aeaweb.org/doi/pdfplus/10.1257/aer.100.1.98) main analysis she tries to quantify the importance of the birth control pill for marital childbearing in the 1960s. The first birth control pill, the Envoid, had been introduced in 1957 and was followed by a start of a new era in US demographics in the 1960s. Lower fertility rates, of around 50\%, and smaller family sizes occurred and have never changed back until today. Bailey (2010) uses data from National Surveys and makes use of the heterogenous laws for the use of contraception methods in the early 1960s to find differences in fertility rates that can be related to the use of oral contraception. She finds evidence that the introduction of the pill reduced marital childbearing in the US in the 1960s and the subsequent years.

The main part of my project is the replication of the results from Bailey (2010). I present her identification strategy using a causal graph and a review of the econometric methods she used and discuss her results. Additionally, I provide extensions to validate the robustness of the results by checking the common trend assumptions, establishing a model to quantify the effect of the sales bans and using different starting values for the models with numerical optimizaion methods.  


## This Repository
My replication, which is conducted in Python, is depicted in the Jupyter notebook. [replication-notebook.ipynb](https://github.com/HumanCapitalAnalysis/microeconometrics-course-project-manuhuth/blob/master/replication-notebook.ipynb). To ensure appropriate formatting and enumeration of equations, the best way to view my notebook is by downloading the [repository](https://github.com/HumanCapitalAnalysis/microeconometrics-course-project-manuhuth) from GitHub. Alternatively, mybinder <a href="https://mybinder.org/v2/gh/HumanCapitalAnalysis/microeconometrics-course-project-manuhuth/master?filepath=replication-notebook.ipynb"
    target="_parent">
    <img align="center"
       src="https://mybinder.org/badge_logo.svg"
       width="109" height="20">
</a> and nbviewer [![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/HumanCapitalAnalysis/microeconometrics-course-project-manuhuth/blob/master/replication-notebook.ipynb) provide convenient ways of accessing the notebook. 

The original data and the code provided by the authors can be accessed [here](https://www.openicpsr.org/openicpsr/project/112340/version/V1/view) and the paper following this [link](https://pubs.aeaweb.org/doi/pdfplus/10.1257/aer.100.1.98).

## References
> Abadie, A., Athey, S., Imbens, G. W., and Wooldridge, J. (2017). When should you adjust standard errors for clustering? (No. w24003). National Bureau of Economic Research. [(link)](https://economics.mit.edu/files/13927)

> Angrist, J. D. and Pischke, J.-S. (2009). Mostly Harmless Econometrics: An Empiricist’s Companion.  Princeton University Press 
[(link)](https://www.researchgate.net/publication/51992844_Mostly_Harmless_Econometrics_An_Empiricist%27s_Companion)

> Bailey, M. J. (2010).  “Momma’s Got the Pill”: How Anthony Comstock and Griswold v. Connecticut Shaped US Childbearing. American Economic Review, 100:1, 98–129. [(link)](https://pubs.aeaweb.org/doi/pdfplus/10.1257/aer.100.1.98)

> Bailey, M. J. (2010).  “Momma’s Got the Pill”: How Anthony Comstock and Griswold v. Connecticut Shaped US Childbearing - data. [(link)](https://www.openicpsr.org/openicpsr/project/112340/version/V1/view)

> Bailey, M. J. (2010).  “Momma’s Got the Pill”: How Anthony Comstock and Griswold v. Connecticut Shaped US Childbearing - legal appendix. [(link)](http://www-personal.umich.edu/~baileymj/Bailey_Griswold_Legal_Appendix.pdf)

> Bailey, M. J. (2010).  “Momma’s Got the Pill”: How Anthony Comstock and Griswold v. Connecticut Shaped US Childbearing - sensitivity analysis. [(link)](http://www-personal.umich.edu/~baileymj/Bailey_Griswold_Sensitivity_Appendix.pdf)

> Bartus, T. (2005). Estimation of marginal effects using margeff. The Stata journal, *5*, 3, 309-329. [(link)](https://journals.sagepub.com/doi/pdf/10.1177/1536867X0500500303)

> Eisenhauer, P. (2020). Course project template, HumanCapitalAnalysis [(link)](https://github.com/HumanCapitalAnalysis/template-course-project.)

> Gehlen, A. (2019). Replication of Jason M. Lindo, Nicholas J. Sanders & Philip Oreopoulos (2010). [(link)](https://github.com/amageh/replication-performance-standards/blob/master/replication-notebook.ipynb)

> Kim, K. and Lee, M. (2019). Difference in differences in reverse. Empirical Economics 57(3):1-21 [(link)](https://www.researchgate.net/publication/325570354_Difference_in_differences_in_reverse)

> Michael, R. T. and Willis, R. J. (1976). Contraception and Fertility: Household Production under Uncertainty. National Bureau of Economic Research. [(link)](https://www.nber.org/chapters/c3960.pdf) 
