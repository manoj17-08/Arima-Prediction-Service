# app.py

from flask import Flask, jsonify, request, render_template # <-- ADDED render_template
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load data & train model
df = pd.read_csv("data.csv", parse_dates=["Date"])
df = df.sort_values("Date").set_index("Date")
ts = df["Temp"].asfreq("D").fillna(method="ffill")


model = ARIMA(ts, order=(5,1,1))
res = model.fit()

@app.route("/forecast", methods=["GET"])
def forecast():
    steps = int(request.args.get("steps", 30))
    pred = res.get_forecast(steps=steps).predicted_mean
    
    # 1. Convert Timestamps to Strings (as before)
    pred_df = pred.to_frame(name="prediction")
    pred_df.index = pred_df.index.strftime('%Y-%m-%d')
    
    # 2. Get the final dictionary of data
    forecast_dict = pred_df['prediction'].to_dict()
    
    # --- CHANGE: Render the HTML template, passing the data and steps ---
    return render_template(
        'index.html', 
        forecast_data=forecast_dict, 
        steps=steps
    )
    
if __name__ == "__main__":
    app.run(debug=True, port=5002)