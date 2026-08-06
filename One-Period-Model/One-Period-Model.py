#Data extraction

import yfinance as yf
appl=yf.download("AAPL",
                 start="2026-01-01",
                 end="2026-07-01",
                 progress=False)
bound=yf.download("^IRX",
                  start="2026-01-01",
                  end="2026-07-01",
                  progress=False)

A_0=appl["Close"].iloc[0].iloc[0]
B_0=bound["Close"].iloc[0].iloc[0]

A_1=appl["Close"].iloc[-1].iloc[-1]
B_1=bound["Close"].iloc[-1].iloc[-1]
#Assuming the quantity of stocks and bonds we will buy
x=10
y=20
#Equation for calculating stock and bond prices before and after investment
s1=(A_0*x)+(B_0*y)
s2=(A_1*x)+(B_1*y)

kV=(s2-s1)/s1

import matplotlib.pyplot as plt

apple_close = appl["Close"].iloc[:, 0]
bound_close = bound["Close"].iloc[:, 0]

portfolio_history = (apple_close * x) + (bound_close * y)
plt.figure(figsize=(12, 6))
plt.plot(portfolio_history,
         label="Total Portfolio Value (V)",
         color="#1f77b4",
         linewidth=2.5)

plt.title("Portfolio Value Growth Over Time ",
          fontsize=14,
          fontweight='bold',
          pad=15)
plt.xlabel("Date (التاريخ)",
           fontsize=12)
plt.ylabel("Total Value in USD ($ القيمة الإجمالية)",
           fontsize=12)
plt.grid(True,
         linestyle="--",
         alpha=0.6)
plt.legend(fontsize=11)
plt.show()

print("Total portfolio before investment s1:",s1)
print("Total portfolio after investment s2:",s2)
print("Total returns :",kV)
