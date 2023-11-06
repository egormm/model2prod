from flask import request, Flask, jsonify

from image_transform import image_to_matrix
from model import predict

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def post_predict_handler():
    if request.mimetype == 'application/json':
        features = request.json['images']
    else:
        file = request.files['images']
        features = image_to_matrix(file.read(), 32, 32)
    prediction = predict(features)
    return jsonify(prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
