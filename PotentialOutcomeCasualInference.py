import numpy as np 
import pandas as pd 
import statsmodels.api as sm  
import statsmodels.formula.api as smf 
from itertools import combinations 
import plotnine as p

import ssl # 보안 관련 모듈 to deal with https access to github
ssl._create_default_https_context = ssl._create_unverified_context

# github에서 데이터 읽기.
def read_data(file): 
    return pd.read_stata("https://github.com/scunning1975/mixtape/raw/master/" + file)

# read data
yule = read_data('yule.dta')

# plot
res = sm.OLS.from_formula('paup ~ outrelief + old + pop', yule).fit()
print(res.summary())