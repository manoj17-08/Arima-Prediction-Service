
***

# Time Series Temperature Forecasting App

This project is a simple end‑to‑end time series forecasting demo that downloads a daily minimum temperature dataset, trains an ARIMA model in a Jupyter notebook, and serves interactive forecasts through a Flask web app. [attached_file:file:1][attached_file:file:2]

## Features

- Downloads the classic daily minimum temperatures dataset and saves it as `data.csv`. [attached_file:file:2]  
- Trains an ARIMA time series model on the temperature series using `statsmodels`. [attached_file:file:1][attached_file:file:2]  
- Exposes a `/forecast` endpoint with a `steps` query parameter to control forecast horizon. [attached_file:file:1]  
- Renders an HTML page (`index.html`) that displays the forecast produced by the Flask backend. [attached_file:file:1][attached_file:file:3]  
- Saves a 30‑day forecast to `forecast.csv` from the notebook for offline inspection. [attached_file:file:2]

## Project Structure

- `project.ipynb` – Notebook that:
  - Downloads the dataset from an online source and saves it as `data.csv`. [attached_file:file:2]
  - Performs exploratory analysis and ARIMA model training.
  - Generates a 30‑day forecast and writes it to `forecast.csv`. [attached_file:file:2]
- `app.py` – Flask application that:
  - Loads `data.csv`, prepares the daily temperature time series, and fits an ARIMA model. [attached_file:file:1]
  - Provides the `/forecast` route to generate forecasts and pass them to the template. [attached_file:file:1]
- `index.html` – Frontend template used by Flask to display forecast data. [attached_file:file:1][attached_file:file:3]  
- `forecast.csv` – Example CSV file containing a saved forecast from the notebook. [attached_file:file:2]

## Requirements

Make sure you have Python 3.10+ installed, then install the required packages:

- Flask  
- pandas  
- numpy  
- statsmodels  
- matplotlib  
- jupyter (to run the notebook)  

You can install them with:

- `pip install flask pandas numpy statsmodels matplotlib jupyter`  

The notebook also uses standard scientific Python stack components (such as `scipy`), which will be installed as dependencies. [attached_file:file:2]

## How to Run

1. Clone this repository and navigate into the project folder.  
2. (Optional) Create and activate a virtual environment.  
3. Run the notebook `project.ipynb` if you want to:
   - Re‑download the dataset into `data.csv`. [attached_file:file:2]
   - Retrain the ARIMA model or modify the analysis. [attached_file:file:2]
4. Start the Flask app:

   - `python app.py` [attached_file:file:1]

5. Open your browser and go to:

   - `http://127.0.0.1:5002/forecast?steps=30` to view a 30‑day forecast. [attached_file:file:1]

You can change the `steps` parameter (for example, `steps=7` or `steps=60`) to get different forecast horizons. [attached_file:file:1]

## Notes

- The ARIMA order is currently set to \((5, 1, 1)\); you can experiment with different orders in the notebook to improve performance. [attached_file:file:1][attached_file:file:2]  
- The dataset is treated as a daily frequency series, forward‑filled to handle any gaps before modeling. [attached_file:file:1]  
- `forecast.csv` is generated from the notebook and is not strictly required for the Flask app, which trains and forecasts directly from `data.csv`. [attached_file:file:1][attached_file:file:2]

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51022286/2e7c5ba9-33cf-4e97-b513-b34a84a91ce1/app.py)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51022286/811551f1-3ead-48f0-98dc-82c60b2eec95/project.ipynb)
[3](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51022286/36a4b18f-41d9-4a31-b72b-6d91d1453a2b/index.html)
