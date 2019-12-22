# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

from stats import d2, D3, D4
from stats import XMR

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# %% [markdown]
# # SPC

# %%
df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y')


# %%
xmr_A = XMR(df['A'].values, index=df['date'].values)
xmr_B = XMR(df['B'].values, index=df['date'].values)


# %%
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey='row', tight_layout=True)
ax = axes.flatten()

xmr_A.xchart(ax[0])
xmr_A.mrchart(ax[2])
xmr_B.xchart(ax[1], color='orange')
xmr_B.mrchart(ax[3], color='orange')

ax[0].xaxis.set_major_locator(mdates.WeekdayLocator()) # major ticks every start of week
ax[0].xaxis.set_minor_locator(mdates.DayLocator()) # minor ticks every day
ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.setp(ax[2].get_xticklabels(), rotation=45)
plt.setp(ax[3].get_xticklabels(), rotation=45)
ax[0].set_ylabel('X')
ax[2].set_ylabel('MR')
ax[0].set_title('A')
ax[1].set_title('B')

plt.show()


# %%
axes = df.plot(x='date', y='A', marker='o', )
df.plot(x='date', y='B', marker='o', ax=axes, color='orange')

axes.legend()
axes.xaxis.set_major_locator(mdates.WeekdayLocator()) # major ticks every start of week
axes.xaxis.set_minor_locator(mdates.DayLocator()) # minor ticks every day
axes.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.setp(axes.get_xticklabels(), rotation=45)
axes.set_ylabel('X')

plt.show()


# %%


