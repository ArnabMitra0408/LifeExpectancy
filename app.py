from flask import Flask, request, render_template

import sklearn
import joblib
import pickle
import numpy as np

app = Flask(__name__)
model = joblib.load("regr.pkl")

with open('leCountry.pkl', 'rb') as f1:
    countrypkl = pickle.load(f1)
with open('leStatus.pkl', 'rb') as f2:
    Statuspkl = pickle.load(f2)

inputs=[]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def predict():
    if request.method=="POST":
        Country=countrypkl.transform([request.form["Country"]])[0]
        inputs.append(int(Country))
        inputs.append(int(request.form["Year"]))
        inputs.append(int(Statuspkl.transform([request.form["Status"]])[0]))
        inputs.append(float(request.form["ADR"]))
        inputs.append(int(request.form['Infant']))
        inputs.append(float(request.form["Alcohol"]))
        inputs.append(float(request.form["Expenditure"]))     
        inputs.append(float(request.form["HepB"]))
        inputs.append(int(request.form["Measles"]))
        inputs.append(float(request.form["BMI"]))
        inputs.append(int(request.form["Under5"]))
        inputs.append(float(request.form["polio"]))
        inputs.append(float(request.form["Expenditure2"]))
        inputs.append(float(request.form["diptheria"]))
        inputs.append(float(request.form["Aids"]))
        inputs.append(float(request.form["GDP"]))
        inputs.append(float(request.form["Population"]))
        inputs.append(float(request.form["thin1019"]))
        inputs.append(float(request.form["thin59"]))
        inputs.append(float(request.form["HDI"]))
        inputs.append(float(request.form["Schooling"]))
        print(Country)
        para=np.array(inputs)
        para=para.reshape(1,-1)
        life=model.predict(para)[0]
    return render_template("index.html",life_expectancy=life)

if __name__ == "__main__":
    app.run(debug=True)