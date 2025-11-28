# download_data.py
import pandas as pd

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
df = pd.read_csv(url)
df.to_csv("data.csv", index=False)
print("Downloaded dataset saved as data.csv")


!pip install pandas numpy matplotlib statsmodels scipy jupyter


# forecast.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings

warnings.filterwarnings("ignore")

# ------------------------------
# Load dataset
# ------------------------------
df = pd.read_csv("data.csv", parse_dates=["Date"])
df = df.sort_values("Date").set_index("Date")
ts = df["Temp"].asfreq("D")
ts = ts.fillna(method="ffill")

# ------------------------------
# Stationarity Check
# ------------------------------
def check_stationarity(series):
    result = adfuller(series.dropna())
    print("\nADF Statistic:", result[0])
    print("p-value:", result[1])
    if result[1] < 0.05:
        print("Series is likely stationary.")
    else:
        print("Series is NOT stationary.")

print("Original Series Stationarity:")
check_stationarity(ts)

# ------------------------------
# Plot original series
# ------------------------------
plt.figure(figsize=(10, 4))
plt.plot(ts)
plt.title("Daily Minimum Temperatures")
plt.show()

# ------------------------------
# Create difference series (for ACF/PACF)
# ------------------------------
ts_diff = ts.diff().dropna()
print("\nDifferenced Series Stationarity:")
check_stationarity(ts_diff)

plt.figure(figsize=(10, 4))
plt.plot(ts_diff)
plt.title("Differenced Series")
plt.show()

# ------------------------------
# Plot ACF and PACF
# ------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(ts_diff, ax=axes[0])
plot_pacf(ts_diff, ax=axes[1])
plt.show()

# ------------------------------
# Fit ARIMA model
# ------------------------------
order = (5, 1, 1)  # safe ARIMA order for this dataset
model = ARIMA(ts, order=order)
res = model.fit()
print(res.summary())

# ------------------------------
# Forecast next 30 days
# ------------------------------
steps = 30
forecast = res.get_forecast(steps=steps)
pred_mean = forecast.predicted_mean
conf = forecast.conf_int()

# ------------------------------
# Plot forecast
# ------------------------------
plt.figure(figsize=(10, 4))
plt.plot(ts, label="Historical")
plt.plot(pred_mean, label="Forecast", color="red")
plt.fill_between(conf.index, conf.iloc[:, 0], conf.iloc[:, 1], color="pink", alpha=0.3)
plt.title("30-Day Temperature Forecast")
plt.legend()
plt.show()

# ------------------------------
# Save forecast
# ------------------------------
pred_mean.to_csv("forecast.csv")
print("\nForecast saved to forecast.csv")
