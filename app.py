import numpy as np
from flask import Flask,request,jsonify,render_template,url_for
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	model = joblib.load("wind_energy.pkl")
	x_test = [[str(x) for x in request.form.values()]]
	#print(x_test)
	prediction = model.predict(x_test)
	#print(prediction)
	output=prediction[0]
	return render_template('index.html',prediction_text='Energy Output of Wind Turbine (in kW) is {}'.format(output))
        

if __name__ == "__main__":
    app.run(debug=True)
