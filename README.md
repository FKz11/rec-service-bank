# Predicting the response to the bank's service

## Files:
* `main.ipynb`: Colab notebook with exploratory data analysis
* `app.py`: Streamlit app file
* `requirements.txt`: package requirements files
* `/data` folder has:
  * `clients.csv`: dataset
  * and png visualizations for EDA

## Service:
Streamlit service is available at [rec-service-bank.streamlit.app](https://rec-service-bank.streamlit.app/) via Streamlit Cloud

To run locally, clone the repo and do the following:
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
```
The app will be available at `http://localhost:8501`