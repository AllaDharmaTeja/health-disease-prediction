from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load dataset to get symptoms list
data = pd.read_csv("dataset/Testing.csv")
symptoms = data.columns[:-1]

@app.route("/")
def home():
    return render_template("index.html", symptoms=symptoms)

@app.route("/predict", methods=["POST"])
def predict():

    input_data = [0] * len(symptoms)

    selected = request.form.getlist("symptom")

    for s in selected:
        if s in symptoms:
            index = list(symptoms).index(s)
            input_data[index] = 1

    prediction = model.predict([input_data])

    return render_template(
        "index.html",
        symptoms=symptoms,
        prediction=prediction[0]
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
