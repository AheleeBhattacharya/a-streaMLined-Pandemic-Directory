from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *

import pickle
import numpy as np
model = pickle.load(open('covid_med_age_vs_total_death_regression_model.pkl', 'rb'))

app = Flask(__name__)

def predict():
    Median_age = input("Enter the median age of your country", type=NUMBER)
    value = np.array(Median_age).reshape(-1, 1)
    prediction = model.predict(value)
    put_text(f'Predicted total deaths per million: {prediction}')


if __name__ == '__main__':
    predict()
app.run()

