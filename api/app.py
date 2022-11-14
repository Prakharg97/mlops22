from flask import Flask
from flask import jsonify
from flask import request
from joblib import dump, load

app = Flask(__name__)
model_path = "svm_gamma=0.001_C=0.5.joblib"
model = load(model_path)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sum", methods=["POST"])
def sum():
    x = request.json['x']
    y = request.json['y']
    z = x + y
    return {'sum': z}


@app.route("/predict", methods=['POST'])
def predict_digit():
    #print(request.json())
    image1 = request.json['image1']
    print(image1)
    image2 = request.json['image2']
    print("done loading")
    predicted1 = model.predict([image1])
    predicted2 = model.predict([image2])
    if predicted1 == predicted2:
        val = 'Same string'
    else:
        val = 'Different string'
    return {"prediction": val}

if __name__ == "__main__":
    app.run(port=5000,host="0.0.0.0")

