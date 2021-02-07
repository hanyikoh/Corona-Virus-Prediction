
import numpy as np
import pickle
from flask import Flask, render_template, request, url_for


model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    data1 = request.form['date']
    arr = np.array([data1])
    pred = model.predict(arr)

    return render_template('index.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
