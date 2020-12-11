from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "eyJraWQiOiIyMDIwMTEyMTE4MzQiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC01NTAwMDhSV0FOIiwiaWQiOiJJQk1pZC01NTAwMDhSV0FOIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiY2EyZmY5M2UtYTBkNi00Zjg0LTljZDgtYjcyZTJjYWE2ODIzIiwiaWRlbnRpZmllciI6IjU1MDAwOFJXQU4iLCJnaXZlbl9uYW1lIjoiUml0dSIsImZhbWlseV9uYW1lIjoicmFqIiwibmFtZSI6IlJpdHUgcmFqIiwiZW1haWwiOiI0bmkxOGlzMDcxX2JAbmllLmFjLmluIiwic3ViIjoiNG5pMThpczA3MV9iQG5pZS5hYy5pbiIsImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6IjkzZWI1YzY4NDc4YjQ5N2NhZGZmZTg5NzE2ZDBlM2Y3IiwiZnJvemVuIjp0cnVlfSwiaWF0IjoxNjA3NzEyNDI4LCJleHAiOjE2MDc3MTYwMjgsImlzcyI6Imh0dHBzOi8vaWFtLmJsdWVtaXgubmV0L2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.RPq2kN7AlZS6Pax_rbM2NDLRnI8DAKirOjb0U4AIZNJhN6TLi447EBqAdXd0bcAlaMYPgNZF-jHMbyLepTh0Xw_rgmpTYBDMyp7sIgDcY3thtgqC3bN_KbdrYiMa2ZnZtgmZNMED5ty71upWBZQ0FQ-_RWm7UAnuuw3QkHzm8MIKIVGU8k-oS3FXPfvZG2ktYA1d0TWIHa61t40dHTtA3re4P-YlzZFNDECiMqPcj1r6HRxaWpGjDo_aJCYuatTuhoPChT7jZ7H5VDTEfxtET3lqg3vjz1q_AsHXQnj35cjRAHadeAjgT146InWu0dTOB4f4ROSpD5kCuwQl55OPwg","refresh_token":"OKBh1FV_0Z4EBaqzLLt-GqmWA-mF4pfpw6kbfS_FIhMAszPIpj_jmsnlXaT8Qj47Y0EdG_9eTrrxa-MP6B6Jvt09_wRRRX9ZSNfo-VMHo69PhfioMfBe9TDQXe7xBaBjYSjxBRfROf0WTXZVcZ5RrIw77oFHEPbFQDH6Q1iSLNBleOcTphFBIcNpG1JjTB-nopPxtAbzH4ZgTuSPflbOVYKzlTUSJELL_u1uO6wi8kgBLjNvxgby25kqtKd3wmhZbcX8HcKiA98shzMyg6ISpS41vJMrgfN11h6t-gfoEc0sq4CPqJI69W2-LoVY9CpqfG7_DmzEpyRO_DKKQx82PcvTYrEumYDbRVT1cVrZGeZgg4LGJ8e6gFldwFiiB8ZNvClJ69Rf2e5o5QQ8gpZbtY3ffthswydTsEBQ1vRF8T8AcC29LMSWNJALg5MJViomTcVqcNgTITHhWB4efpq0WJ3gSlOdDCJM_i2aITCdl4rTq3PiCa4bl6xQymCzBvsBI9DIg3Nv6G_t-Z005JofKz-pG8DRdoagotIt7uerClwbNKjqfCTE3kScwyhnFx-hFOIdjoa5Cwsmwy8A6DYR0rdMNVLU4M2DI8N7_8YJAViKvP0WJYaMr0mUPdNF-qJ2ffP4eazknnG7yilmjEq3tOZgXrpAY1k1ZdHpg0xh-1S_uyIkpG9Wr26He3u_FwNNnVki9tvPElFuDtsSXqOyoAPHB0s88jatAd_kf03fBYNW3QdNxDEr6W5-iXWW8UDdsjDGZpMYPi0OIrevnCgTpwg5QYq13l4608w85Cx14Lhm3mupzvN_pHroLIzfDW7iQWQVMq17WTBYndbLKIEea7mre1J_7xpR-W0i1yqKZwH_5vsSnlva77KXlIeW_XBVoYCHyCQeKfAOR4YUQtMINB54ZBqwyKtvBx_R68U5yqwoTf7lsXZqCPSJ34OqSHFHaTDRPEPNa3FAo8PDeEgGPdRsDuN3Q0gXgqZKs3NTF4V-odcM2jr2fzdiYq9XpmMP0Pp0Kxo29OBpfnMQYo6QbY71by9tHYIp1T7bdeDYGFwQM-pulTcV7-gjWFl4tU1dw1lShfXRFqkwFbQmqTy1DG8SWisVD3S7yyHjOP3dc2xdtg"}

        
        python_object = [float(form.Wind_Speed.data), float(form.Theoretical_Power_Curve.data), float(form.Wind_Direction.data)]
        #Transform python objects to  Json
        #print(python_object)
        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["Wind Speed (m/s)", "Theoretical_Power_Curve (KWh)", "Wind Direction (°)"], "values": userInput }]}
        #print(payload_scoring)
        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/ml/v4/deployments/685d0d82-7b7c-4bcb-bf36-05446c46c097/predictions?version=2020-11-30", json=payload_scoring, headers=header)
        print(response_scoring.text)
        output = json.loads(response_scoring.text)
        #print(output)
        for key in output:
          ab = output[key]
        

        for key in ab[0]:
          bc = ab[0][key]

  
        form.abc = bc[0][0] # this returns the response back to the front page
        return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
