from flask import request, Flask, jsonify

from model import predict

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def get_predict_handler():
    features = list(map(float, request.args.get('features').split(',')))
    prediction = predict(features)
    return jsonify(prediction=prediction)


@app.route('/predict', methods=['POST'])
def post_predict_handler():
    features = request.json['features']
    prediction = predict(features)
    return jsonify(prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
