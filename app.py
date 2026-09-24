from flask import Flask, abort, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":
        abort(400)

    bedrooms = float(request.form["bedrooms"])
    bathrooms = float(request.form["bathrooms"])
    floors = float(request.form["floors"])
    yr_built = float(request.form["yr_built"])

    arr = np.array([
        bedrooms,
        bathrooms,
        floors,
        yr_built
    ]).reshape(1, -1)

    prediction = model.predict(arr)

    result = round(float(prediction[0]), 2)

    return render_template(
        "index.html",
        data=result
    )


if __name__ == "__main__":
    app.run(debug=True)