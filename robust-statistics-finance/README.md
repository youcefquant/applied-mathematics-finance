# Quantitative Finance: Estimates of Location in Financial Returns (AAPL)

An exploratory data analysis (EDA) project applying robust statistics—specifically **Mean**, **Median**, and **Trimmed Mean**—to Apple Inc. (`AAPL`) daily stock returns using Python and real-time market data from Yahoo Finance.

---

## 📌 Overview & Mathematical Foundations

In financial quantitative analysis, standard arithmetic estimates can be heavily distorted by market volatility, news shocks, and extreme candle spikes (outliers). Understanding how central tendencies behave requires comparing different statistical estimators:

### 1. Arithmetic Mean ($\bar{x}$)
The sum of all daily returns divided by the total number of observations ($n$). It measures the expected value under a standard normal distribution but is highly sensitive to extreme price movements.

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

### 2. Median ($\text{Med}$)
The middle value when all daily returns are ordered sequentially. If $n$ is even, it represents the average of the two central numbers. It represents the 50th percentile and is completely robust against extreme outliers.

$$\text{Med}(X) = \begin{cases} x_{\left(\frac{n+1}{2}\right)} & \text{if } n \text{ is odd} \\ \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2} + 1\right)}}{2} & \text{if } n \text{ is even} \end{cases}$$

### 3. Trimmed Mean ($\bar{x}_p$)
Calculated by sorting the daily returns and trimming a fraction $p$ (e.g., $p = 0.05$ or $5\%$) of the smallest and largest values before taking the average of the remaining $(n - 2k)$ values (where $k = \lfloor n \cdot p \rfloor$). It filters market noise while retaining most of the dataset.

$$\bar{x}_p = \frac{1}{n - 2k} \sum_{i=k+1}^{n-k} x_{(i)}$$

---

## 🛠️ Tech Stack & Dependencies

* **Python 3.10+**
* `yfinance` - For fetching historical stock data.
* `numpy` & `pandas` - For mathematical transformations and data processing.
* `scipy` - For robust statistical computations (`stats.trim_mean`).
* `matplotlib` - For plotting time series and visual statistical levels.

---

## 💻 Source Code

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import yfinance as yf

# 1. Fetch Apple Inc. historical price data (1 Year)
df = yf.download("AAPL", period="1y", multi_level_index=False)

# 2. Compute daily percentage returns and drop NaN initial values
df["rtn"] = df["Close"].pct_change()
rtn = df["rtn"].dropna()

# 3. Calculate statistical central location estimates
mean_rtn = np.mean(rtn)
median_rtn = np.median(rtn)
trimed_rtn = stats.trim_mean(rtn, proportiontocut=0.05)

# 4. Output formatted percentage results
print(f"Mean Return:        {mean_rtn:.4%}")
print(f"Median Return:      {median_rtn:.4%}")
print(f"Trimmed Mean (5%): {trimed_rtn:.4%}")

# 5. Visualizing time series returns with Trimmed Mean reference line
rtn.plot(
    figsize=(10, 5), label="Daily Return", color="gray", alpha=0.6
)

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
