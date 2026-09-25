import numpy as np
import pandas as pd
from scipy import stats
import yfinance as yf
#downlaod data form yahoo finance
df=yf.download("AAPL",
               period="1y",
               multi_level_index=False)
df["rtn"]=df["Close"].pct_change()
rtn=df["rtn"].dropna()

mean_rtn=np.mean(rtn)
median_rtn=np.median(rtn)
trimed_rtn=stats.trim_mean(
    rtn,proportiontocut=0.05
)
print(f"Mean Return:        {mean_rtn:.4%}")
print(f"Median Return:      {median_rtn:.4%}")
print(f"Trimmed Mean (5%): {trimed_rtn:.4%}")
import matplotlib.pyplot as plt

rtn.plot(figsize=(10, 5),
         label="Daily Return",
         color="gray",
         alpha=0.6)

plt.axhline(
    y=trimed_rtn,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"Trimmed Mean: {trimed_rtn:.4%}",
)
plt.title("AAPL Daily Returns with Trimmed Mean")
plt.ylabel("Return")
plt.legend()
plt.show()

