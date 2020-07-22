import numpy as np
import matplotlib as mpl
import pandas as pd
from pylab import mpl, plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
%matplotlib inline

raw=pd.read_csv('/Data/suken.csv',index_col=0,parse_dates=True)

quotes=raw[['Open' ,'High','Low', 'Close']]
quotes=quotes.iloc[:]

import cufflinks as cf
import plotly.offline as plyo
qf=cf.QuantFig(quotes,title='USD_RUB',legend='top',name='USD_RUB Rate')

plyo.iplot(qf.iplot(asFigure=True),image='png',filename='qf_01')

qf.add_bollinger_bands(periods=15,boll_std=2)
plyo.iplot(qf.iplot(asFigure=True),image='png',filename='qf_02')

qf.add_rsi(periods=14, showbands=False)
plyo.iplot( qf.iplot(asFigure=True),image='png',filename='qf_03')

data.plot(figsize=(20,40),subplots=True)

print(data.info, data.describe().round(2), data.aggregate([min,np.mean,np.std,np.median,max]).round(2))

data.pct_change().mean().plot(kind='bar',figsize=(10,6))

rets=np.log(data/data.shift())

rets.cumsum().apply(np.exp).plot(linewidth=0.5,figsize=(10,6))

rets.cumsum().apply(np.exp). resample('1m', label='right').last( ).plot(linewidth=0.5,figsize=(10, 6))


