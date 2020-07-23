import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set(color_codes=True)
#sns.set(style="whitegrid", color_codes=True)
np.random.seed(sum(map(ord, "distributions")))
from scipy import stats,integrate

import cufflinks as cf
import plotly.offline as plyo

raw=pd.read_csv('./Data/601952.SS.csv',index_col=0,parse_dates=True)
raw2=pd.read_csv('./Data/000001.SS.csv',index_col=0,parse_dates=True)
cols=['Open' ,'High','Low', 'Close','Volume']
quotes=raw[cols]
quotes_base=raw2[cols]
q_calc=quotes*500/quotes_base
q_calc.Volume/=300
q_calc.dropna(inplace=True)
q_calc.Volume.replace([np.inf, -np.inf], 229,inplace=True)
q_calc.Volume.replace(np.nan,0,inplace=True)

qf1=cf.QuantFig(quotes,title='Suken',legend='top',name='Suken Stock')
qf2=cf.QuantFig(quotes_base,title='Shanghai',legend='top',name='Shanghai Index')
qf3=cf.QuantFig(q_calc,title='Scale',legend='top',name='Suken/Shanghai')

plyo.iplot(qf1.iplot(asFigure=True),image='png',filename='qf1_1')
qf1.add_bollinger_bands(periods=15,boll_std=2)
plyo.iplot(qf1.iplot(asFigure=True),image='png',filename='qf1_2')
qf1.add_bollinger_bands(periods=15,boll_std=2)
plyo.iplot(qf1.iplot(asFigure=True),image='png',filename='qf1_3')

plyo.iplot(qf2.iplot(asFigure=True),image='png',filename=f'qf2_01')
qf2.add_bollinger_bands(periods=15,boll_std=2)
plyo.iplot(qf2.iplot(asFigure=True),image='png',filename=f'qf2_02')
qf2.add_rsi(periods=14, showbands=False)
plyo.iplot(qf2.iplot(asFigure=True),image='png',filename=f'qf2_03')

plyo.iplot(qf3.iplot(asFigure=True),image='png',filename=f'qf3_01')
qf3.add_bollinger_bands(periods=15,boll_std=2)
plyo.iplot(qf3.iplot(asFigure=True),image='png',filename=f'qf3_02')
qf3.add_rsi(periods=14, showbands=False)
plyo.iplot(qf3.iplot(asFigure=True),image='png',filename=f'qf3_03')

fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(15,3))
sns_plot = sns.distplot(quotes['Close'],rug=True,ax=ax1)
sns_plot = sns.distplot(quotes['Open'],rug=True,ax=ax2)
sns_plot = sns.distplot(quotes['Volume'],rug=True,ax=ax3)
fig.savefig('./Data/quotes_hist.png')

fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(15,3))
sns_plot = sns.distplot(quotes_base['Close'],rug=True,ax=ax1)
sns_plot.savefig('quotes_close.png')
sns_plot = sns.distplot(quotes_base['Open'],rug=True,ax=ax2)
sns_plot = sns.distplot(quotes_base['Volume'],rug=True,ax=ax3)
fig.savefig('./Data/quotes_base_hist.png')

fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(15,3))
sns_plot = sns.distplot(q_calc['Close'],rug=True,ax=ax1)
sns_plot = sns.distplot(q_calc['Open'],rug=True,ax=ax2)
sns_plot = sns.distplot(q_calc['Volume'],rug=True,ax=ax3)
fig.savefig('./Data/quotes_calc_hist.png')

sns.jointplot(x='Close',y='Volume', data=quotes,color='m', kind='hex').savefig('./Data/jp1.png')
sns.jointplot(x='Close',y='Volume', data=quotes_base, kind='kde').savefig('./Data/jp2.png')
sns.jointplot(x='Close',y='Volume', data=q_calc).savefig('./Data/jp3.png')

sns.pairplot(quotes).savefig('./Data/quotes_pairplot.png')
sns.pairplot(quotes_base).savefig('./Data/quotes_base_pairplot.png')
sns.pairplot(q_calc).savefig('./Data/q_calc_pairplot.png')